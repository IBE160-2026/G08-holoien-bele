# Team workflow and feature ownership

## 2026-11-08 kl. 22:47 — NorskNoobing

### Task

Create a team commit/push, branch and PR policy to preserve recoverable progress and make it visible to everyone. Allocate development work between Daniel and Jakob while recognizing joint brief/PRD decisions through Discord screenshare.

### Plan

- Inspect existing instructions, logs and repository state; ask about ownership model, standing push authorization and scope of GitHub setup.
- Prepare shared policy/task register, root agent routing, PR template and a server-protection guide on a short task branch.
- Validate and push a checkpoint, open a draft PR, then record reviewer/setup tasks and a log-only checkpoint.

### Results

- User chose end-to-end feature ownership, automatic task-branch checkpoint commits/pushes and repository files plus a GitHub protection guide only. User confirmed Daniel owns accounts/sessions/saved progress/completed review; Jakob owns interrogation/turns/evidence/hints/verdicts. Each owns UI/backend/tests, with the other reviewing. UX, architecture, integration and reflection have joint decisions and one driver.
- Created [CONTRIBUTING.md](../../CONTRIBUTING.md), [shared team-work register](../../.docs/team-work.md), [GitHub protection guide](../../.docs/github-protection.md) and a PR template. Checkpoints target 30-60 active minutes and breaks/handoffs/session end; incomplete work is labelled WIP on a draft task branch. Preserve meaningful commit history and explicitly verified recovery markers; never treat all commits as working game versions.
- Updated AGENTS.md and made CLAUDE.md import it. Narrowly updated the Codex logging wrapper so explicit standing task-branch push authorization also covers separate log-only commits. The canonical teacher logging workflow remains unchanged. The standing policy does not authorize main pushes, self-approval, PR merges, force pushes or settings changes.
- Shared register assigns named owners/reviewers/dependencies, coordinates schema/dependency/Compose/CI and shared UI hotspots, and treats confirmed Discord contributions honestly without invented hours or co-author identities. Personal reminders now point to shared tasks instead of competing owner lists.
- Worked on `codex/team-workflow-policy` from origin/main. Pushed `8bc4bac` (policy/ownership) and prepared `e3e7f10` (PR-linked task and rollout clarification) for the final checkpoint push.
- Opened [draft PR #1](https://github.com/IBE160-2026/G08-holoien-bele/pull/1), base main. C01 is in review and awaits Jakob's human review/merge. No merge, direct main push, protection setup or remote task assignment was performed.
- Official skill validator passed in an isolated temporary environment. Local links, whitespace, eight-file change scope and shared instruction routing passed; final checks also cover the PR-linked register, session log and personal reminders. Local main remains at origin/main. Staging/cache files were removed. No app logic changed and no application test/preview/CI result is claimed.
- GitHub CLI is unavailable; the draft PR was created with the existing GitHub credential in memory, without exposing or saving credential values. No automatic reviewer handle was invented.


- Follow-up: the user explicitly requested merging PR #1, then clarified that review by the other person must not be required and asked for GitHub team best practices. No merge action had occurred before that clarification; the interrupted step only inspected PR state.
- Updated the policy to a lightweight GitHub Flow adaptation: branch/checkpoint/PR/checks/merge/cleanup, owner self-review, optional review buddy, and help recommended for authentication/migrations/shared interfaces/deployment uncertainty. Updated CONTRIBUTING, agent routing, README, task register, protection guide and PR template. Agents still need an explicit user merge request; the standing push authorization does not authorize autonomous merges.
- The main-protection guide now calls for PRs with zero required approvals, optional review routing and actual CI gates once created. No GitHub protection settings were changed. Existing tasks retain the approved owner split; review-buddy names are suggestions, not blockers.
- Consulted GitHub's official Flow and branch-protection guidance. The revised Codex skill passed the official validator. Local links, whitespace and absence of the obsolete mandatory-review wording are checked before committing. No application code changed or application test/CI success is claimed.
- Finalization updates PR #1's description, converts it from draft, and performs the explicitly requested head-pinned merge commit after checking actual conflicts/statuses. The linked GitHub PR is the canonical merge outcome/time; no fabricated Jakob approval or direct main push is used. C01's closing register state applies when that PR lands.

### Open items

- No mandatory second-person approval remains. C01 closes when user-requested PR #1 lands; the linked PR records the actual merge result. C02 setup is still separate and pending.
- Daniel coordinates C02: enable/verify main protection using the guide and an admin/teacher if needed. Settings were not configured by this task. Confirm GitHub handles before automatic reviewer routing/CODEOWNERS.
- U01 UX choices remain pending. R01 architecture, S01 stories and F01 app/CI foundations gate application development. Current repository has no application CI; select real job names only after those checks exist/run.
- Follow the [shared register](../../.docs/team-work.md) and [personal reminders](issues.md). The existing target remains a near-complete product by 2026-11-21 and submission on 2026-12-05; weekly hours remain open.
