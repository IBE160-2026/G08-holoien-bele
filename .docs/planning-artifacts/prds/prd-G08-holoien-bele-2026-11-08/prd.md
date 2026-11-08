---
title: "PRD: AI Detective Game"
status: final
created: 2026-11-08
updated: 2026-11-08
---

# PRD: AI Detective Game

## Purpose and source precedence

This PRD defines the required player experience, observable behaviour and acceptance conditions for UX, architecture and implementation. Sources are the [product brief](../../briefs/brief-G08-holoien-bele-2026-09-16/brief.md) and [brief addendum](../../briefs/brief-G08-holoien-bele-2026-09-16/addendum.md), refined by the user's PRD decisions on 2026-11-08. Later confirmed refinements in this PRD govern hints, repeated confrontations, confirmation steps, completed-attempt retention and validation targets. They do not restore optional AI or case-variation scope. The [PRD addendum](addendum.md) records these refinements and architecture handoffs.

## Vision, player and tone

Provide crime-fiction fans, including newcomers to detective games, with an approachable investigation they can finish in approximately 15 minutes. Players choose questions, expose contradictions and build an evidence-backed accusation. This may encourage exploration of longer detective games; it is a player-need hypothesis, not a validated market gap, uniqueness claim or conversion target.

The required game is one English-language, fixed authored police-station murder mystery with three interviewable characters, including the culprit. Keep the tone serious and the writing/rules easy to understand; avoid graphic descriptions and imagery. Desktop/laptop browsers are primary, with a basic phone layout. Fifteen minutes is a pacing target, not a countdown. Runtime AI is not required.

The approved case is [The Last Invoice, version 1.0](case-spec.md): a small-company owner murdered shortly before a financial review, with the business partner, accountant and building caretaker as the three interviewable roles. The user approved the complete authored case on 2026-11-08, including names, culprit, exact dialogue, graph, hint table and admission-based ending. [case-data.json](case-data.json) is the matching exact data contract.

## Required scope and non-goals

Required: one fixed murder case, three characters, an initial six-item evidence set, selectable authored dialogue, confrontations, turns, verdicts, accounts, saved progress, latest completed-attempt review, rules, hints and the delivery requirements below. A serious tone does not require graphic content.

Outside required scope: runtime AI, free-text questioning, case variations, generated plots, alternative valid proof sets, full attempt history, email verification, social login, email-based recovery, cross-installation save synchronization and phone-specific features. Optional extensions receive no planned development time. Use the same case on replay.

## Player journeys

Alex is an illustrative crime-fiction fan new to detective games, used to describe the agreed flows rather than a research-derived persona.

- **UJ-1 — Start:** Alex sees a short landing-page introduction, registers or logs in, then reads the case briefing, initial evidence and short rules covering turns, evidence and accusations.

- **UJ-4 — Investigate:** Alex switches among three characters, selects available questions, automatically collects revealed clues and presents evidence to challenge testimony. New exchanges consume turns; review and hints are free. At zero turns, Alex reviews existing material and may still accuse, without a forced immediate verdict.

- **UJ-3 — Accuse and resolve:** Alex selects a culprit and up to three collected evidence items, reviews them with a warning that submission ends the attempt, and confirms or cancels. Confirmation produces a terminal verdict. Alex may reveal the full solution or replay the same case.

- **UJ-2 — Return or replay:** Alex returns after an interruption, logs in if necessary and resumes the same saved investigation. The most recently completed attempt is also available for read-only review of its full transcript, collected evidence, submitted accusation and verdict, with the solution-reveal button. Reviewing it does not alter the active attempt. Restarting requires confirmation before active progress and the turn budget reset; the completed attempt remains available.

## Glossary

- **Case:** the fixed authored mystery with three characters, its facts and solution, and an initial target of six evidence items.
- **Attempt:** one account's investigation of the case. One active attempt and the most recently completed attempt are retained. An accusation completes an attempt; an explicit restart resets active progress.
- **Turn:** one of the initial 12 shared opportunities for a new question, follow-up or confrontation exchange.
- **Evidence item:** an automatically collected clue available for review and selection; initial briefing evidence counts toward the six-item target.
- **Key evidence:** the single authored set of three evidence items that, with the correct culprit, proves the case.
- **Confrontation:** presenting a collected evidence item to a character; attempt state determines whether a new exchange is available.
- **Hint:** free, requested, prewritten guidance based on current progress, without revealing the solution.
- **Accusation:** a selected culprit and zero to three distinct collected evidence items submitted for a terminal verdict.
- **Verdict:** wrong culprit, correct culprit with insufficient proof, or fully proved.

## Functional requirements

### Accounts and progress

#### FR-1 — Accounts

Players can register with a username and password, log in and log out using established authentication facilities. Realizes UJ-1 and UJ-2.

Acceptance: a registered player can log in again and resume saved progress; logout ends authenticated access. No email verification, social login or email-based recovery is required.

The approved account/session contract is:

- **Usernames:** trim surrounding whitespace; require 3-24 ASCII letters, digits or underscores. Preserve display case but compare lowercase for uniqueness and login. `Alex` and `alex` identify the same account.
- **Passwords:** 15-128 Unicode code points after NFC normalization; spaces allowed and not trimmed. Validate the whole password without silent truncation. No compulsory capital/digit/symbol mixture or scheduled expiry. Reject common passwords using a bundled offline validator/list selected and versioned in architecture.
- **Sign-up guidance:** before the player types or submits, show the username and password minimum, maximum and allowed-input requirements visibly beside/below their labelled fields. Keep this guidance visible while typing and after errors; do not hide it in placeholder text, tooltips, or a post-submission error alone. Use the exact field-help copy in the [approved policy table](addendum.md#approved-account-session-and-acceptance-policies). Client and server validation must agree on these rules. Associate field errors with their controls.
- **Registration/login:** successful registration signs the player in. Explain an unavailable username during registration; use `Invalid username or password.` for invalid login without revealing which credential failed.
- **Failed-login limits:** at most 5 failures per normalized username/IP pair and 20 per IP in a rolling 15-minute window. Block subsequent attempts until the applicable count falls below the threshold; blocked attempts do not extend it. Successful login clears only the pair counter, not the IP aggregate. See the addendum for shared enforcement requirements.
- **Sessions:** expire server-side after 30 minutes without a user-initiated authenticated request or 8 hours after sign-in, whichever comes first. Background polling does not reset inactivity. No remember-me option; browser closure alone need not end a persistent cookie within these limits. Multiple device sessions are allowed. Logout invalidates only the current browser session on the server and clears its cookie.
- **Expiry and recovery:** reject new unauthenticated game actions without changing progress or spending turns. Show `Your session has expired. Sign in to continue. Your saved progress is safe.` After login, restore saved state without automatically resubmitting a pending accusation, restart or question; reconcile uncertain completed actions through NFR-1. Expiry/logout do not delete saved progress or retained results.

Boundary acceptance: usernames of length 2/25 and passwords of length 14/129 are rejected with an inline explanation of the actual limit; otherwise valid inputs at 3/24 and 15/128 are accepted subject to username uniqueness and common-password rejection. Test the shared normalization/counting rule and verify that overlong input is not silently truncated. The visible field help must state both bounds before any error occurs.

#### FR-2 — Ownership

Players can read and change only their own attempts, transcripts, evidence and results. Realizes UJ-2.

Acceptance: user B cannot read or change user A's active or completed attempt, including by requesting its identifier directly. Denied operations leave A's progress unchanged.

#### FR-3 — Autosave and resume

Completed actions autosave the transcript, collected evidence, remaining turns and character state. Realizes UJ-2 and UJ-4.

Acceptance: reload or later login restores the same attempt and all four state categories; the case is not regenerated and the budget is not reset.

#### FR-4 — Restart, replay and retained results

Allow explicit restart/replay of the same case with reset progress and a fresh budget. Retain one active attempt and the most recently completed attempt, with no full results history. Realizes UJ-2.

Acceptance: restart requires a warning that active progress will be cleared; cancel preserves it. Confirm resets the active investigation to its initial state and 12 turns while retaining the latest completed attempt. Completed-attempt review includes its full transcript, collected evidence, submitted accusation and verdict plus the existing solution-reveal button. This review cannot add exchanges, change its accusation or alter the active attempt. Completing a new attempt replaces the previous completed attempt available for review. Replay provides the same mystery, not new content.

### Investigation

#### FR-5 — Briefing

Provide the authored briefing and initial evidence before investigation. Realizes UJ-1.

Acceptance: a fresh attempt starts with the defined briefing, two supporting evidence items and 12 turns. The three proof items are discovered during investigation, not provided initially. Reviewing briefing/evidence consumes no turn.

#### FR-6 — Authored interviews

Allow questions to any of the three characters, in any order, with state-appropriate prewritten responses. Hide locked questions until unlocked. Realizes UJ-4.

Acceptance: character switching costs no turn; available questions match the attempt's unlock state. Answered questions remain freely readable without generating a new response or spending a turn.

#### FR-7 — Evidence collection

Automatically collect revealed evidence. Author six evidence items in total: two initial supporting items and four discovered items, including all three key items and one further supporting or inconclusive item. Realizes UJ-4.

Acceptance: initial evidence is available immediately, newly revealed evidence appears without a collection click, and rereading does not duplicate items. Collected evidence survives resume.

#### FR-8 — Confrontations and follow-ups

Present collected evidence to characters. Relevant evidence and state unlock authored testimony/follow-ups. Realizes UJ-4.

Acceptance: a new confrontation consumes one turn even when unsuccessful. An unsuccessful response conveys no new information without explicitly declaring evidence irrelevant or a character innocent; the counter shows the spent turn. Repeating an unchanged response is free. A genuinely new exchange unlocked by later discoveries costs one turn.

#### FR-9 — Turn accounting

Start each attempt with 12 turns shared across all characters, adjustable through documented playtesting. Charge one turn per new question, follow-up or confrontation exchange. Realizes UJ-4.

Acceptance: completed new exchanges decrement the counter exactly once. Switching, rereading, repeated unchanged confrontation responses, evidence review and hints cost zero. Remaining turns are visible during investigation. Technical failure/retry behaviour follows NFR-1.

#### FR-10 — Exhausted budget

At zero turns, block new questions and confrontation exchanges without forcing an accusation or ending the attempt. Realizes UJ-4 and UJ-3.

Acceptance: review, previous confrontation responses, hints and accusation remain available. Attempts to obtain a new exchange neither change state nor make the budget negative.

### Accusation and resolution

#### FR-11 — Accusation confirmation

Allow accusation at any time with a culprit and up to three collected evidence items. Realizes UJ-3.

Acceptance: selecting a fourth item is prevented; fewer than three, including no supporting items, can be submitted. Show the selected culprit/evidence and a clear end-of-attempt warning before confirmation. Cancel costs no turn and keeps the investigation active. Confirm ends the attempt; further accusations or investigative exchanges in it are blocked.

#### FR-12 — Verdict

Apply the authored proof rule and show the submitted accusation with its verdict. Realizes UJ-3.

| Submitted accusation | Verdict |
|---|---|
| Wrong culprit, with any permitted evidence selection | Wrong culprit |
| Correct culprit, missing or replacing any key evidence item | Correct culprit with insufficient proof |
| Correct culprit and all three key evidence items | Fully proved |

Acceptance: each row produces exactly its specified outcome. Before solution reveal, do not additionally disclose the actual culprit or identify/explain missing key evidence beyond what the verdict necessarily confirms about the submitted accusation.

#### FR-13 — Solution reveal

Offer a post-verdict "Reveal solution" button explaining the culprit, key evidence and contradictions. Realizes UJ-3.

Acceptance: the full solution is not automatically displayed after any verdict; the button deliberately reveals it for the completed attempt.

### Introduction and assistance

#### FR-14 — Introduction and rules

Provide a short introduction before account entry, then briefing and concise rules before investigation. Realizes UJ-1.

Acceptance: explain charged/free actions, the shared budget, evidence collection, accusation confirmation, proof requirements, optional hints and the absence of a countdown without disclosing the actual solution.

#### FR-15 — Player-requested hints

Offer free prewritten guidance based on current progress. Realizes UJ-4.

Acceptance: requesting a hint consumes no turn and does not require runtime AI. It suggests a useful action without naming the culprit, identifying the required proof set or revealing the solution. Hint-changing progress means an explicitly authored discovery milestone, such as collecting evidence or unlocking testimony; it does not mean every action or turn deduction. Repeat requests return the same hint until a relevant milestone changes, except that reaching zero turns switches to guidance for reviewing collected material rather than unavailable questioning. Spending a turn without a milestone does not otherwise advance the hint. The case specification must define the exact milestone-to-hint selection, priority and fallback conditions before implementation.

## Cross-cutting requirements

- **NFR-1 — Reliable actions:** Save responses, clues, character changes and turn deduction together. Failed, uncommitted actions do not spend turns. Show a clear error and allow safe retry; repeated submissions/retries must not apply an action twice or lose previously saved progress. Show saving progress and prevent duplicate submissions while an action is pending. A timeout with uncertain completion must be reconciled to saved state before charging a retry. For different actions submitted from tabs/devices against the same saved attempt state, save the first valid action; reject later actions based on the outdated state without spending a turn or applying any changes. Tell that player the investigation changed and ask them to refresh before acting again. Apply this rule to questions, confrontations, accusations and restarts; do not silently reapply an outdated action to the updated state. A retry of the same already saved action returns its saved outcome instead of performing it again. Architecture must enforce this policy across concurrent requests, not only by disabling a button in one tab.
- **NFR-2 — Local delivery:** From a clean checkout, `docker compose up --build` starts the full website and PostgreSQL through one `docker-compose.yml` after documented configuration. Include schema setup and case data. Accounts and saved attempts survive normal Compose shutdown/restart or container recreation when database storage is retained. The full core flow needs no external service account, AI key or paid account, and no separately installed application runtime/database. See addendum for configuration/repository obligations.
- **NFR-3 — Hosted development:** Support Vercel main-branch deployments and PR previews using Supabase PostgreSQL. Preserve the same application code, schema and gameplay as local delivery. Infrastructure/hosting use free services. Architecture resolves runtime and environment arrangements; local/hosted accounts and saves need not synchronize.
- **NFR-4 — Case integrity and solvability:** Facts and solution remain fixed throughout an attempt. Code controls unlocks, turn accounting and verdicts. Verify at least one fair route to all three key evidence items within the budget.
- **NFR-5 — Usability:** Test desktop Chrome and Edge at a 1280 x 800 viewport and 100% zoom, then the same browser window at 200% browser zoom. Test Chrome mobile emulation at 360 x 800 CSS pixels, portrait and 100% zoom. All core controls remain reachable and text readable, without overlap, clipping or horizontal page scrolling; vertical scrolling is allowed. All desktop core actions work by keyboard with clear labels and visible focus. Sign-up requirements remain visible and readable at these settings. No phone-only feature is added. Record browser versions and actual settings.
- **NFR-6 — Response target:** In a warm, ready local Compose setup with one test player, measure 20 samples for each action group: new question, new confrontation, hint, evidence review, transcript review, resume and confirmed accusation. The target passes when at least 19 of 20 samples in each group finish within two seconds. Measure user action to usable final UI, including confirmed persistence for state-changing actions. Prepare/reset fixtures outside timing; count failures as misses. Exclude Compose build/startup and initial cold load. Record machine/OS, Docker allocation, browser, fixtures and observations. Misses require correction or an explicit team-approved exception; an agent cannot waive its own misses. This is not a hosted-service SLA or all-hardware guarantee. Pending/error behaviour follows NFR-1.
- **NFR-7 — Account and configuration protection:** Store password hashes using established authentication facilities. Enforce ownership in the backend and keep credentials/database access out of public client configuration. Commit configuration placeholders, not secrets. Detailed controls belong to architecture.

## Success criteria and verification

- **SM-1 — Functional completion:** Verify FR-1 through FR-15 and NFR-1 through NFR-7, including all three verdict outcomes, owner isolation and a complete key-free Compose playthrough. This expands the brief's eight functional criteria into implementable checks.
- **SM-2 — Agent testing:** Start with 12 sessions: six blind investigations using only player-visible information and six directed sessions covering wrong accusations, insufficient proof, exhausted turns, hints, restart and resume. Students verify findings, fix blockers and rerun affected scenarios before human testing. Twelve is a starting plan, not a cap; record instructions, paths, findings and corrections.
- **SM-3 — Human evaluation:** After agent testing/corrections, three people outside the team play without coaching. Record duration against the approximately 15-minute target, confusing interactions and understanding of verdict/evidence. Record observations and resulting decisions rather than invent a pass percentage from three participants.
- **SM-C1 — Counter-metrics:** Do not optimize for every player winning, rapid completion through guessing, hint avoidance or progression to other games. Assess understandable, evidence-based play rather than perfect scores.

Retain AI suggestions, student assessments, test evidence and corrections for the course reflection. The portfolio comprises code/functionality (70%) and group reflection (30%); there is no oral examination. Both are due 2026-12-05. Target a near-complete product by 2026-11-21, followed by final checks, corrections, reflection and submission preparation. Weekly hours remain open.

## Implementation readiness

All six product/content readiness items below are resolved. The user approved the full case on 2026-11-08, closing the final PRD-level content decisions. The PRD and case are final inputs to UX and architecture; implementation still requires the visual/interaction contract, recorded architecture decisions and ready stories. An implementing agent may not silently choose those missing contracts.

| ID | Readiness item and current state | Destination / decision owner |
|---|---|---|
| D-1 | Resolved: full case version 1.0 approved, including fixed facts, six cards, exact dialogue/conditions, culprit and admission-based ending. | [case-spec.md](case-spec.md) and [case-data.json](case-data.json); [case-validation.md](case-validation.md) records authoring-model checks, not application playtests. |
| D-2 | Resolved: explicit discovery milestones, zero-turn mode and the exact ordered hint text/conditions/fallback table approved with case version 1.0. | FR-15 and the approved case hint contract. |
| D-3 | Resolved: full read-only transcript, collected evidence, submitted accusation, verdict and deliberate solution reveal. Reviewing the completed attempt cannot alter the active attempt. | Approved in FR-4 and UJ-2. |
| D-4 | Resolved: first valid action from a saved state is applied; different stale actions are rejected free of charge with a refresh message. Retrying the same saved action recovers its outcome. | Approved in NFR-1; architecture must specify enforcement before state-changing stories. |
| D-5 | Resolved: approved P-1 account/credential rules, visible pre-submit sign-up requirements and P-2 expiry/logout/recovery policy. | FR-1 and approved addendum policies; architecture still selects and documents the enforcing library, offline list and shared mechanisms before account stories. |
| D-6 | Resolved: desktop 1280 x 800, 100%/200% browser zoom, mobile emulation 360 x 800, and 19-of-20 samples per action group within two seconds in the documented warm local setup. | NFR-5/NFR-6 and approved P-3; QA records the concrete reference environment and observations when executing. |

Agents must not invent case facts, hint mechanics, player-visible rules or optional additions to fill these gaps. Proposed choices remain proposals until approved and recorded. Playtest findings may propose changes but do not authorize an agent to change the 12-turn starting budget, six-item evidence target or proof rules on its own. Internal implementation choices are allowed when they preserve the approved behaviour and architecture contracts. Optional extensions require an explicit scope decision; available time alone is not authorization.

## Deferred work and assumptions

Before dependent implementation, produce and approve the UX contracts, architecture decisions and implementation stories. Remaining downstream work has an explicit destination:

- **UX visual and interaction contracts:** team/UX; complete and approve [DESIGN.md](../../ux-designs/ux-G08-holoien-bele-2026-11-08/DESIGN.md) and [EXPERIENCE.md](../../ux-designs/ux-G08-holoien-bele-2026-11-08/EXPERIENCE.md) before dependent UI stories. They are currently draft frontmatter scaffolds, not a completed layout or visual contract.
- **Framework, authentication library, schema and hosted compatibility:** architecture owner/team; resolve during architecture before implementation stories depend on them.
- **Approved case maintenance:** team; implement version 1.0 verbatim. Record and approve any future content/rule revision, update both case representations and rerun model validation before implementation changes. Do not silently invent facts through technical requirements.
- **Agent tools and individual scenario assignments:** team/test planning; resolve before the first agent sessions. Use the agreed six-blind/six-directed starting plan.
- **Concrete test environments for usability and response time:** team/UX/QA; use the approved viewport/zoom settings and sample criteria in NFR-5/NFR-6. Record browser versions, machine/Docker configuration, fixtures and observations when executing; do not substitute looser bounds without a recorded scope decision.
- **Weekly capacity:** team; remains open by explicit choice, revisit if the 2026-11-21 target is threatened.

No unconfirmed product assumptions are used to expand scope. Alex is only an illustrative name; fine visual design, transport choices and provider setup are downstream work, not implicit new requirements.
