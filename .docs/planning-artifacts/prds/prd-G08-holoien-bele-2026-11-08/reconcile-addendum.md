# Source reconciliation: brief addendum

- Source: `.docs/planning-artifacts/briefs/brief-G08-holoien-bele-2026-09-16/addendum.md`
- Compared with: `prd.md` and `addendum.md` in this workspace.
- Result: Core requirements and qualitative intent are preserved. One small delivery clarification should be carried forward explicitly.

## Gap

### Local database durability

The source addendum's **Local delivery** section explicitly says, "Persist database data." PRD FR-3 covers reload and later login, and NFR-2 covers initialization and clean Compose launch, but neither explicitly requires database records to survive ordinary local stack stop/start or container recreation with retained storage. The PRD architecture handoff also does not name persistent database storage.

Suggested clarification: add durable local database storage to NFR-2 or the architecture handoff, with a check that existing accounts/attempts survive a normal Compose restart using retained data. Do not imply data survives deliberate volume deletion.

## Preserved source requirements

- One fixed case, three characters, six initial evidence items, one three-item proof set, 12-turn starting budget, no countdown, and a fair solvable route.
- Automatic clues, authored stateful testimony, free review, terminal three-outcome verdicts, deliberate solution reveal, ownership isolation and consistent resume.
- English-language approachable introduction to the genre, desktop-first/basic phone layout, 15-minute hypothesis without uniqueness claims or guaranteed wins.
- Key-free local Compose delivery with initialization/case data, hosted Vercel/Supabase development using the same code/schema, free infrastructure, one backend, application-managed authentication, and no cross-installation synchronization.
- Configuration templates, ignored environment secrets, backend-only database access, version-controlled case data and README delivery instructions.
- Agent-before-human testing, student verification of findings, three external uncoached human sessions, preserved testing/reflection evidence, and unchanged schedule.

## Intentional refinements, not conflicts

Hints, free unchanged confrontation repeats, active plus latest-completed retention, confirmation steps, hidden locked questions, serious non-graphic murder, 12 initial agent sessions and two-second local target are later user-approved decisions. Their precedence is explicit in the PRD and supporting addendum.

Stack/provider implementation choices, historical research and optional AI configuration may remain in the linked source context or architecture handoff. They do not need duplication in the PRD's functional requirements.

## Resolution
The missing local-storage requirement is now explicit in NFR-2 and the PRD addendum: accounts and saved attempts survive normal Compose shutdown/restart or container recreation when database storage is retained. This closes the reported gap.
