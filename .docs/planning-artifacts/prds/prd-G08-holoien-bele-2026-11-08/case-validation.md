# Case-model validation: The Last Invoice

Status: PASS for the approved authoring model. Human case approval recorded on 2026-11-08.

- Input: `case-data.json`, version `1.0`.
- Input SHA-256 (BOM-free UTF-8 text, LF-normalized): `8701a8649e3efc9365ec5623b83e5e3a8553dbbe213cd00a4ccfd414113915b9`.
- The readable case snapshot and all rendered evidence, response, hint, briefing and solution text match the authored data.
- Run: `python verify_case_spec.py` from this directory, or invoke it by path.
- Structural checks: three characters, six evidence items, two initial supporting items, four discovered items, 18 questions, 18 confrontation pairs and unique action/response IDs.
- Reachable plot states: 14. Minimum-cost search collapses cost-only exchanges because no unlock condition depends on their history; it does not claim to enumerate all transcript permutations.
- Hint checks: 149 plot-state/remaining-turn combinations. At positive turns, guidance targets a legal progress-producing action or a fully supported accusation; at zero it targets review.
- Checks passed for free unchanged confrontation replay, charged later admission branch, free admission replay, preservation of historical answers, no hint advance from an ordinary spent turn, exhausted-budget blocking and free historical review.
- Verdict classification covers all 126 permitted culprit/evidence-set combinations across the six items: 84 wrong-culprit, 41 insufficient-proof and exactly one fully-proved combination. This checks the authored rule, not application endpoints.

## Shortest proof route

E-Q2 -> J-Q2 -> C-nora-E3 -> C-nora-E4 (4 turns; 8 remaining).

## Example nine-turn investigation

| Action | Delivered response | Cost | Turns left |
|---|---|---|---|
| N-Q1 | N-Q1-initial | 1 | 11 |
| J-Q1 | J-Q1-answer | 1 | 10 |
| J-Q2 | J-Q2-answer | 1 | 9 |
| J-Q3 | J-Q3-answer | 1 | 8 |
| E-Q1 | E-Q1-answer | 1 | 7 |
| E-Q2 | E-Q2-answer | 1 | 6 |
| C-nora-E3 | C-nora-E3-return | 1 | 5 |
| N-F1 | N-F1-before-admission | 1 | 4 |
| C-nora-E4 | C-nora-E4-admission | 1 | 3 |

## Limits

This is a deterministic authoring-model check, not a browser, database, concurrency, ownership, performance or real application test. It does not prove that humans find the mystery compelling or finish in 15 minutes. The 12 agent sessions and three human sessions remain future work. D-1/D-2 approval is recorded for version 1.0; any revised draft needs renewed approval before replacing that contract.
