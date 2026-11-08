# Detective game UX design

## 2026-11-08 kl. 22:12 — NorskNoobing

### Task

After approving the complete case including its admission-based ending, the user requests UX design with questions about remaining choices. Capture the visual and interaction contract so the implementing agent does not invent it.

### Plan

- Use the approved [PRD](../../.docs/planning-artifacts/prds/prd-G08-holoien-bele-2026-11-08/prd.md), its addendum and case version 1.0 as inherited behaviour, not open product decisions.
- Follow the bmad-ux workflow to capture preferences, then produce separate visual and experience contracts. Ask about unknowns rather than select a palette, layout or UI kit without input.
- Keep [DESIGN.md](../../.docs/planning-artifacts/ux-designs/ux-G08-holoien-bele-2026-11-08/DESIGN.md) and [EXPERIENCE.md](../../.docs/planning-artifacts/ux-designs/ux-G08-holoien-bele-2026-11-08/EXPERIENCE.md) in the new UX workspace with workflow decision history.

### Results

- Created the UX workspace, `.working/` and `imports/`, draft frontmatter-only DESIGN.md/EXPERIENCE.md and a workflow memlog. There is no completed UX contract or screen mock yet.
- Extracted approved UX-facing requirements to [source-context.md](../../.docs/planning-artifacts/ux-designs/ux-G08-holoien-bele-2026-11-08/source-context.md). Covered required capabilities/states, numerical policies, visible sign-up help, viewport/timing conditions, confirmations, read-only history, hints and spoiler protections.
- Read all five bundled design/experience examples for spine shape only. No example palette, typography, layout or kit was adopted. Public product name, visual mood/references and interview information hierarchy remain unchosen.
- Updated the PRD handoff with links to the draft UX contracts and an explicit warning that frontmatter scaffolds are not implementation-ready designs.
- Confirmed the user has already approved serious/easy-to-understand non-graphic writing, desktop-first/basic-phone support and all game rules. UX will inherit them rather than reopen scope.
- No new visual/interaction choice, runtime implementation or browser/UI test was made in this task. Source links and draft status are checked before the local log-only commit.

### Open items

- Ask the user for visual feeling/references or dislikes, the interview screen's information priorities and displayed game name; then capture further layout/navigation/component/state/responsive/accessibility choices. Tracked in [issues.md](issues.md).
- Complete the two UX spines, visual references/mocks as useful, and the workflow's review/coverage decisions before finalizing UX. Architecture and implementation stories follow; no UI-system choice is implied by the current sources.
