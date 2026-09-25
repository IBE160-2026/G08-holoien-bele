---
title: "Product Brief: AI Detective Game"
status: draft
created: 2026-09-16
updated: 2026-09-25
---

# AI Detective Game

## Product and audience

A text-based detective game for people who enjoy crime fiction and logical puzzles. Set in a police station, each case takes approximately 15 minutes and involves 3-4 witnesses or suspects. The player starts with a case briefing and known evidence, asks free-text questions, uncovers clues and motives, and confronts inconsistent explanations to identify the culprit.

The intended value is the freedom to formulate questions and solve a mystery through reasoning across evidence and testimony. AI portrays characters with distinct knowledge, secrets, lies and motives. This is a product hypothesis to test with players, not a claim of validated market demand or uniqueness.

## Core experience

1. Read the case briefing and initial evidence.
2. Question witnesses and suspects, switching freely between them and revisiting earlier interviews.
3. Use evidence and new clues to challenge explanations and understand motives. Character responses reflect what has already happened in that player's attempt.
4. Select a culprit and supporting evidence, then receive an explanation of the result.

Questions draw from a limited budget for the case; the question limit and rules for counting questions will be tested. Players may accuse at any time. Once questions run out, further questioning stops, but evidence and conversation history remain available for deliberation. Fifteen minutes is a pacing target, not a countdown.

A submitted accusation ends the attempt. Full victory requires both the correct culprit and sufficient supporting evidence. The result distinguishes identifying the correct culprit with insufficient evidence from fully proving the case. A wrong accusation ends the attempt, preventing players from cycling through suspects. Feedback explains what was correct or missing.

## Scope and development stages

**Initial test version:** One fixed authored mystery to prove the interrogation loop, evidence-dependent explanations, question budget, verdict and saved progress.

**Target delivery:** A new case variation for each attempt, using authored mystery patterns. Characters, motives, evidence and event details vary within coherent case structures. Pattern count and variation rules remain to be planned. The game retains the police-station setting and short interrogation format.

**Optional extension:** Entirely AI-generated plots, explored only if time remains after the main game works and is tested. This is not required for the target delivery.

The design challenge is to combine flexible dialogue with a fair, solvable mystery. The proposed integrity rule is to establish each case's facts before play and preserve them throughout the attempt. Variation must preserve meaningful evidence relationships, not merely change names.

## Accounts and delivery constraints

Players register with a username and password, log in and resume their own saved games. Progress, conversations, discovered clues and character state are isolated per user and attempt. Email verification, social login and email-based password recovery are outside the agreed basic account scope.

**Database purpose:** PostgreSQL stores user accounts and password hashes, login sessions, each attempt's case facts, question budget, conversation history, discovered evidence, character state, accusations and results. These records support resuming an unchanged case and enforcing separate progress for each player. The detailed table structure remains to be designed.

The entire fullstack website must deploy through a single `docker-compose.yml`, including the frontend, backend, PostgreSQL and any required supporting services. The local stack must be self-contained, requiring no separate installation of language runtimes or a database on the host. Docker with Compose and documented configuration are the deployment prerequisites; live AI dialogue additionally requires internet access and an OpenRouter API key.

The same application code and schema must support optional hosted deployment, with Supabase usable as hosted PostgreSQL. Authentication is handled by the application backend using an established framework or library. Separate installations do not automatically share accounts or saves.

Infrastructure and optional hosting must use free services. AI dialogue may incur costs. Public hosting is optional; local execution is sufficient for submission.

## External integrations

**OpenRouter:** The selected API service for witness and suspect dialogue, following the professor's recommendation. The backend calls OpenRouter with relevant character knowledge and conversation context. Prefer a low-cost LLM; the specific model remains undecided and configurable. Keep the API key on the server. See the [OpenRouter quickstart](https://openrouter.ai/docs/quickstart).

**Supabase, optional:** Provides hosted PostgreSQL if the website is published. Local deployment uses the PostgreSQL container; neither deployment requires Supabase Auth. No other external service is currently required by the product scope.

## Success and assessment

The project targets the course's hard difficulty level, building on a playable foundation. The teacher has not classified this specific game. Both code/functionality and the group reflection are due **2026-12-05**. The two-person team targets completion of both around **2026-11-21**, leaving approximately two weeks for final checks, corrections and submission preparation. Weekly capacity remains open.

Proposed validation targets, to make measurable during specification:

- Players can explain their accusation using discovered evidence after a session of roughly 15 minutes.
- Tested case variations have a discoverable solution within the question budget; dialogue preserves character knowledge and case facts.
- Saved attempts resume consistently, and users cannot read or change one another's progress.
- A single `docker-compose.yml` starts the complete website and database from a clean checkout after documented configuration, without separately installed application runtimes or database software.

The portfolio has two components: code/functionality at 70% and group reflection at 30%. There is no oral examination this semester. Document AI-assisted development, student quality assurance, challenges, solutions, and ethical and technological implications. Submission includes source code, the single `docker-compose.yml`, supporting Dockerfile(s) as needed and startup instructions. See `addendum.md` for source details.

## Open decisions

Question limit and counting rules; evidence-presentation interaction and sufficiency rules; case-pattern count and variation checks; framework and authentication library; weekly team capacity. OpenRouter is selected; the low-cost model, credentials, spending budget and API-key handling during assessment remain open. Technical proposals, sources and supporting context are in `addendum.md`.
