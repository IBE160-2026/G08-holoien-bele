# Project instructions

## Collaboration, commits and pushes

Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [shared work register](.docs/team-work.md)
before changing the repository. Claim an owned task and work on its `codex/` branch,
not `main`. Respect the other person's scope, existing changes and shared-file owners.

The user explicitly authorized automatic focused commits and pushes to the current
task branch at stable checkpoints and before breaks, handoffs or session end.
Save incomplete work as a clearly labelled WIP checkpoint on a draft PR branch.
Do not repeatedly ask to publish those checkpoints. This standing authorization
also covers log-only commits; it overrides the logging skill's default of waiting
for a separate push request. Never treat it as permission to push directly to
`main`, autonomously merge a PR, fabricate an approval, force-push, or change GitHub settings.

Open a draft PR after the first branch push. If unavailable tools prevent it,
provide the comparison link and record the pending step. A second-person review
is optional. The owner checks the final diff and relevant tests; an agent may
merge only on an explicit user merge request and after the PR readiness checks.
Never invent another person's approval. Record tests honestly; a pushed WIP is a
backup, not evidence that a version works.

## Session logging

Before the final summary of a task or session that changes state, use the
[`sesjonslogg` skill](.agents/skills/sesjonslogg/SKILL.md). It follows the shared
logging instructions in `.claude/skills/sesjonslogg/SKILL.md`: record the task,
plan, results and open items in `.logs/<git-user-slug>/`, maintain that user's
`issues.md`, and commit only the log files in a separate log-only commit on the
task branch. Push that commit under the standing authorization above. Keep
feature/policy commits separate; the logging commit must not capture other edits.

BMAD `.memlog.md` files are workflow decision records; they do not replace the
project session log. When continuing earlier work, read the relevant session
log and the user's `issues.md` before proceeding.

The shared register owns team assignments/status; personal `issues.md` files
link to it. Record both participants in shared Discord decision sessions without
inventing authorship, contribution times or a teammate's approval.
