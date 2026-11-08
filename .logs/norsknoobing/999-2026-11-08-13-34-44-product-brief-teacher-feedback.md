# Product brief: teacher feedback

## 2026-11-08 kl. 13:34 — NorskNoobing

Retrospective backfill of this Codex chat, written at the time above (Europe/Oslo). Earlier turn-by-turn timestamps are not reconstructed. Sources are the visible conversation and saved artifacts; this does not backfill unrelated earlier chats.

### Task

Review the teacher's feedback, create an actionable checklist, ask the team about remaining choices and update the brief/addendum with agreed decisions. Clarify player value honestly without claiming a unique or superior game.

### Plan

- Compare the [teacher feedback](../../.docs/planning-artifacts/briefs/brief-G08-holoien-bele-2026-09-16/tilbakemelding-product-brief.md) with the existing brief, addendum and decision history.
- Resolve scope, gameplay, audience, delivery and test criteria interactively, then consolidate the source documents.
- Preserve current decisions in the [brief](../../.docs/planning-artifacts/briefs/brief-G08-holoien-bele-2026-09-16/brief.md), detail in its [addendum](../../.docs/planning-artifacts/briefs/brief-G08-holoien-bele-2026-09-16/addendum.md), and decision history in the workflow memlog.

### Results

- Revised the project to one fixed authored case with three characters, selectable questions and prewritten responses. Runtime AI, generated plots, variations and alternative proof sets are optional additions without planned implementation time.
- Agreed an initial shared 12-turn budget, charged new questions/follow-ups/confrontations, free review, and no extra turn costs from technical errors. Unsuccessful new confrontations cost a turn.
- Automatically collect an initial target of six evidence items; the correct culprit plus one required set of three key items proves the case. An accusation selects at most three items and ends the attempt with one of three verdicts. Full solution disclosure requires an explicit post-verdict reveal.
- Agreed username/password accounts, autosave, per-user ownership and one active attempt. Later PRD work refined this with retention of the latest completed attempt and repeat-exchange rules; see the [PRD log](998-2026-11-08-13-34-44-detective-game-prd.md).
- Kept local fullstack PostgreSQL delivery through one Docker Compose file without external credentials. Retained Vercel/Supabase for development, main-branch deployment and PR previews after the user's teacher-announcement screenshot. The screenshot does not mandate Supabase or hosted submission.
- Positioned the English-language game as an approachable, roughly 15-minute introduction to detective games for crime-fiction fans and newcomers. Desktop/laptop primary; basic phone responsiveness. No established market-gap, uniqueness or superiority claim.
- Added eight functional success criteria and agent-before-human testing. Three external people should play without coaching. Target a near-complete product on 2026-11-21; both submission components remain due 2026-12-05. Weekly hours deliberately remain open.
- Completed structure/prose checks and whitespace checks; removed the personal-machine source path. No actual application or playtests were executed.
- Follow-up creation of the PRD and its consolidation were completed later in this chat. The workflow memlogs already recorded decisions, but project-level session logging was missing until this backfill.

### Open items

- Weekly team capacity remains open; revisit if the 2026-11-21 target is threatened. Tracked in [issues.md](issues.md#open-items).
- Downstream UX, architecture, case authoring, implementation, testing and reflection tasks are consolidated under the [PRD log](998-2026-11-08-13-34-44-detective-game-prd.md) and [issues.md](issues.md#open-items), rather than duplicated here.
