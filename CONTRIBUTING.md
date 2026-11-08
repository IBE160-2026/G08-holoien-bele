# Team workflow

Approved by the user on 2026-11-08: end-to-end task ownership, automatic task-branch checkpoints and pushes, and teammate review before merging. Applies to Daniel, Jakob, Codex and Claude. The [shared work register](.docs/team-work.md) records owners and dependencies. Server-side enforcement must be enabled separately using the [GitHub protection guide](.docs/github-protection.md).

## Start an owned task

1. Read `AGENTS.md` or `CLAUDE.md`, this policy, the shared task and relevant session logs. Verify the current branch, working tree and staged changes.
2. Claim one task in the shared register: one accountable owner, the other person as reviewer, acceptance criteria and dependencies. Each person has at most one active development task. Shared work still has one driver.
3. Fetch `origin` and create a short-lived `codex/<task-id>-<topic>` branch from the latest `origin/main`. Do not develop, test experimental changes or commit session logs directly on `main`.
4. Use a separate clone/worktree per concurrently active task. Do not let two people or writing agents share a working directory. Never discard or include someone else's uncommitted/staged changes to make your task easier.
5. After the first push, open a draft PR to `main` so the teammate can see the scope and progress. If tools cannot open it, provide the branch comparison link and record that PR creation remains pending.

Example from a clean checkout:

```sh
git fetch origin
git switch --no-track -c codex/a01-account-entry origin/main
```

No permanent Daniel/Jakob, frontend/backend or develop branches. One task branch and one PR per coherent task; start the next task from updated `main` after its dependencies merge.

## Commit and push during work

- Commit each coherent, reviewable checkpoint: one behaviour change with its relevant tests/docs, rather than one commit per file or a whole day's unrelated work. Use messages such as `feat(accounts): add registration`, `fix(game): prevent duplicate turn charges`, or `docs(ux): define investigation flow`.
- Aim to commit and push within each 30-60 minutes of active work, and always before a break, task switch, handoff or session end. This is a working habit, not an unattended timer.
- A working checkpoint passes the checks relevant to that increment; record what ran and what remains untested. A commit's existence alone does not mean it is known-good.
- If unfinished work must be saved, make an explicit `wip(<area>): <remaining work>` checkpoint on the task branch, push it and keep the PR draft. Record failing/not-run checks and the next step. Never label broken work as passing or merge it for backup.
- Inspect the diff, stage explicit task paths and check the staged diff before committing. Do not use blanket staging that captures unrelated changes. Do not commit credentials, local environment files or generated caches.
- Push with `git push -u origin <task-branch>` the first time; subsequent pushes target that same branch. A failed push is not a successful backup: retry an ordinary transient failure, then report the cause and preserved local commit if blocked. Do not silently end with unpublished work.

### Standing authorization for agents

When performing a user-approved task, agents are authorized to create its task branch, make focused local commits, push checkpoints/WIP/session logs to that task branch, and open/update its draft PR without repeatedly asking. This includes the session-end checkpoint. The user approved this authorization explicitly; it satisfies logging skills' condition that pushes require a user request.

This does **not** authorize direct pushes to `main`, merging PRs, approving on a teammate's behalf, force-pushing published history, deleting another person's branch, or changing GitHub settings. A specific user instruction is required for such an exception; record its purpose and resulting checks. Normal work follows the PR path.

## Keep branches current without overwriting work

Fetch before starting and before requesting final review. Merge `origin/main` into the task branch when needed, resolve conflicts there and rerun affected checks. Avoid rebasing published branches and avoid force pushes. A non-fast-forward push means inspect remote changes; do not overwrite them.

Branches reduce overlap but do not eliminate conflicts. Agree interfaces before parallel work, and coordinate changes to shared files as described in the work register. If two tasks need the same contract/schema edit, split out a prerequisite PR or agree which owner makes it.

## Review and merge

A PR is ready only when its owner has:

- completed the task's acceptance criteria and linked the task/FR IDs;
- run relevant available checks and recorded commands/results and any limitations;
- added/updated meaningful tests for new application behaviour;
- checked the Vercel preview for UI/deployment changes, or recorded a reason it is not applicable;
- synchronized with `main`, resolved conflicts and updated docs/session logs.

The other human teammate reviews the diff and test evidence, tries the important flow, and approves. An AI review helps but does not substitute for that approval. New changes invalidate the approval; request another review. Resolve all review conversations before merge.

Use GitHub's **Create a merge commit** so meaningful checkpoint commits and contribution history remain available. Only merge an approved, passing PR; do not use `main` to find out whether the feature works. Post-merge verification can confirm integration. After merging, remove the finished branch and update local `main` with a fast-forward pull.

Current automated application CI does not exist. Until the foundation task adds it, PRs must show relevant local checks, including the existing case verifier when applicable. Before application features merge, create meaningful build/test/Compose checks and require their actual observed job names in GitHub. Passing the authoring-model verifier alone never proves the application works.

## Recover known-good versions

Treat reviewed, verified `main` merge commits as recovery points. For a demonstrated working milestone, record its commit, checks, environment and limits in the task/PR and create an annotated `milestone/<name>` tag when the team approves it. Do not label today's planning-only repository as a working game.

To inspect a prior version, create a separate recovery branch/worktree from its known-good SHA/tag. To undo a regression, propose a revert/fix PR from current `main`; do not reset shared `main`, move published milestone tags or force-push history. This preserves later work and the reason for recovery.

## End the session

1. Save a coherent or clearly marked WIP checkpoint and push the task branch.
2. Update the shared task status, PR, checks, blockers and next action. Joint Discord work records participants, driver and decisions; never invent contribution times or identities.
3. Use `sesjonslogg`: update the relevant per-user log and `issues.md`. Commit **only** those log files in a separate `Logg: ...` commit on the task branch, then push it too. Do not include application files in the logging commit.
4. Report the branch, last pushed commit, PR/link, tests and any actual blocker. A clean tree is preferred; if someone else's changes must remain, identify them without committing them.

The shared task register is the team assignment/status source. Per-user `issues.md` files remain personal reminders and should link the shared task instead of creating competing ownership decisions.
