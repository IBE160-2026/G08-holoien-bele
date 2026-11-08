# Confirmed UX source context

Extracted 2026-11-08 for UX discovery. This is a source digest, not an approved visual or layout contract. It does not choose page boundaries, navigation containers, colors, typography or a UI kit.

## Authoritative inputs

- [Final PRD](../../prds/prd-G08-holoien-bele-2026-11-08/prd.md): product behaviour, FR-1–FR-15, NFR-1–NFR-7 and UJ-1–UJ-4.
- [PRD addendum](../../prds/prd-G08-holoien-bele-2026-11-08/addendum.md): approved account/session policies P-1/P-2 and acceptance setup P-3.
- [Approved case version 1.0](../../prds/prd-G08-holoien-bele-2026-11-08/case-spec.md): exact text, evidence, conditions and hint selection. Case approval includes the admission-based finale; UX must not rewrite its facts or add dialogue.

All D-1–D-6 product/content decisions are resolved. Public product naming remains a UX/brand decision: “AI Detective Game” is a working project title; “The Last Invoice” is the approved case title. Do not treat either as the confirmed website brand yet.

## Experience to preserve

- English-language, serious but easy-to-understand murder investigation for crime-fiction fans and genre newcomers. No graphic descriptions/imagery. Approximately 15 minutes is a pacing target, not a countdown.
- One fixed case and three interviewable characters: Nora Reed, Elias Ward and June Park. Selectable questions and prewritten responses; no free-text or runtime-AI requirement.
- Twelve shared turns initially. New questions, follow-ups and confrontation branches cost one, including unsuccessful new confrontations. Switching, review, unchanged response replay and hints are free. Show remaining turns.
- Six collectible cards: two initial supporting items, then four discoveries including all three proof items. Automatic collection; contextual testimony does not create extra cards.
- Hide locked questions. Replaying an answered question shows its saved historical answer, even after a lie has been exposed. A newly eligible confrontation branch is a new charged exchange; old testimony remains free to review.
- Free requested hints follow the approved milestone table, not a click/turn counter. At zero turns, hints guide review rather than unavailable questioning. Do not automatically reveal the culprit or proof set through hint or visual metadata.
- At zero turns, block new exchanges but retain evidence/transcript review, hints and accusation. Do not force an immediate verdict.
- Accuse at any time with one culprit and zero to three distinct collected cards. Review the selection and end-of-attempt warning before confirmation; cancellation preserves progress. Outcomes distinguish wrong culprit, correct culprit/insufficient proof and fully proved.
- Show submitted accusation and outcome without extra solution disclosure. Full explanation appears only through the post-verdict reveal action.
- Retain one active attempt and the latest completed attempt. Completed review includes the read-only full transcript, collected evidence, submitted accusation, verdict and reveal. It cannot change active progress. Confirm restart; replay resets the same mystery, not new content.

Author-only truth notes, required-key markers, hidden prerequisites and locked dialogue must not appear in active player UI. Case-file IDs are implementation references, not a requirement to display technical identifiers. No exploration, audio, uploads, signature capture, extra mechanics or procedural variation is required.

## Capabilities needing a UX destination

The following must be reachable; this list does not imply separate pages, panels or dialogs:

1. Short public introduction; registration and login.
2. Returning-player access to resume, latest completed review and starting/restarting.
3. Briefing, initial evidence and concise rules explaining costs, proof, hints and no countdown.
4. Character selection, available questions, testimony/history, collected evidence, confrontation, remaining turns, hint request and accusation entry.
5. Culprit/evidence selection, fourth-item prevention, submission review and confirmation/cancel.
6. Verdict, deliberate solution reveal, read-only completed material and replay.
7. Restart warning/confirmation/cancel and logout.
8. Loading/pending save, successful save, failure/retry, stale-state refresh, session expiry and form feedback.

Mirror the source protagonist Alex and UJ IDs. Narrative beats are Start (UJ-1), Investigate (UJ-4), Accuse/resolve (UJ-3), Return/replay (UJ-2).

## Protected policies and states

- Sign-up: usernames 3–24 ASCII letters/digits/underscores, surrounding whitespace trimmed and uniqueness/login case-insensitive; passwords 15–128 NFC-normalized Unicode code points, spaces retained. Use the exact approved helper/error copy. Both bounds and input rules must be visibly associated with each labelled field before typing/submission, remain through errors, and not rely on placeholders/hover or a failed submission. No silent truncation.
- Registration signs in. Login failure uses the approved generic credential message. Throttling: five failures per normalized username/IP and twenty per IP in a rolling fifteen-minute window; backend semantics remain as specified in P-1.
- Session expiry: thirty minutes without a user-initiated authenticated request, or eight hours since sign-in. No remember-me option. Logout ends the current browser session; other device sessions have their own expiry. Expiry must preserve saved progress and use the approved message. Reauthentication does not automatically resubmit pending actions.
- Pending mutation: show saving progress and prevent duplicate submission. Failed uncommitted actions cost no turn; uncertain completion is reconciled before retry. Do not promise offline writes or auto-sync absent a source requirement.
- Simultaneous different actions from the same old state: first valid action wins. Reject stale actions free of charge and ask for refresh; do not silently reapply. Same-action retries recover the saved outcome.
- Desktop Chrome/Edge: 1280×800 at 100%, then the same window at 200% browser zoom. Phone: Chrome mobile emulation, 360×800 CSS pixels, portrait, 100%. All core controls reachable; readable text, no overlap/clipping/horizontal page scroll; vertical scrolling allowed. Desktop core actions keyboard-operable, labelled and visibly focused.
- Warm local response target: at least nineteen of twenty samples per group within two seconds for question, confrontation, hint, evidence review, transcript review, resume and confirmed accusation. Include persistence for mutations; exclude fixture preparation, startup/build and first cold load. This is a future acceptance check, not a measured current result.

## Choices to elicit

- Displayed website/game name, desired visual feeling, references and explicit dislikes.
- Light/dark treatment, palette, type, shapes, depth, icon/portrait/illustration use and motion, if any. None selected yet.
- Information hierarchy and simultaneous visibility during questioning; where review and action selection live; which capabilities share a destination. Do not decide containers or page boundaries in this digest.
- How players recognize new versus read-only exchanges, new evidence, pending/saved/error states, zero turns and completed read-only mode.
- Placement/presentation of requested hints, evidence selection, confirmations and recovery feedback, without changing their approved semantics.
- Responsive adaptation and focus/reading order across approved viewport/zoom conditions. No UI system/framework has been selected; architecture still owns technical selection.

## Spine shape learned from the five bundled examples

All three DESIGN examples and both EXPERIENCE examples were read for structure only. Their palettes, fonts, layout patterns, shortcuts, UI kits and product-specific restrictions are not inherited.

- `DESIGN.md`: YAML visual tokens (`colors`, `typography`, `rounded`, `spacing`, `components`) and body sections, in order when present: Brand & Style; Colors; Typography; Layout & Spacing; Elevation & Depth; Shapes; Components; Do’s and Don’ts. Use examples to make rationale and component/state appearance explicit after user choices.
- `EXPERIENCE.md`: Foundation; Information Architecture; Voice and Tone; Component Patterns; State Patterns; Interaction Primitives; Accessibility Floor; Key Flows. Responsive & Platform is relevant here; Inspiration & Anti-patterns earns a place if the user supplies references. Specify destinations, reachability, behaviour/state/failure rules and Alex’s climax beats. Reference DESIGN tokens as `{path.to.token}` rather than duplicate their values.
- Both contracts win over mocks on conflict. Only an explicitly selected UI system may supply inherited defaults. Keep upstream requirements linked and add the concrete UX decisions needed to implement them.
