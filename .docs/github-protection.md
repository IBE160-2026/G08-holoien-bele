# GitHub protection setup

This change supplies a guide only. GitHub protection has **not** been configured or verified by this task. Repository files and agent instructions do not enforce server-side rules on human pushes. C02 in the [shared register](team-work.md) owns setup and verification.

## Administrator setup

In the repository Settings, create an active branch ruleset or protection rule targeting `main`:

- Require pull requests, with **zero required approving reviews**. Leave required approvals, required Code Owner approval and required approval of the latest push disabled. Peer review remains optional.
- Require review conversations to be resolved. Once real CI checks are configured, also require the task branch to be up to date before merging.
- Block branch deletion and force pushes. Apply protections to administrators; do not add routine bypass actors.
- Enable required status checks **only after their real jobs have run**. Select actual check names, not placeholders. Today no application CI exists; F01 must establish it before application features merge. Vercel preview status is not a substitute for tests.
- Keep merge commits enabled and use them under the team policy, preserving meaningful checkpoints and contribution history.

GitHub documents [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and [rule setup](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule). Exact availability depends on repository/account permissions. If the organization controls the rules or denies access, Daniel coordinates with the teacher/admin; do not bypass configured checks or change settings without authorization.

## Verify before relying on protection

Inspect the saved, active settings and target branch. Confirm that PRs are required but no second-person approval is required, and that failed/missing required checks block merge once CI is configured. Do not test by pushing broken code to `main`. Record the rule name, required check names and verification result in C02's PR/task evidence.

Do not claim protection is active solely because this guide was merged. Recheck after rule changes, and do not use an admin bypass for ordinary progress. New checks must be added to required settings as F01 evolves; workflow path filters must not leave a required check permanently pending.

## Access and reviewer identities

Confirm both GitHub handles and repository access before configuring automatic review routing or CODEOWNERS. The project currently records Daniel/Jakob's names; it must not invent Jakob's handle or an email address. Reviewer routing is optional and is not a merge gate.

If GitHub tooling is unavailable, push the task branch and use its comparison page to open a draft PR. Record the limitation; do not replace the PR with a direct push to `main`.
