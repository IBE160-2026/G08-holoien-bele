# AI Detective Game: supporting context

Updated: 2026-11-08. This addendum supports the current [product brief](brief.md). Current scope decisions below supersede earlier proposals for mandatory AI dialogue and a new case variation per attempt. The working title is retained from the earlier concept. The append-only `.memlog.md` retains decision history.

## Sources and course requirements

The product decisions come from team discussions on 2026-09-16, 2026-09-19, 2026-09-25 and 2026-11-08. The repository README identifies Daniel Holøien and Jakob Saleh Bele as the two-person team in IBE160 Programmering med KI at Høgskolen i Molde, autumn 2026.

The four-page assignment proposal, *Prosjektforslag: Programmering med KI*, permits self-defined projects and invites instructor feedback (p. 1). Difficulty influences assessment, but it supplies no detailed rubric or grade guarantee. Medium examples include a course FAQ chatbot (p. 4); hard examples include project-management simulation (p. 2) and calibrated exam assessment (p. 3). This game is the team's own project. The personal-machine source path has been removed for repository portability.

The examination description supplied by the user specifies groups of 1-4, code/functionality at 70%, and group reflection at 30%. Document AI-assisted development, student quality assurance, challenges, solutions and ethical and technological implications. The user confirms there is no oral examination. Both components are due 2026-12-05.

The teacher's reply supplied on 2026-09-19 requires fullstack development and a database at every difficulty level. Local execution is sufficient; source code and a Docker file are required. Hosting may use free tiers. The user's subsequent requirement is more specific: the entire website must run through one `docker-compose.yml`.

### Product-brief feedback and the team's response

The [teacher's feedback dated 2026-10-06](tilbakemelding-product-brief.md) evaluates the earlier brief and addendum. It recommends a complete fixed case before variants, prewritten dialogue so the examiner can play without an OpenRouter key, testable success criteria and bounded scope. It classifies the earlier AI-heavy concept as difficult and describes the fixed-case foundation as closer to medium difficulty. That is not a new classification or grade guarantee for the revised product.

The team chooses a narrower baseline than merely adding a scripted test mode: selectable questions and prewritten responses are the required game. Free-text AI dialogue and case variations are optional, unlikely additions with no planned implementation allocation. The revised brief includes eight functional acceptance criteria and explicit exclusions. Framework and deployment details remain architecture work.

To address the teacher's request for a clearer player problem, the team positions the game as an approachable introduction for crime-fiction fans, including people new to detective games, who want to try the genre without a lengthy commitment. A short, self-contained investigation may encourage later exploration of longer, more developed games. This is an unvalidated player-need hypothesis, not evidence that existing games lack this experience or that this project is unique or better. It adds no new feature or requirement to track what players play afterwards.

### Vercel publishing announcement

The user supplied a screenshot of the teacher's announcement, "Publisering av nettsiden", published 29 October. It describes Vercel installation across the course GitHub organization, automatic deployments from `main` and separate PR previews. Vercel is the publishing service supported by the course. One group member creates and owns one project for the repository; put its deployment address in the README. Other members can use GitHub deployment status and links.

Supabase and Neon are examples for configuring database environment variables, not mandated providers. The announcement does not explicitly make public hosting a submission requirement. The team nevertheless retains Vercel and Supabase for development and deployment testing alongside required local Compose delivery. Runtime compatibility, quotas and configuration need checking during architecture and setup; no provider capabilities or current free-tier limits are assumed here.

## Agreed gameplay rules

| Area | Required behaviour |
|---|---|
| Audience and device | English-language introduction to detective games for crime-fiction fans, including genre newcomers; desktop/laptop primary, basic phone responsiveness where it adds little development work. |
| Case and cast | One fixed authored police-station murder mystery with exactly three interviewable characters, including the culprit. Serious, easy-to-understand writing without graphic descriptions or imagery. Replay uses the same mystery. |
| Pacing | Approximately 15 minutes; no countdown. |
| Dialogue | Selectable questions and prewritten responses; evidence and attempt state unlock authored follow-ups. |
| Initial budget | 12 turns shared across characters, adjustable after playtesting. |
| Charged actions | Each new question, follow-up or confrontation exchange costs one turn. An irrelevant or unsuccessful new confrontation still costs a turn. |
| Free actions | Switching characters, reviewing evidence, rereading answers, repeating unchanged confrontation responses and requesting hints. |
| Evidence | Automatically collect revealed clues. The initial case target is six collectible items in total, including initial evidence: three key items and three supporting or inconclusive items. |
| Confrontation | Present collected evidence to a character; relevant evidence unlocks appropriate authored testimony and follow-ups. Hide locked questions. Unsuccessful responses give no new information without declaring innocence or irrelevance. |
| Accusation | Available at any time, with a selected culprit and at most three supporting evidence items. Fewer items are allowed. Confirm after reviewing the selection and end-of-attempt warning; cancel preserves the active attempt. |
| Full proof | Correct culprit plus the one authored set of all three key items. Missing or replacing a key item means insufficient proof. |
| Verdict | Wrong culprit; correct culprit with insufficient proof; or fully proved. Distinguish culprit identification from proof without automatically exposing the full solution. |
| Solution | A post-verdict "Reveal solution" button explains the culprit, key evidence and contradictions. |
| Zero turns | Block new questions and confrontation exchanges; keep evidence, transcript, previous responses, hints and accusation available. |
| Hints | Free prewritten non-spoiler guidance based on progress; repeat the same hint until progress changes. Zero-turn hints support reviewing collected material. Exact state conditions/selection remain in the PRD readiness register. |
| Progress | Autosave completed actions; retain one active attempt plus the latest completed attempt. Confirm restart before clearing active progress and restoring the budget. Restart preserves the completed result; a newly completed attempt replaces it. |
| Technical failures | Do not consume turns. Save the answer, clues, state changes and turn deduction together; retries must not charge twice. |

The full [case version 1.0](../../prds/prd-G08-holoien-bele-2026-11-08/case-spec.md), including its hint table and admission-based ending, was approved on 2026-11-08. Its authoring model verifies routes within the 12-turn budget, but actual pacing and usability still require playtesting. Additional proof combinations remain outside required scope. The [PRD readiness register](../../prds/prd-G08-holoien-bele-2026-11-08/prd.md#implementation-readiness) records resolved product decisions; UX, architecture and stories remain separate implementation prerequisites. Do not let an implementing agent invent replacements for the approved content.

## Case content and state integrity

Write the case facts, culprit, evidence relationships, testimony and unlock conditions before play. Store the authored case as version-controlled data. The database records each attempt's case identity/version and progress so reload or resume does not change the mystery. Exact schema and versioning strategy remain architecture decisions.

Code controls available questions, clue collection, disclosure transitions, turn accounting and verdicts. Author concise answers and verify that testimony matches what each character knows or is concealing. Check reachable paths and narrative solvability, not only whether data fields are present.

No case generator, variation validator, live model or prompt-validation pipeline is needed for required delivery. If variants are pursued later, initially limit them to two or three authored patterns with explicit variation rules and solvability checks. Entirely AI-generated plots remain a further extension.

## Data, authentication and environments

Use PostgreSQL locally and Supabase PostgreSQL for hosted development/testing. Store accounts and password hashes, login sessions, attempt ownership, case identity/facts as needed, remaining turns, transcripts, discovered evidence, character state, accusations and results. Determine ownership from the authenticated session and enforce it on reads and writes. Use an established authentication library or framework; Supabase Auth is not part of the agreed design.

Players use usernames and passwords. Email verification, social login and email-based password recovery remain outside scope. The database supports gameplay and resumption, not merely a chat archive. Test login/logout, persistence, cross-user access and clean initialization.

### Local delivery

A single `docker-compose.yml` must start the complete frontend, backend, PostgreSQL and any required supporting services. Logical components need not have separate containers. Include migrations/schema setup and the fixed authored case in the startup flow. Persist database data. The host requires Docker with Compose, not separate Python, Node.js or PostgreSQL installations.

The documented command is `docker compose up --build` after any documented local configuration. Required gameplay needs no OpenRouter key, Supabase account or other paid/external service account. Installing/building dependencies may require network access; there is no requirement for local AI inference.

### Hosted development and testing

Use Vercel for the main-branch deployment and PR previews, with Supabase as hosted PostgreSQL. Preserve the same application code, schema and gameplay across environments. Local and hosted installations have separate accounts and progress; synchronization is outside scope. Choose the framework and backend arrangement to support both Compose and Vercel rather than assume that Compose itself deploys to Vercel.

Keep one backend implementation. Architecture must resolve runtime compatibility, database connections, schema migrations, session settings and how preview/test data is separated from the main deployment. Infrastructure and hosting must use free services. These are planning decisions, not completed integrations.

### Configuration and repository organisation

Provide `.env.example` with placeholders and document local and hosted configuration separately. Ignore local `.env` files; keep credentials and database connection strings out of committed source and browser-delivered configuration. Keep database access in the backend. Put authored case data in a dedicated version-controlled directory; choose its exact path during implementation. Record startup and deployed-site instructions in README.

## Verification and playtesting

Use the brief's eight numbered functional criteria as traceable requirements for PRD, stories and tests. In particular, test all three verdict outcomes, the three-item selection cap, exact turn accounting, failed confrontations, exhausted turns, autosave/resume, ownership isolation and a clean key-free Compose launch. Include technical failure/retry checks for partial saves and duplicate turn charges.

Before human testing, start with 12 AI-agent sessions: six blind investigations with player-visible information only and six directed sessions covering wrong accusations, insufficient proof, exhausted turns, hints, restart and resume. Record instructions, paths, findings and student verification; fix blockers and rerun affected scenarios before human sessions. Further sessions may be needed. Tooling and individual scenario assignments remain open. This is a testing activity; runtime AI remains optional.

After agent testing and corrections, have three people outside the team play without coaching. Record completion time against the approximately 15-minute target, confusing interactions, and whether they understand their verdict and supporting evidence. Do not require all three to win. Use human observations to assess clarity and pacing alongside agent and automated checks.

## Schedule and reflection

Aim for a near-complete product by **2026-11-21**. Use the remaining period for final checks, corrections, reflection and submission preparation, rather than plan to defer core features. Both submission components remain due **2026-12-05**. Weekly hours remain open. The user's expectation that the teacher's parallel app work runs over approximately two weeks is context, not a confirmed revised deadline.

Retain representative AI suggestions, agent playtest reports, student assessments, corrections and test results. Distinguish AI-assisted development/testing from AI dialogue as a product feature. Explain the scope reduction in the reflection and trace teacher feedback through decisions, requirements, implementation and checks. Record observed limitations honestly.

## Optional AI integration and historical references

OpenRouter was selected on 2026-09-25 for the earlier runtime-AI concept. It remains the preferred provider only if that optional addition is pursued. Model, credentials, spending limit and key handling are deferred and do not block delivery. Keep any future key server-side and model identifier configurable. ChatGPT subscriptions are not assumed to fund OpenRouter access. Optional AI use may incur costs; infrastructure must remain free.

If live AI dialogue is added, test hidden-knowledge leakage and contradictions with a fixed question set, and define output validation and failure handling. Those checks are conditional extension work, not required baseline infrastructure.

The following references were gathered for earlier planning and are retained as context, not as current implementation requirements or newly verified provider documentation:

- [Vaudeville developer FAQ](https://store.epicgames.com/p/vaudeville-faq-dd3e5b?lang=en-US): related AI detective-game context; no claim of uniqueness.
- [KNUDGE, EMNLP 2024](https://aclanthology.org/2024.emnlp-main.520/): character/world-grounded dialogue research relevant if runtime AI is revisited.
- [Django authentication](https://docs.djangoproject.com/en/5.2/topics/auth/default/): historical framework candidate, not a stack decision.
- [OpenRouter quickstart](https://openrouter.ai/docs/quickstart): historical integration reference for the optional AI extension.
