---
name: sesjonslogg
description: Record completed repository work in per-user session logs and maintain open items. Use before the final summary of state-changing tasks, when asked to log or backfill work, and when resuming earlier work. Small read-only answers without follow-up work need no log.
---

# Session logging

Read and follow the [shared session-logging instructions](../../../.claude/skills/sesjonslogg/SKILL.md)
before logging. This Codex entry point uses the same canonical workflow as Claude,
including user identity, descending filenames, same-work continuation, `issues.md`
maintenance and a path-limited commit of log files only. Apply the root project
instructions and [team workflow](../../../CONTRIBUTING.md): the user has granted
standing authorization to push task-branch checkpoints and logs. Keep logging
commits separate from feature commits. This does not authorize main pushes or
autonomous PR merges. A user-requested merge follows the PR readiness policy;
second-person approval is optional.

Resolve repository paths from the Git/worktree root. Keep BMAD decision records
in addition to these session logs. For a retrospective backfill, use the available
chat and artifacts as evidence, mark the entry as retrospective, and use the
actual logging time rather than inventing timestamps for earlier actions.
