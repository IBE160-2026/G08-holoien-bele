---
title: "Case specification: The Last Invoice"
status: final
created: 2026-11-08
updated: 2026-11-08
---

# The Last Invoice — approved case specification

**Author spoilers throughout. Approved 2026-11-08, case version 1.0.** The user approved the complete case as drafted, explicitly including the admission-based ending. Names, culprit, fixed facts, exact dialogue, clue graph and ordered hint table are now the approved content contract. D-1 and D-2 are resolved. This approval does not claim that application or human playtests have been completed.

The [PRD](prd.md) controls general game rules. [case-data.json](case-data.json) contains the exact authored data and ordered response/hint conditions; the dialogue below mirrors it as the readable contract. Keep the two files synchronized for any approved revision. [case-validation.md](case-validation.md) records the model checks, reproducible with `python verify_case_spec.py`. This data is a planning artifact, not an implemented app.

Authored-data snapshot SHA-256 (BOM-free UTF-8 text, LF-normalized): `8701a8649e3efc9365ec5623b83e5e3a8553dbbe213cd00a4ccfd414113915b9`. The verifier checks this snapshot and all rendered response/card/hint text when validating the approved snapshot.

## Review summary

- Case: a small logistics-company owner is murdered shortly before a financial review; interviews take place at the police station.
- Cast: Nora Reed (business partner), Elias Ward (accountant), June Park (building caretaker). Nora is the culprit.
- Initial evidence: E1 incident summary and E2 appointment note. Discover E3 landing/intercom record, E4 supplier report, E5 recorded admission and E6 archive record.
- Required proof: E3 + E4 + E5 with Nora selected. No other three-item set gives full proof.
- No exploration, audio playback, uploads, signature capture, runtime AI, timer, trust/stress system or procedural variation is added.
- Nine-turn example route leaves three turns; the shortest expert route uses four. Actual pacing and appeal remain to be tested.

## Player briefing

Martin Hale, owner of North Quay Logistics, was found dead in his office at 19:10 on Friday evening. Police are treating his death as a murder. He had scheduled a review of unusual company payments for the next morning. Nora Reed, his business partner, Elias Ward, the accountant, and June Park, the building caretaker, are at the station to give statements. Read the incident summary and appointment note, question the three characters, and compare what they say with the records you uncover. You have 12 turns. A new question or confrontation costs one turn; reviewing material and asking for a hint are free. When ready, choose a culprit and up to three collected evidence items. Your confirmed accusation ends the attempt.

## Fixed author facts

- All people and events are fictional adults. The entire playable investigation takes place through station interviews and text evidence cards; no scene exploration, audio, document upload or signature-capture feature is required.
- Nora Reed murdered Martin Hale at 19:05 by striking him once with a desk paperweight during an argument over money she had diverted. Do not add injury details or graphic imagery.
- Nora left at 18:50, returned at 19:02 and left again at 19:08. Her original claim that she never returned is false.
- The office has one entrance from the third-floor landing. There is no usable second door or window entrance. The landing recording is complete, time-checked and unaltered. Do not invent a hidden route or camera failure.
- Martin spoke to June on the intercom at 19:04, confirming that Nora was with him. June discovered him dead at 19:10. Nora is the only visitor recorded in that interval before June arrived.
- Elias was in the records archive from 18:55 until 19:12, verified by the archive entry/exit recording. He had incorrectly claimed a GBP 300 personal expense, but did not murder Martin.
- June remained at the lobby desk until going to the office at 19:10. She holds an emergency key but did not use it during the murder interval and did not murder Martin.
- The payment report documents GBP 18,000 diverted to a supplier controlled by Nora, using her sole payment authorization. The GBP 300 expense issue is separate and must not be described as the GBP 18,000 diversion.
- Nora gives the recorded admission only after the player has collected the landing record and payment report and has confronted her with the landing record. No hidden trust score, exact wording puzzle or extra prerequisite exists.

## Cast, knowledge and secrets

### Nora Reed — Business partner

ID: `nora`.

**Player introduction:** Co-owner of North Quay Logistics. Says she left at 18:50 and did not return.

**Permitted knowledge and behaviour:** Knows the true meeting, diversion and murder. Initially conceals her return and describes the transfers as loans. After the landing confrontation admits the return but falsely claims Martin was alive when she left. After the combined confrontation admits the murder.

**Author-only secret:** Diverted GBP 18,000; killed Martin to prevent exposure. The culprit.

### Elias Ward — Accountant

ID: `elias`.

**Player introduction:** Prepared the payment review. Says he was retrieving files in the archive.

**Permitted knowledge and behaviour:** Knows the appointment, payment report and his own archive visit. Does not witness the murder or know Nora killed Martin before an admission is obtained.

**Author-only secret:** Claimed a GBP 300 personal expense. Embarrassed about it; separate from the major diversion and not the murderer.

### June Park — Building caretaker

ID: `june`.

**Player introduction:** Found Martin and supplied the appointment note. Has access to building records.

**Permitted knowledge and behaviour:** Knows the office access arrangement, the 19:04 intercom contact, the discovery, and the landing/archive records. Does not see the blow and must not claim to have witnessed it.

**Author-only secret:** No hidden crime or withheld murder witness statement. Possession of an emergency key is a lead to check, not proof of guilt.

## Fixed timeline

| Time | Fact |
|---|---|
| 18:40 | Elias gives Martin the payment report and is told to retrieve supporting files. |
| 18:45 | Martin writes the appointment note for Nora and notes the next-morning review. |
| 18:50 | Nora leaves the building, as she initially claims. |
| 18:55 | Elias enters the records archive. |
| 19:00 | Scheduled time of the meeting with Nora; she is late. |
| 19:02 | Nora returns and enters Martin's office from the landing. |
| 19:04 | Martin tells June on the intercom that Nora is with him and asks for a few minutes of privacy. |
| 19:05 | Nora kills Martin during their argument. June hears a brief clatter but does not see the attack. |
| 19:08 | Nora leaves the office and landing alone. |
| 19:10 | June goes to the office and discovers Martin dead. |
| 19:11 | June calls the police. |
| 19:12 | Elias leaves the records archive. |

## Evidence cards

Only these six designated items become evidence cards. Other interview context remains in the transcript; it does not silently create a seventh card. The initial/discovered and supporting/key classifications below are author metadata, not labels that reveal the proof set in the active player UI.

### E1 — Incident summary

Availability: initial. Author classification: supporting. Source: Initial police case file.

Martin Hale was found dead in his office at 19:10. June Park called the police at 19:11. The death is being investigated as a murder. Initial accounts: Nora Reed says she left at 18:50 and did not return. Elias Ward says he was in the records archive. June says she was at the lobby desk until checking the office. These are accounts to investigate, not verified conclusions.

### E2 — Appointment note

Availability: initial. Author classification: supporting. Source: Note supplied by June before the attempt.

A note in Martin's handwriting reads: '19:00 - Nora. Discuss the supplier transfers. Full payment review tomorrow, 08:00.' The note establishes an appointment and an issue to investigate; it does not establish who committed the murder.

### E3 — Landing and intercom record

Availability: discovered. Author classification: key. Source: June, J-Q2.

Time-checked building records show Nora entering Martin's office at 19:02 and leaving alone at 19:08. At 19:04 Martin tells June on the intercom: 'Nora is here. Give us a few minutes.' June is next seen entering at 19:10. No other person enters or leaves the office between 19:02 and 19:10. The office has one entrance, covered continuously by this recording; there is no alternate entrance. This contradicts Nora's claim that she never returned.

### E4 — Supplier payment report

Availability: discovered. Author classification: key. Source: Elias, E-Q2.

The report links GBP 18,000 in unauthorized supplier payments to a company controlled by Nora Reed. The bank references match the company ledger, and the payment authorizations are Nora's alone. Martin's review note says he will raise the diversion at the 08:00 review. Elias's GBP 300 personal-expense claim is listed separately and is not part of these transfers.

### E5 — Recorded admission

Availability: discovered. Author classification: key. Source: Nora, C-nora-E4-admission.

Nora's recorded statement: "You have the record of my return and the payments. Martin had found the money I diverted and said he would expose me at the review. During our argument I struck him with the desk paperweight. I acted alone and left at 19:08. That is my statement." The statement is corroborated by the landing/intercom record and the supplier payment report.

### E6 — Archive attendance record

Availability: discovered. Author classification: supporting. Source: June, J-Q3.

The archive entrance recording shows Elias entering at 18:55 and not leaving until 19:12. It is time-checked against the building system and shows no intermediate exit. This corroborates his archive account during the office incident. It does not establish the murderer's identity or motive on its own.

## State and action contract

1. A fresh active attempt has E1/E2, no flags, 12 turns and an empty transcript/action history. Evidence and flags only accumulate until a confirmed restart. The only case flags are `nora_return_admitted` and `nora_confessed`.
2. Conditions are conjunctions: every token in `requires_all` must be present as a collected evidence ID or true flag. Questions with unmet prerequisites are hidden. No extra prerequisite may be added to an authored action.
3. For a question not previously answered, choose the first eligible response in its listed priority order, charge one turn and save its response ID/text and effects together. There is no free-text matching. For an answered question, show its originally saved response for free, even if a later variant would now be eligible. Label it as previous testimony; do not silently rewrite a lie after it has been exposed. New follow-ups have separate IDs.
4. For a confrontation, the evidence item must already be collected. All 18 character/item pairs are specified below. Choose the first eligible response branch in priority order. A branch not previously delivered costs one turn, even if it grants nothing. A previously delivered selected branch is free replay. Free repeat means the same pair and branch, not merely identical wording on some other action.
5. C-nora-E4 is deliberately state-dependent: the earlier deflection becomes a new paid admission exchange after the landing confrontation. If the advanced branch is already recorded, replay it; do not offer an unseen lower branch as another paid action.
6. At zero turns, block every new exchange. Previously saved answers/confrontations remain accessible from history for free, even if a different new branch has become eligible. Reviewing a previous response must not trigger that new branch.
7. Automatic collection and flag effects occur only on successful completion of a new action. Reviewing, switching, hints and repeated branches do not apply effects again. Invalid IDs, unavailable evidence, locked actions and stale/conflicting requests do not charge turns; use the PRD reliability policy.
8. NPC text, initial evidence and the case truth are fixed. New facts must not be generated. Evidence order within the final three-item selection does not matter, and duplicate selections are not permitted.
9. The admission does not automatically end the attempt. The player may still review, use remaining turns or accuse. Only confirmed accusation ends it; restart is separately confirmed. Verdict/reveal/retained-result behaviour follows the PRD.
10. Player-facing text is the briefing, introductions, prompts, chosen response text, collected card text, hint text and deliberate solution reveal. Do not display author truth notes, key-item markers, hidden prerequisites or the locked dialogue catalogue during active play. Repository source visibility is not an anti-cheat guarantee.

## All selectable questions and exact responses

Each character begins with four available questions. Two follow-ups per character have the explicit prerequisites shown. Variants are evaluated only on the first asking; historical rereading remains free.

### Nora Reed

#### N-Q1 — Walk me through your departure.

**Question availability:** Always (subject to action prerequisites).

**Response 1: `N-Q1-after-return`** — `nora_return_admitted`.

> I left at 18:50, then came back at 19:02. I went straight to Martin's office and left again at 19:08. You have the landing record now.

**Effects:** No evidence/flag change.

**Response 2: `N-Q1-initial`** — Always (subject to action prerequisites).

> I left at 18:50 and went to my car. I did not return to the office. I cannot tell you what happened after I left.

**Effects:** No evidence/flag change.

**Author-only truth note:** Knowingly lies about returning; the 18:50 departure itself is true.

#### N-Q2 — Why did Martin want to meet you?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `N-Q2-after-admission`** — `nora_confessed`.

> He had found the money I diverted. The morning review would expose it. I wanted him to delay it.

**Effects:** No evidence/flag change.

**Response 2: `N-Q2-initial`** — Always (subject to action prerequisites).

> There was a disagreement over supplier transfers. I called them short-term loans. Martin wanted to discuss the paperwork before the morning review.

**Effects:** No evidence/flag change.

**Author-only truth note:** Minimizes the unauthorized diversion as loans; do not change the verified payment facts.

#### N-Q3 — What can you tell me about the other two?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `N-Q3-answer`** — Always (subject to action prerequisites).

> Elias kept the accounts and June looked after the building. Elias was worried about an expense claim. June had an emergency key. They can explain those matters themselves.

**Effects:** No evidence/flag change.

#### N-Q4 — Did you hear an argument that evening?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `N-Q4-after-admission`** — `nora_confessed`.

> Martin and I argued about the money. I struck him during that argument. I have already given you the account of what I did.

**Effects:** No evidence/flag change.

**Response 2: `N-Q4-after-return`** — `nora_return_admitted`.

> Our discussion became heated. I wanted the review delayed. I am not going to describe it further just now.

**Effects:** No evidence/flag change.

**Response 3: `N-Q4-initial`** — Always (subject to action prerequisites).

> I had already left. I cannot describe an argument in the office after 19:00.

**Effects:** No evidence/flag change.

**Author-only truth note:** Deflects by repeating the false never-returned account.

#### N-F1 — Why did you come back after leaving?

**Question availability:** `nora_return_admitted`.

**Response 1: `N-F1-after-admission`** — `nora_confessed`.

> I came back because Martin had found the transfers and would not delay the review. That is why we argued.

**Effects:** No evidence/flag change.

**Response 2: `N-F1-before-admission`** — Always (subject to action prerequisites).

> Martin wanted an explanation before the review. I thought I could persuade him to postpone it. He was still alive when I left.

**Effects:** No evidence/flag change.

**Author-only truth note:** Admits return/motive pressure but falsely claims Martin was alive on departure.

#### N-F2 — What did you do after the argument?

**Question availability:** `nora_confessed`.

**Response 1: `N-F2-answer`** — Always (subject to action prerequisites).

> I left the office alone at 19:08. I did not stay to call for help. The building record shows my departure.

**Effects:** No evidence/flag change.

### Elias Ward

#### E-Q1 — Where were you around 19:00?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `E-Q1-answer`** — Always (subject to action prerequisites).

> I entered the records archive at 18:55 to retrieve old invoices. I stayed until 19:12. June can provide the archive entry and exit record.

**Effects:** No evidence/flag change.

#### E-Q2 — What was the payment review meant to examine?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `E-Q2-answer`** — Always (subject to action prerequisites).

> I prepared a report on GBP 18,000 sent to a supplier controlled by Nora. The bank references and her payment authorizations match the ledger. Martin planned to raise it at 08:00. Here is the report. My own expense mistake is listed separately.

**Effects:** collect `E4`

#### E-Q3 — Did you have a dispute with Martin?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `E-Q3-answer`** — Always (subject to action prerequisites).

> He challenged a GBP 300 reimbursement of mine. It was a personal expense I should not have claimed. I was embarrassed and worried about my job. That is separate from the supplier transfers.

**Effects:** No evidence/flag change.

#### E-Q4 — Who knew about the review?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `E-Q4-answer`** — Always (subject to action prerequisites).

> Martin, Nora and I had the agenda. June knew there was an evening meeting, but I did not discuss the payment report with her. Martin asked me to retrieve supporting invoices from the archive.

**Effects:** No evidence/flag change.

#### E-F1 — How does your expense claim relate to the report?

**Question availability:** `E4`.

**Response 1: `E-F1-answer`** — Always (subject to action prerequisites).

> It is a separate GBP 300 entry. The GBP 18,000 went through Nora's sole authorizations to a supplier she controlled. My incorrect reimbursement does not account for those transfers.

**Effects:** No evidence/flag change.

#### E-F2 — Does the archive record cover the whole interval?

**Question availability:** `E6`.

**Response 1: `E-F2-answer`** — Always (subject to action prerequisites).

> Yes. I entered at 18:55 and left at 19:12. I was looking through old invoices the whole time. I did not make an intermediate trip to Martin's office.

**Effects:** No evidence/flag change.

### June Park

#### J-Q1 — Tell me how you found Martin.

**Question availability:** Always (subject to action prerequisites).

**Response 1: `J-Q1-answer`** — Always (subject to action prerequisites).

> At 19:04 Martin spoke to me on the intercom. He said Nora was with him and asked for a few minutes of privacy. I heard a short clatter around 19:05 but did not see what caused it. I checked the office at 19:10 and found him dead. I called the police at 19:11.

**Effects:** No evidence/flag change.

#### J-Q2 — Are there records of movement near the office?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `J-Q2-answer`** — Always (subject to action prerequisites).

> Yes. The landing recording shows Nora entering at 19:02 and leaving at 19:08, then me arriving at 19:10. Nobody else enters in between. The time check and Martin's 19:04 intercom contact are included. Here is the complete record.

**Effects:** collect `E3`

#### J-Q3 — Can you check Elias's archive account?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `J-Q3-answer`** — Always (subject to action prerequisites).

> The archive recording shows him entering at 18:55 and leaving at 19:12, with no exit between those times. Here is the attendance record.

**Effects:** collect `E6`

#### J-Q4 — Who could enter Martin's office?

**Question availability:** Always (subject to action prerequisites).

**Response 1: `J-Q4-answer`** — Always (subject to action prerequisites).

> Martin and Nora normally used it. I hold an emergency key. There is only one entrance, from the recorded third-floor landing, and no usable window entrance. I was at the lobby desk until I went up at 19:10.

**Effects:** No evidence/flag change.

#### J-F1 — Could someone have entered without appearing in the record?

**Question availability:** `E3`.

**Response 1: `J-F1-answer`** — Always (subject to action prerequisites).

> Not through another route. The office has one entrance and the recording covers it continuously. The time check is complete. I did not see the attack, so I can only speak to those records and my intercom contact.

**Effects:** No evidence/flag change.

#### J-F2 — What supports the archive entry and exit times?

**Question availability:** `E6`.

**Response 1: `J-F2-answer`** — Always (subject to action prerequisites).

> The recording covers the archive entrance continuously and is time-checked to the same building clock. It shows no intermediate exit by Elias. It is more than a name written on a sign-in sheet.

**Effects:** No evidence/flag change.

## Complete confrontation matrix

Every pair below requires its named evidence item to be collected. All are visible options once that item is collected; do not highlight whether a pairing will succeed. Each first new branch costs one turn. Previously recorded branches can be reviewed for free. The special C-nora-E4 branches are ordered most advanced first.

### Present evidence to Nora Reed

#### C-nora-E1 — Incident summary

**Priority 1: `C-nora-E1-no-new-information`** — `E1`.

> I have nothing further to add to that incident summary.

**Effects:** No evidence/flag change.

#### C-nora-E2 — Appointment note

**Priority 1: `C-nora-E2-no-new-information`** — `E2`.

> The appointment note is real. I have nothing further to add about the note itself.

**Effects:** No evidence/flag change.

#### C-nora-E3 — Landing and intercom record

**Priority 1: `C-nora-E3-return`** — `E3`.

> That is me in the record. I came back at 19:02 to speak to Martin and left at 19:08. I did not want to admit we had argued. He was still alive when I left.

**Effects:** set `nora_return_admitted`

**Author-only truth note:** Return is true; alive-on-departure claim is false.

#### C-nora-E4 — Supplier payment report

**Priority 1: `C-nora-E4-admission`** — `E3` AND `E4` AND `nora_return_admitted`.

> You have the record of my return and the payments. Martin had found the money I diverted and said he would expose me at the review. During our argument I struck him with the desk paperweight. I acted alone and left at 19:08. That is my statement.

**Effects:** collect `E5`; set `nora_confessed`

**Author-only truth note:** Truthful admission, corroborated by E3/E4; creates text evidence E5.

**Priority 2: `C-nora-E4-deflection`** — `E4`.

> I authorized those transfers as loans. Martin and I disagreed over the paperwork. A payment report does not tell you what happened in his office after I left.

**Effects:** No evidence/flag change.

**Author-only truth note:** False loan explanation and misleading departure claim. No evidence or milestone is granted.

#### C-nora-E5 — Recorded admission

**Priority 1: `C-nora-E5-no-new-information`** — `E5`.

> That is the statement I have just given. I have nothing to add to it.

**Effects:** No evidence/flag change.

#### C-nora-E6 — Archive attendance record

**Priority 1: `C-nora-E6-no-new-information`** — `E6`.

> That is Elias's archive record. I cannot add anything about that item.

**Effects:** No evidence/flag change.

### Present evidence to Elias Ward

#### C-elias-E1 — Incident summary

**Priority 1: `C-elias-E1-no-new-information`** — `E1`.

> I have nothing further to add to that incident summary.

**Effects:** No evidence/flag change.

#### C-elias-E2 — Appointment note

**Priority 1: `C-elias-E2-no-new-information`** — `E2`.

> I recognize the appointment note. I have no further information about the note itself.

**Effects:** No evidence/flag change.

#### C-elias-E3 — Landing and intercom record

**Priority 1: `C-elias-E3-no-new-information`** — `E3`.

> The landing record speaks for itself. I have no further information to add about it.

**Effects:** No evidence/flag change.

#### C-elias-E4 — Supplier payment report

**Priority 1: `C-elias-E4-no-new-information`** — `E4`.

> Those are the payment records I supplied. I have no new information to add to that report.

**Effects:** No evidence/flag change.

#### C-elias-E5 — Recorded admission

**Priority 1: `C-elias-E5-no-new-information`** — `E5`.

> I have nothing to add to Nora's recorded statement.

**Effects:** No evidence/flag change.

#### C-elias-E6 — Archive attendance record

**Priority 1: `C-elias-E6-no-new-information`** — `E6`.

> That is the archive record. I have no further information to add about it.

**Effects:** No evidence/flag change.

### Present evidence to June Park

#### C-june-E1 — Incident summary

**Priority 1: `C-june-E1-no-new-information`** — `E1`.

> I have no further information to add to that incident summary.

**Effects:** No evidence/flag change.

#### C-june-E2 — Appointment note

**Priority 1: `C-june-E2-no-new-information`** — `E2`.

> That is the note I handed over. I have no further information about the note itself.

**Effects:** No evidence/flag change.

#### C-june-E3 — Landing and intercom record

**Priority 1: `C-june-E3-no-new-information`** — `E3`.

> That is the complete landing and intercom record. I cannot add anything further to it.

**Effects:** No evidence/flag change.

#### C-june-E4 — Supplier payment report

**Priority 1: `C-june-E4-no-new-information`** — `E4`.

> I do not handle company payments. I cannot add anything about that report.

**Effects:** No evidence/flag change.

#### C-june-E5 — Recorded admission

**Priority 1: `C-june-E5-no-new-information`** — `E5`.

> I have nothing to add to that recorded statement.

**Effects:** No evidence/flag change.

#### C-june-E6 — Archive attendance record

**Priority 1: `C-june-E6-no-new-information`** — `E6`.

> That is the archive export I supplied. There is no additional entry to explain.

**Effects:** No evidence/flag change.

## Milestones and deterministic hints

### Explicit discovery milestones

| ID | Trigger token becomes present | Meaning |
|---|---|---|
| M-landing | `E3` | Landing/intercom evidence collected |
| M-payments | `E4` | Payment evidence collected |
| M-archive | `E6` | Archive evidence collected; may leave the highest-priority hint unchanged |
| M-return | `nora_return_admitted` | Nora confronted with landing record and admits return |
| M-admission | `nora_confessed` | Corroborated admission obtained; E5 collected in the same action |

A milestone can enable a different hint but need not change it if the same higher-priority rule still applies. Ordinary turn spending, wrong/unchanged confrontations, free review and hint clicks do not advance a hidden hint counter. Reaching zero turns is the separate permitted mode change.

### Selection rules

Evaluate the following from top to bottom whenever the player requests a hint. Return the first matching rule. `requires_none` means that none of those tokens may be present. At positive turns, every suggested new action is legal and produces case progress; if proof is complete, guide deliberation instead. At zero turns, never suggest obtaining new information. Hint requests do not mutate evidence, flags or budget.

**H-zero:** remaining turns = 0.

> No turns remain. Review the evidence and interview history you have already collected, then decide whom you can accuse and which items support it. You can still submit an accusation.

Author-only suggested action: `review`.

**H-ready:** all of `nora_confessed`.

> Compare the statements and records you have collected. Choose the person whose account fits the facts and the evidence that supports your accusation.

Author-only suggested action: `accuse`.

**H-combine:** all of `E3`, `E4`, `nora_return_admitted`.

> Now that the departure account has changed, present the payment report to the person connected to those transfers.

Author-only suggested action: `C-nora-E4`.

**H-return:** all of `E3`; none of `nora_return_admitted`.

> Compare the landing record with the departure account in the incident summary. Present the record to the person whose account it contradicts.

Author-only suggested action: `C-nora-E3`.

**H-payments:** all of `nora_return_admitted`; none of `E4`.

> Ask the accountant what the scheduled payment review was meant to examine.

Author-only suggested action: `E-Q2`.

**H-landing:** Fallback for every other reachable state.

> Ask the building caretaker about records of movement near the office.

Author-only suggested action: `J-Q2`.

## Proof, verdict and solution

- Correct culprit: `nora`.
- Full proof requires exactly the set `{E3, E4, E5}`; order is irrelevant.
- Nora with zero to three collected items but an incomplete/replaced proof set: correct culprit with insufficient proof.
- Elias or June with any allowed evidence selection: wrong culprit.
- Do not automatically show the solution or list missing key items in the verdict. Show the submitted accusation and outcome as the PRD requires.

### Exact post-verdict solution text

Nora Reed killed Martin Hale. She claimed she never returned after 18:50, but the landing and intercom record places her alone with him while he was alive at 19:04, before she left at 19:08 and June found him at 19:10. The supplier payment report explains why she wanted the review stopped: Martin had found GBP 18,000 diverted through her authorizations. Confronted with her return and the payment report, Nora admitted striking Martin with the desk paperweight and leaving at 19:08. The required proof set is the landing/intercom record, supplier payment report and corroborated recorded admission. The appointment note and incident summary establish context; the archive record supports Elias's account. Elias's separate GBP 300 expense mistake and June's emergency key do not make either the murderer.

## Demonstrated routes and verification

**Shortest route (four turns):** E-Q2 -> J-Q2 -> C-nora-E3 -> C-nora-E4. It collects the two independent records, obtains the admission and leaves eight turns. The initial case file already records Nora's departure claim, so N-Q1 is not an artificial prerequisite.

**Example investigation (nine turns):** N-Q1 -> J-Q1 -> J-Q2 -> J-Q3 -> E-Q1 -> E-Q2 -> C-nora-E3 -> N-F1 -> C-nora-E4. It checks accounts and the archive lead before proving the case, leaving three turns.

**Changed-confrontation example:** E-Q2 -> C-nora-E4 gives the deflection. Repeating it immediately is free. J-Q2 -> C-nora-E3 then unlocks the new C-nora-E4 admission branch, which costs one turn. Repeating the admission is free.

The [validation report](case-validation.md) contains counts, methodology, limits and the input-data hash. Its pure model verifies the approved graph, not application behaviour. It does not constitute the planned blind agent or human playtests.

## Approved design choices and revision control

- Approved finale: the advanced confrontation yields an explicit corroborated admission. The introductory challenge is exposing the false account and assembling proof, rather than concealing the culprit until the verdict.
- Approved routes: an expert can prove the case in four charged actions; the example investigation takes nine. Twelve is a ceiling, not a minimum. The approximately 15-minute pacing target still requires real playtesting.
- Approved evidence split: two initial supporting cards and four discoveries, including all three required proof items. Other dialogue remains in the transcript rather than creating additional evidence cards.
- The user approved the complete case as drafted, including names, culprit, timeline, exact dialogue, graph, hint table and admission-based ending, on 2026-11-08. Any revision requires a recorded approval and revalidation.

Case approval is recorded in the PRD decision log. Preserve stable IDs when possible and rerun the model checker after any approved data edit. The implementing agent must not rewrite lines, invent facts or add branches to improve the story without an approved revision.
