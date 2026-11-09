# Shared team work and ownership

Initial allocation approved by the user on 2026-11-08. This is a capability-level plan, not a substitute for the approved PRD, UX, architecture or implementation stories. Update task/branch/PR/status here as work starts and finishes; do not infer that an assignment makes a blocked task ready.

## People and working agreement

- **Daniel Holøien:** accounts, sessions, saved progress and latest-completed-attempt review, including their UI, backend and tests.
- **Jakob Saleh Bele:** interrogation, turn accounting, evidence, hints and verdicts, including their UI, backend and tests.
- The other person is the suggested review buddy; a second-person approval is optional and does not block a ready merge. Each person owns one development task at a time. Implement a small complete feature slice, not a private layer the other person cannot understand.
- UX, architecture, API/data contracts, integration and reflection are joint decisions with a named driver. The driver maintains the artifact; both agree on decisions affecting both feature areas.

The user reports that brief/PRD decisions were discussed together through Discord screenshare. Record them as joint decision work; exact meeting dates/durations were not supplied. For future pair sessions, log participants, driver, decisions and each person's contribution. Git authorship remains the actual committer; add co-author trailers only with confirmed identities. Do not manufacture equal hours or commit authors.

## Task register

Statuses: `ready`, `needs-input`, `blocked`, `in-progress`, `review`, `done`. `done` requires a merged PR and accepted evidence, not merely a pushed branch. Named allocation is approved; story boundaries and implementation file paths will be finalized after UX/architecture.

| ID | Deliverable / boundary | Owner / driver | Optional review buddy | Status and dependency |
|---|---|---|---|---|
| C01 | Collaboration policy, agent routing, PR template and protection setup guide | Daniel | Jakob | done on landing — [PR #1](https://github.com/IBE160-2026/G08-holoien-bele/pull/1); user-directed merge after local checks, with optional second-person review |
| C02 | Enable and verify GitHub protection for `main` using the guide; coordinate with repository admin/teacher if permissions require it | Daniel | Jakob | blocked — C01 merge/admin access; settings not changed by C01 |
| H01 | Provision free hosting/database accounts and record deployment prerequisites; keep architecture/schema work in R01/F01 | Daniel | Jakob | in-progress — repository setup handoff approved for merge by Daniel; local Supabase connection/TLS and shared skills verified. Jakob account/invitation and Vercel signup appeal/import remain pending. Handoff: [PR #2](https://github.com/IBE160-2026/G08-holoien-bele/pull/2), branch `codex/h01-hosting-setup`; [setup record](hosting-setup.md) |
| U01 | Complete DESIGN.md/EXPERIENCE.md and relevant screen references; jointly decide name, visual direction and interview information hierarchy | Daniel (joint decisions) | Jakob | needs-input — current UX files are draft frontmatter only |
| R01 | Architecture and shared contracts: framework/auth, data model, engine/progress interface, migrations, sessions, atomicity/idempotency, Vercel/Supabase and preview data | Jakob (joint decisions) | Daniel | blocked — agreed UX inputs; decide before dependent coding |
| S01 | Break approved PRD/UX/architecture into small ready stories with FR/NFR acceptance criteria and owners | Daniel (joint planning) | Jakob | blocked — U01/R01 |
| F01 | Establish agreed app skeleton, base Compose/migration setup, shared interfaces and meaningful PR CI; include existing case check, then selected framework build/test checks | Jakob | Daniel | blocked — R01/S01; prerequisite for parallel app features |
| A01 | Registration/login/logout, visible sign-up constraints, expiry and throttling: complete UI/backend/tests (FR-1, NFR-7) | Daniel | Jakob | blocked — U01/R01/F01 |
| G01 | Case loader and deterministic engine: questions, unlocks, evidence, turns, hints and verdict rules with tests (FR-5–FR-10, FR-12, FR-15, NFR-4) | Jakob | Daniel | blocked — R01/F01; approved case v1.0 already available |
| A02 | Owned persistence, autosave/resume, restart confirmation and read-only latest completed review, including UI/backend/tests (FR-2–FR-4) | Daniel | Jakob | blocked — A01 and agreed engine/progress contract; integrate G01 |
| G02 | Investigation/accusation/results experience and deliberate reveal, including UI/backend/tests (FR-5–FR-13/FR-15) | Jakob | Daniel | blocked — U01/G01 and A02 integration interface |
| A03 | Landing, briefing/rules, player navigation and agreed shared presentation components (FR-14 and U01) | Daniel | Jakob | blocked — U01/F01; coordinate shared components before G02 |
| I01 | Integrate slices; verify ownership isolation, duplicate/stale action handling, retained saves, clean key-free Compose startup, hosted preview and README | Daniel (joint execution) | Jakob | blocked — A02/G02/A03; use full FR/NFR checks |
| T01 | Six blind + six directed starting agent sessions, verified fixes/reruns, then three human sessions; evidence and pacing decisions | Jakob (joint execution) | Daniel | blocked — I01; test the other person's area too |
| D01 | Group reflection and evidence trail, citing shared decisions and each person's implementation/review work | Daniel (joint writing) | Jakob | ready — collect evidence continuously; final conclusions depend on T01 |

## Ready-task record

Before moving a story to `in-progress`, record its objective, acceptance/FR IDs, owner, optional review buddy, dependencies, affected area, branch and expected tests. Keep its PR link, actual test results, blocker and next action current. Both can amend allocations by agreement; record the change before simultaneous editing starts.

Until a separate task tracker is adopted, confirm new claims with the teammate on Discord and link the draft PR. An unmerged branch edit is not yet reflected in `main`'s copy of this register; use the draft PR for live progress and coordinate register edits. Do not maintain an independent personal assignment list with different owners.

## Shared-file coordination

- Architecture establishes the engine/progress API and state/error contracts before parallel coding. Do not silently change the other slice's interface.
- Jakob coordinates shared schema/migration ordering, dependency manifests/lockfiles, Compose and CI. Daniel requests needed changes or agrees a bounded edit before touching those hotspots. This is edit coordination, not authority to change product decisions.
- Daniel coordinates the app shell, shared presentation components and UX contracts. Jakob agrees shared-component changes before editing those hotspots.
- Case facts/dialogue/hints are frozen in approved version 1.0. A case change requires a recorded content decision and revalidation, not a developer's convenience fix.
- This register has one task driver at a time; avoid concurrent branch edits to the same rows. PR descriptions can carry progress details until the next coordinated register update.

## Review, milestones and dates

Follow [CONTRIBUTING.md](../CONTRIBUTING.md). The owner self-reviews the final PR state and verifies acceptance evidence. Ask the review buddy for another perspective when useful, especially for shared or risky changes; do not wait for mandatory approval. Pairing/review contributions are recorded honestly. Do not use another account or pretend that an agent review is someone else's sign-off.

Target a near-complete product by **2026-11-21**; code/functionality and reflection are due **2026-12-05**. Weekly hours remain intentionally open, so this register does not invent person-day estimates. If capacity threatens the target, jointly reduce unapproved work rather than silently drop required features. Every feature owner supplies test evidence; integration is continuous, not a final-week handoff.
