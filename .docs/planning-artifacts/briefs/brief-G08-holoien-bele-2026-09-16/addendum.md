# AI Detective Game: supporting context

## Sources and course requirements

The product decisions come from the team's conversation on 2026-09-16 and 2026-09-19. The repository README identifies Daniel Holøien and Jakob Saleh Bele as the team, in IBE160 Programmering med KI at Høgskolen i Molde, autumn 2026.

The assignment proposal, `C:/Users/danhol13/Downloads/Prosjektforslag_ Programmering med KI.pdf`, was inspected across all four pages. It permits self-defined projects and invites instructor feedback (p. 1). Difficulty influences assessment, but the document supplies no detailed rubric or grade guarantee. Its medium examples include a knowledge-grounded course FAQ chatbot (p. 4); hard examples include project-management simulation (p. 2) and consistent, calibrated exam assessment (p. 3). AI Detective Game is the team's own choice, not a proposal listed in that document.

The examination description pasted by the user specifies:

- Groups of 1-4 students and portfolio assessment.
- Code and functionality: 70%, including delivery of an AI-generated application and documentation of AI use and student quality assurance.
- Group reflection: 30%, covering the development process, challenges, solutions, AI's influence on the result, and ethical and technological implications.
- The user confirms that this semester has only the two components above; the oral examination has been removed. There is no third assessment component to plan for.
- Both components are due 2026-12-05. Target completion of the application, quality-assurance documentation and group reflection around 2026-11-21, reserving approximately two weeks for final checks, corrections and submission preparation.

The teacher's reply, pasted on 2026-09-19, requires fullstack development and a database at every difficulty level. Local execution is sufficient; source code and a Docker file are required. Hosting is optional and may use free tiers. No mandatory public availability period was given. Guidance on importing API keys will follow. The reply does not mandate Python, TypeScript or Supabase, or classify this specific game as hard.

## Gameplay details for specification

Confirmed: approximately 15 minutes, 3-4 interviewees, known initial evidence, free choice of interview order and revisits, limited questioning, voluntary early accusation and continued access to evidence/history after questions run out. An accusation ends the attempt. Full victory requires the correct culprit and sufficient supporting evidence; feedback distinguishes a correct identification from a proven case.

The following are design proposals, not accepted numerical or interaction requirements:

- Start playtesting with 12-16 successfully answered interrogation turns shared across the case. Reviewing material and switching people are free; asking a question or confronting someone with evidence consumes a turn.
- Show remaining turns and preserve them across save/resume. Technical failures and retries should not consume extra turns.
- Establish a clear main-question-per-turn rule so multi-question messages cannot bypass the budget. Accept reasonable alternative phrasings; success should not depend on guessing exact words.
- Keep answers concise enough to leave time for reading and deduction. Test the question budget before adding further trust, stress or anger mechanics.

The exact evidence-presentation interaction, sufficiency rules and rules for counting questions remain open. A new attempt receives a new case variation; unlimited uniqueness across all attempts is not promised.

## Case variation and integrity

First test one fixed mystery. For example: record an initial alibi, present conflicting evidence, update what the character is permitted to disclose, generate an appropriate response, and verify that the changed state survives save/resume. This demonstrates the intended mechanics; it does not prove that all future case variations are solvable.

The required target uses authored case patterns with variations in characters, motives, evidence and event details. Entirely generated plots are a time-permitting extension. Pattern count, variation rules and generator implementation remain open.

Proposed approach: construct structured case facts and a solution before play, validate their relationships, and persist the accepted case. Resume must preserve that case rather than regenerate it. Check playable routes to the solution as well as structural consistency; structural checks alone do not establish narrative solvability. Limit each character's dialogue context to permitted knowledge, disclosures and relevant state. Code should control disclosure transitions and verdict rules. Model output still needs validation and defined behavior when a response fails checks.

## Technical and operational proposals

### Data and authentication

Use the selected PostgreSQL database for accounts, login sessions, attempts, dialogue, clues, character state and accusations. Relate evidence to claims and attempts so the database supports gameplay rather than merely archiving chat. Version-controlled case definitions may supply initial data; the storage structure is not yet selected.

Use an established backend framework or authentication library for password hashing and session management. Determine ownership from the authenticated session. Keep database access and any AI credentials in the backend; account and game data must not become publicly readable through optional provider APIs. Test cross-user access, logout, persistence and a clean setup. Django's built-in authentication is one possible option if Python is selected, not a framework decision.

### Deployment and infrastructure

Required delivery: a single `docker-compose.yml` deploys the complete website, including frontend, backend, PostgreSQL and any required supporting services. These logical components need not each have a separate container. The repository may contain supporting Dockerfile(s), source and configuration templates, but local startup must not require composing multiple deployment files or manually starting separate services.

After obtaining the source and supplying documented configuration, the intended startup is `docker compose up --build`. Package application runtimes and dependencies in containers, persist database data, and include database initialization/schema setup and required initial data in the documented startup flow. The host requires Docker with Compose, not separately installed Python, Node.js or PostgreSQL. External AI access and credentials remain deferred; self-contained application deployment does not imply offline AI inference.

Configure connection details, TLS/pooling where needed, service addresses, session secrets and cookie/host settings per environment. Preserve the same application code and schema for optional hosted deployment. Local and hosted installations have separate data; cross-installation synchronization is outside scope.

Infrastructure and hosting must remain free. Optional hosting must be checked for runtime compatibility, quotas and pause behavior before deployment. As consulted on 2026-09-19, [Supabase pricing](https://supabase.com/pricing) lists free PostgreSQL with 500 MB database storage and pausing after one week of inactivity. No application hosting provider has been selected.

### Deferred AI access

AI dialogue is exempt from the free-infrastructure constraint. Both team members report ChatGPT subscriptions, but ordinary API-key usage is billed separately. Provider, access, spending budget and API-key handoff for assessment are deferred. This does not block product planning. Depending on the eventual model choice, local application execution may still require internet access.

## Validation and reflection material

Retain representative AI suggestions, student assessments, corrections and test results. Distinguish AI-assisted development, which the examination requires documenting, from AI dialogue as a product feature. Evaluate unsupported clues, hidden-knowledge leakage, evidence-triggered explanations, case variation, evidence-based verdicts, rules for counting questions, saved-game consistency and API failures. Record limitations and observed outcomes rather than claiming perfect consistency. These are proposed verification areas, not additional course mandates.

## Research references

- [Vaudeville developer FAQ](https://store.epicgames.com/p/vaudeville-faq-dd3e5b?lang=en-US): a related AI detective game uses a prewritten script to ground responses; this is context, not a claim of uniqueness or a course classification.
- [KNUDGE, EMNLP 2024](https://aclanthology.org/2024.emnlp-main.520/): research on dialogue grounded in character/world information informs the consistency risk, not a reliability guarantee.
- [Django authentication](https://docs.djangoproject.com/en/5.2/topics/auth/default/): a candidate framework's username/password and session facilities.
- [OpenAI authentication guidance](https://learn.chatgpt.com/docs/auth) and [API pricing](https://developers.openai.com/api/docs/pricing): subscription access and usage-based API access are distinct.
