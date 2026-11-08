"""Validate the case's authored graph; this is not the application engine."""
from collections import deque
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def source_digest(path):
    """Hash BOM-free UTF-8 text with LF newlines across Git checkouts."""
    return sha256(path.read_text(encoding='utf-8-sig').encode('utf-8')).hexdigest()

@dataclass(frozen=True)
class State:
    tokens: frozenset
    turns: int
    answers: tuple = ()
    seen: frozenset = frozenset()

class Model:
    def __init__(self, data):
        self.data = data
        self.questions = {x['id']: x for x in data['questions']}
        self.confrontations = {x['id']: x for x in data['confrontations']}
        self.responses = {r['id']: r for a in data['questions']+data['confrontations'] for r in a['responses']}
    def initial(self):
        return State(frozenset(self.data['initial_evidence']+self.data['initial_flags']), self.data['starting_turns'])
    def step(self, state, aid):
        answers = dict(state.answers)
        if aid in self.questions:
            action = self.questions[aid]
            if aid in answers:
                return state, answers[aid], 0
            if not set(action['requires_all']) <= state.tokens:
                raise ValueError('Locked question')
        elif aid in self.confrontations:
            action = self.confrontations[aid]
            if action['evidence_id'] not in state.tokens:
                raise ValueError('Evidence not collected')
        else:
            raise ValueError('Unknown action')
        branch = next(r for r in action['responses'] if set(r['requires_all']) <= state.tokens)
        if aid in self.confrontations and branch['id'] in state.seen:
            return state, branch['id'], 0
        if state.turns == 0:
            raise ValueError('No turns for a new exchange')
        tokens = state.tokens | frozenset(branch['grant_evidence']+branch['set_flags'])
        if aid in self.questions:
            answers[aid] = branch['id']
        return State(tokens, state.turns-1, tuple(sorted(answers.items())), state.seen | {branch['id']}), branch['id'], 1
    def hint(self, state):
        return next(h for h in self.data['hint_rules']
                    if (h['turns_eq'] is None or state.turns == h['turns_eq'])
                    and set(h['requires_all']) <= state.tokens
                    and not set(h['requires_none']) & state.tokens)
    def route(self, aids):
        state, rows = self.initial(), []
        for aid in aids:
            state, branch, cost = self.step(state, aid)
            rows.append((aid,branch,cost,state.turns))
        return state,rows

def verify(data):
    evidence = {e['id'] for e in data['evidence']}
    assert data['starting_turns'] == 12
    assert len(data['evidence']) == 6
    assert evidence == {f'E{i}' for i in range(1,7)}
    assert len(data['characters']) == 3
    assert {c['id'] for c in data['characters']} == {'nora','elias','june'}
    assert data['initial_evidence'] == ['E1','E2']
    assert set(data['required_proof']) == {'E3','E4','E5'}
    assert not set(data['initial_evidence']) & set(data['required_proof'])
    assert {e['id'] for e in data['evidence'] if e['initial']} == set(data['initial_evidence'])
    assert {e['id'] for e in data['evidence'] if e['author_kind'] == 'key'} == set(data['required_proof'])
    assert len(data['questions']) == 18 and len(data['confrontations']) == 18
    flags = {'nora_return_admitted','nora_confessed'}
    tokens = evidence | flags
    ids = []
    grants = {eid: [] for eid in evidence}
    for a in data['questions']+data['confrontations']:
        ids.append(a['id'])
        assert a['character_id'] in {'nora','elias','june'}
        assert set(a.get('requires_all',[])) <= tokens
        if a in data['questions']:
            assert not a['responses'][-1]['requires_all'], 'Question needs a final fallback'
        else:
            assert set(a['responses'][-1]['requires_all']) <= {a['evidence_id']}, 'Confrontation needs an inventory-covered fallback'
        for r in a['responses']:
            ids.append(r['id'])
            assert set(r['requires_all']) <= tokens
            assert set(r['grant_evidence']) <= evidence
            assert set(r['set_flags']) <= flags
            for eid in r['grant_evidence']:
                grants[eid].append(r['id'])
    assert len(ids) == len(set(ids)), 'Duplicate action/response ID'
    assert all(len(grants[eid]) == 1 for eid in ['E3','E4','E5','E6'])
    assert not grants['E1'] and not grants['E2']
    assert len({h['id'] for h in data['hint_rules']}) == len(data['hint_rules'])
    for h in data['hint_rules']:
        assert set(h['requires_all']+h['requires_none']) <= tokens
    assert not data['hint_rules'][-1]['requires_all'] and not data['hint_rules'][-1]['requires_none'] and data['hint_rules'][-1]['turns_eq'] is None
    assert {(c['character_id'],c['evidence_id']) for c in data['confrontations']} == {(c['id'],e) for c in data['characters'] for e in evidence}
    model = Model(data)
    actions = list(model.questions)+list(model.confrontations)
    # Authoring graph proof: cost-only exchanges cannot unlock any branch, so
    # collapse their history and keep minimum cost for each evidence/flag state.
    start = model.initial().tokens
    paths = {start: []}
    queue = deque([start])
    while queue:
        ts = queue.popleft()
        route = paths[ts]
        if len(route) >= data['starting_turns']:
            continue
        for aid in actions:
            try:
                nxt,_,cost = model.step(State(ts,data['starting_turns']-len(route)),aid)
            except ValueError:
                continue
            if nxt.tokens != ts and nxt.tokens not in paths:
                assert cost == 1
                paths[nxt.tokens] = route+[aid]
                queue.append(nxt.tokens)
    proof = set(data['required_proof'])
    wins = [r for ts,r in paths.items() if proof <= ts]
    shortest = min(wins,key=len)
    assert len(shortest) <= 12
    checked_hints = 0
    for ts,route in paths.items():
        assert ('E5' in ts) == ('nora_confessed' in ts)
        assert 'nora_return_admitted' not in ts or 'E3' in ts
        for turns in range(13-len(route)):
            s = State(ts,turns)
            h = model.hint(s)
            checked_hints += 1
            if turns == 0:
                assert h['id'] == 'H-zero' and h['suggested_action'] == 'review'
            elif h['suggested_action'] == 'accuse':
                assert proof <= ts
            else:
                nxt,_,cost = model.step(s,h['suggested_action'])
                assert cost == 1 and nxt.tokens != ts, (h['id'],ts)
    usual = ['N-Q1','J-Q1','J-Q2','J-Q3','E-Q1','E-Q2','C-nora-E3','N-F1','C-nora-E4']
    usual_state,usual_rows = model.route(usual)
    assert proof <= usual_state.tokens and usual_state.turns == 3
    early = ['E-Q2','C-nora-E4']
    s, _ = model.route(early)
    old = s
    s, branch, cost = model.step(s,'C-nora-E4')
    assert s == old and cost == 0 and branch.endswith('deflection')
    s,_,_ = model.step(s,'J-Q2')
    s,_,_ = model.step(s,'C-nora-E3')
    s,branch,cost = model.step(s,'C-nora-E4')
    assert cost == 1 and branch.endswith('admission') and proof <= s.tokens
    after = s
    s,_,cost = model.step(s,'C-nora-E4')
    assert s == after and cost == 0
    s,_ = model.route(['N-Q1','J-Q2','E-Q2','C-nora-E3','C-nora-E4'])
    old = s
    s,branch,cost = model.step(s,'N-Q1')
    assert s == old and cost == 0 and branch == 'N-Q1-initial'
    s = model.initial()
    initial_hint = model.hint(s)['id']
    s,_,_ = model.step(s,'N-Q3')
    assert model.hint(s)['id'] == initial_hint
    zero = model.initial()
    for aid in actions:
        if zero.turns == 0:
            break
        try:
            nxt,_,cost = model.step(zero,aid)
        except ValueError:
            continue
        if nxt.tokens == zero.tokens and cost == 1:
            zero = nxt
    assert zero.turns == 0 and model.hint(zero)['id'] == 'H-zero'
    try:
        model.step(zero,'J-Q2')
        raise AssertionError('New exchange accepted at zero turns')
    except ValueError:
        pass
    replay,_,cost = model.step(zero,'N-Q1')
    assert replay == zero and cost == 0
    verdict_counts = {'wrong culprit':0,'insufficient proof':0,'fully proved':0}
    from itertools import combinations
    for culprit in [c['id'] for c in data['characters']]:
        for n in range(4):
            for selected in combinations(sorted(evidence),n):
                outcome = 'wrong culprit' if culprit != data['culprit_id'] else ('fully proved' if set(selected)==proof else 'insufficient proof')
                verdict_counts[outcome] += 1
    assert verdict_counts == {'wrong culprit':84,'insufficient proof':41,'fully proved':1}
    return dict(plot_states=len(paths),hint_checks=checked_hints,shortest=shortest,usual=usual_rows,verdict_counts=verdict_counts)

def main():
    source = ROOT/'case-data.json'
    data = json.loads(source.read_text(encoding='utf-8'))
    readable = (ROOT/'case-spec.md').read_text(encoding='utf-8')
    assert source_digest(source) in readable, 'Readable specification snapshot is stale'
    for item in data['evidence']:
        assert item['text'] in readable, item['id']
    for action in data['questions']+data['confrontations']:
        for branch in action['responses']:
            assert branch['text'] in readable, branch['id']
    for hint in data['hint_rules']:
        assert hint['text'] in readable, hint['id']
    assert data['player_briefing'] in readable and data['solution_text'] in readable
    result = verify(data)
    report = [
        '# Case-model validation: The Last Invoice', '',
        ('Status: PASS for the approved authoring model. Human case approval recorded on '+data['approved_on']+'.' if data.get('status') == 'approved' else 'Status: PASS for the draft authoring model. Human approval is pending.'), '',
        f'- Input: `case-data.json`, version `{data["version"]}`.',
        f'- Input SHA-256 (BOM-free UTF-8 text, LF-normalized): `{source_digest(source)}`.',
        '- The readable case snapshot and all rendered evidence, response, hint, briefing and solution text match the authored data.',
        '- Run: `python verify_case_spec.py` from this directory, or invoke it by path.',
        f'- Structural checks: three characters, six evidence items, two initial supporting items, four discovered items, 18 questions, 18 confrontation pairs and unique action/response IDs.',
        f'- Reachable plot states: {result["plot_states"]}. Minimum-cost search collapses cost-only exchanges because no unlock condition depends on their history; it does not claim to enumerate all transcript permutations.',
        f'- Hint checks: {result["hint_checks"]} plot-state/remaining-turn combinations. At positive turns, guidance targets a legal progress-producing action or a fully supported accusation; at zero it targets review.',
        '- Checks passed for free unchanged confrontation replay, charged later admission branch, free admission replay, preservation of historical answers, no hint advance from an ordinary spent turn, exhausted-budget blocking and free historical review.',
        '- Verdict classification covers all 126 permitted culprit/evidence-set combinations across the six items: 84 wrong-culprit, 41 insufficient-proof and exactly one fully-proved combination. This checks the authored rule, not application endpoints.', '',
        '## Shortest proof route', '',
        ' -> '.join(result['shortest'])+f' ({len(result["shortest"])} turns; {12-len(result["shortest"])} remaining).', '',
        '## Example nine-turn investigation', '',
        '| Action | Delivered response | Cost | Turns left |', '|---|---|---|---|'
    ]
    report += [f'| {a} | {r} | {cost} | {left} |' for a,r,cost,left in result['usual']]
    report += ['', '## Limits', '',
        'This is a deterministic authoring-model check, not a browser, database, concurrency, ownership, performance or real application test. It does not prove that humans find the mystery compelling or finish in 15 minutes. The 12 agent sessions and three human sessions remain future work. D-1/D-2 approval is recorded for version 1.0; any revised draft needs renewed approval before replacing that contract.', '']
    (ROOT/'case-validation.md').write_text('\n'.join(report),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))

if __name__ == '__main__':
    main()
