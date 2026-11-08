# PRD supporting context

Updated: 2026-11-08. The [PRD](prd.md) builds on the [brief](../../briefs/brief-G08-holoien-bele-2026-09-16/brief.md) and [brief addendum](../../briefs/brief-G08-holoien-bele-2026-09-16/addendum.md). Source history and teacher evidence remain there; PRD decisions confirmed later in the conversation refine the baseline as described below. The append-only `.memlog.md` holds decision history.

## Confirmed refinements to the brief

- **Entry and tone:** short landing-page introduction, registration/login, then case briefing and concise rules. The mystery concerns murder, takes a serious tone and avoids graphic descriptions/imagery; its writing remains easy to understand.
- **Hints:** an included button that players can choose to use, rather than a deferred extension. Guidance is free, prewritten and progress-based, without revealing the culprit or proof set. Repeat clicks show the same hint until progress changes. At zero turns, hints support reviewing collected material.
- **Repeat exchanges:** a repeated unchanged confrontation response is free review. Later discoveries can enable a genuinely new charged exchange. Locked questions stay hidden. Unsuccessful confrontations spend one turn but provide no new information and do not declare innocence or irrelevance.
- **Confirmations and results:** accusation confirmation shows selected culprit/evidence and warns that the attempt ends. Restart confirmation warns of lost active progress. Cancelling preserves state. Retain both one active attempt and the latest completed attempt, with no full history. Completion replaces the previous retained completed attempt; restart does not.
- **Verdict disclosure:** before reveal, show outcome and submitted accusation, without additional culprit/key-evidence disclosure beyond what the outcome itself establishes. The existing post-verdict reveal button remains the route to the full solution.
- **Usability:** desktop Chrome/Edge, basic phone layout, keyboard operation, labelled controls, visible focus and readable enlarged text. Record test versions/settings rather than claim an exhaustive browser/accessibility certification.
- **Responsiveness and errors:** ordinary local gameplay actions normally complete within two seconds after startup. Show pending progress, prevent duplicate submissions and support clear failure feedback/safe retry without losing saved progress or charging twice. Record measured actions and the reference setup.
- **Agent validation:** start with six blind investigations and six directed sessions, then student verification, blocker fixes and affected-scenario reruns before three external human playtests. Further sessions remain possible.

These are user-approved PRD refinements. The source brief and its gameplay table were explicitly synchronized with confirmed decisions on 2026-11-08 after a stricter implementation-readiness audit; earlier states remain in Git and decision history. Its original one-active-attempt rule did not prohibit retaining the latest completed one, and its turn rule is clarified by distinguishing new exchanges from free review. No runtime AI or generator is needed for hints or tests of game rules.

The user approved the complete case, including its admission-based ending, on 2026-11-08. Case version 1.0 and the PRD are final; D-1 through D-6 are resolved. Account/session and acceptance policies P-1/P-2/P-3 and visible sign-up limits are also approved. Earlier reconciliation/rubric reports describe the checks made at their respective stages; final product/content approval does not substitute for the UX and architecture work still required before implementation.

Completed-attempt review includes the full read-only transcript, collected evidence, submitted accusation and verdict with the existing reveal button. It cannot change the active investigation. Hint changes follow explicitly authored discovery milestones, not turn spending alone, with a separate zero-turn review mode; the approved case enumerates exact hint selection priorities and fallback conditions.

## Architecture handoff

Carry forward PostgreSQL in local Compose and Supabase for hosted development/testing, one backend implementation, established application-managed authentication, and Vercel main-branch/PR deployments. Select framework and runtime arrangement during architecture. Local play must remain independent of hosted services and credentials. Preview data separation, schema migrations, connection handling, case versioning, cookie/session configuration and environment settings belong to architecture.

The backend remains authoritative for attempt ownership, available exchanges, state changes and verdicts. Atomic persistence and duplicate-action protection must cover uncertain network responses as well as ordinary retries. An already committed action should be recovered rather than performed again; a failed uncommitted action does not spend a turn. For different concurrent actions based on the same attempt state, only the first valid saved action applies. Reject other stale actions without changes or turn charges and ask the player to refresh; do not silently replay them against the newer state. Include accusation/restart conflicts and distinguish different stale actions from retries of the same saved action. Architecture chooses the enforcement mechanism while preserving this approved behaviour. Retain database storage so accounts and saved attempts survive normal local Compose shutdown/restart and container recreation; test this separately from browser reload/login persistence.

Provide `.env.example` with placeholders, ignore local `.env`, keep credentials/database connection strings out of committed source and browser configuration, and put authored case data in a dedicated version-controlled directory. README must explain the clean Compose startup, initialization/configuration, and the hosted deployment link/setup. Include source, Compose and supporting Dockerfiles as needed for submission. Do not create a second backend or require Supabase Auth.

## Case-authoring handoff

The approved split is two supporting items in the briefing and four discovered items, including all three required proof items. The approved roles are business partner, accountant and building caretaker; the victim is a small-company owner murdered before a financial review. The complete [case specification](case-spec.md) and [exact data](case-data.json), version 1.0, are approved in full: names, culprit, fixed facts, timeline, all question/confrontation branches, effects and ordered hint selection. This closes D-1/D-2.

The [case validation report](case-validation.md), generated by `python verify_case_spec.py`, records 14 reachable plot states, 149 state/budget hint checks, a four-turn shortest route and a nine-turn example route. It also checks replay/changed-response and zero-budget behaviour in the authoring model. These are not application or human/agent playtest results. The admission-based finale and short expert route are approved creative choices; playtesting can propose revisions, not silently authorize them.

Prewrite hint selection by progress rather than introducing model calls. Author zero-turn guidance that is useful without inventing uncollected evidence or recommending blocked actions. The number of hint entries is a content-authoring consequence of the state graph, not an extra click quota or escalation mechanic.

## Approved account, session and acceptance policies

The user approved P-1/P-2/P-3 on 2026-11-08. These tables are binding refinements of FR-1 and NFR-5/NFR-6, including the added visible sign-up guidance. They do not select an authentication framework or deployment arrangement; architecture must document how the chosen facilities enforce them.

### P-1 — Accounts and credentials

| Area | Approved behaviour |
|---|---|
| Username | Trim leading/trailing whitespace; require 3-24 ASCII letters, digits or underscores. Preserve the trimmed display case, but compare lowercase for uniqueness and login. `Alex` and `alex` are the same account name. Embedded spaces are invalid. |
| Password | Require 15-128 Unicode code points after NFC normalization; allow spaces and do not trim them. Verify the whole normalized password without truncation. No forced uppercase/digit/symbol mixture or scheduled password expiry. |
| Common passwords | Reject common passwords using a bundled offline validator/list. Architecture must identify and version the chosen facility before account stories; no external account or runtime service is required. |
| Registration | Username/password only; successful registration signs the player in. Existing username produces a clear registration error. No new guest, email, social-login or recovery flow is added. |
| Visible username help | Before input/submission, show `3-24 characters. Use letters (A-Z or a-z), numbers (0-9) or underscores (_). Usernames are not case-sensitive.` beside/below the labelled username field. Keep it visible while typing and after errors. |
| Visible password help | Before input/submission, show `15-128 characters. Spaces are allowed. No required mix of capitals, numbers or symbols. Common passwords are not accepted.` beside/below the labelled password field. Keep it visible while typing and after errors. |
| Form feedback | Requirements must not depend on placeholders, hover, a tooltip or a failed submission to become visible. Client/server rules agree, and field errors are associated with their controls. Use `Username must be 3-24 characters using only letters, numbers or underscores.`, `Password must be between 15 and 128 characters.`, `That username is already taken.` or `Choose a less common password.` as applicable. Do not silently truncate overlong input or trim passwords. |
| Invalid login | Use the same `Invalid username or password.` message for an unknown username or wrong password. |
| Login throttling | After 5 failed attempts for the same normalized username/IP pair in a rolling 15-minute window, reject further attempts for that pair until the count drops below 5. Also limit each IP to 20 failures per rolling 15 minutes. Blocked attempts do not extend the window; successful login clears the pair counter, not the aggregate IP failure record. Return a generic retry-later message. Architecture must document trusted client-IP handling and shared enforcement across instances. |

The password-length, Unicode and common-password policy is informed by [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html). The 128-character maximum and the rate-limit numbers are approved product settings, not claims that NIST prescribes them or that this project is certified compliant.

### P-2 — Sessions and expiry

| Area | Approved behaviour |
|---|---|
| Limits | Server-enforced expiry after 30 minutes without a user-initiated authenticated request, or 8 hours after sign-in, whichever occurs first. Background polling must not extend inactivity. Requests from deliberately reviewing/hinting/playing count as activity when they reach the server; scrolling alone does not. |
| Browser and devices | No remember-me option. A persistent session cookie can survive browser closure within those limits. Multiple device sessions are allowed; the existing first-valid-action policy protects the shared attempt. |
| Logout | End the current browser session on the server and clear its cookie. Other device sessions remain subject to their own expiry. No log-out-all-devices feature is added. |
| Expired requests | Reject new authenticated game actions before mutating progress or spending a turn. Show `Your session has expired. Sign in to continue. Your saved progress is safe.` |
| After signing in again | Restore the current saved state; do not automatically resubmit a previously pending accusation, restart or question. Reconcile any earlier uncertain completed action using NFR-1. Expiry/logout do not delete the account, active attempt or latest completed result. |

Idle/absolute expiry and server enforcement follow the approach described by the [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html). The specific limits above are approved settings for this short-session game.

### P-3 — Concrete usability and response checks

| Area | Approved acceptance setup |
|---|---|
| Desktop | Chrome and Edge, 1280 x 800 viewport at 100% zoom, then the same browser window at 200% browser zoom. Record versions. All core actions remain keyboard-operable with labelled controls and visible focus. |
| Phone | Chrome mobile emulation at 360 x 800 CSS pixels, portrait, 100% zoom. All core actions remain reachable; vertical scrolling is allowed. No overlapping/clipped controls, unreadable text or horizontal page scrolling at these settings. No separate native or phone-only feature is added. |
| Timing | In a warm, ready local Compose setup with one active test player, collect 20 samples for each of seven action groups: new question, new confrontation, hint, evidence review, transcript review, resume and confirmed accusation. At least 19 of 20 in each group should finish within two seconds. |
| Measurement | Measure from user action to usable final UI; for state-changing actions include confirmed persistence. Prepare/reset fixtures outside the measured interval. Count failures as misses, not discarded samples. Exclude Compose build/startup and initial cold load. Record machine/OS, Docker allocation, browser and fixtures. Report misses for correction or an explicit team exception; this is not a hosted-service SLA or an all-hardware guarantee. |

## Test and assessment handoff

Use the PRD FR/NFR IDs as stable references in stories and evidence. The brief's eight criteria are preserved across ownership, accounting/retry, zero-turn review, unlocks, resume, verdicts, deliberate reveal and clean key-free startup checks. Add tests for later refinements such as confirmations, free repeats, hints and retained results.

For blind agent sessions, give only player-visible information and avoid solution contamination across runs. Directed checks may use the known case specification. Record browser versions, viewport/zoom settings and timing setup. Students verify agent findings; human sessions assess readability, pacing and verdict understanding rather than guarantee a win rate. No actual agent or human playtests have been run as part of writing this PRD.

Keep AI-assisted development/testing evidence separate from optional runtime AI. The 2026-11-21 near-complete-product target and 2026-12-05 submission remain unchanged; weekly capacity is deliberately open. Optional model/provider costs are deferred until an AI extension is explicitly pursued.
