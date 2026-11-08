---
title: "Product Brief: AI Detective Game"
status: final
created: 2026-09-16
updated: 2026-11-08
---

# AI Detective Game

## Product and audience

A short, English-language detective game for crime-fiction fans, including players new to detective games, who want to try questioning suspects and connecting evidence. Set in a police station, the game presents one fixed authored murder mystery with three interviewable characters, including the culprit. The tone is serious, the writing is easy to understand, and graphic descriptions/imagery are excluded. Players choose questions, expose contradictions and build an evidence-backed accusation.

The target player wants to try a detective experience without committing to a lengthy game. We aim to offer an approachable, self-contained introduction to the genre in approximately 15 minutes, which may encourage players to explore longer, more developed detective games. This is a player-need hypothesis to test; we have not established that existing games fail to meet it, and do not claim uniqueness or superiority.

Desktop and laptop browsers are primary; basic responsive layouts should also make the game usable on phones without substantial additional development work. Fifteen minutes is a pacing target, not a countdown.

## Core experience

1. Read the case briefing and initial evidence.
2. Select questions for any of the three characters, switching freely between them.
3. Collect revealed clues automatically and use evidence to confront explanations and unlock follow-ups.
4. Select a culprit and up to three supporting evidence items, submit an accusation and receive a verdict.

Each attempt starts with 12 shared turns, subject to adjustment after playtesting. A new question, follow-up or confrontation exchange costs one turn, including an unsuccessful confrontation. Switching characters, rereading responses, reviewing evidence, repeating unchanged confrontation responses and requesting hints are free. Locked questions remain hidden. Technical errors do not consume extra turns. At zero turns, new exchanges stop but review, hints and accusation remain available.

Free, prewritten hints guide players without revealing the culprit or required proof set. Repeated requests show the same hint until progress changes; zero-turn hints support reviewing collected material. Exact progress conditions and hint selection belong in the approved case specification.

The initial content target is six collectible evidence items: three key items required to prove the case and three supporting or inconclusive items. Full victory requires the correct culprit and the single authored set of all three key items. Players may accuse at any time, including with fewer items. Submitting ends the attempt with one of three outcomes: wrong culprit, correct culprit with insufficient proof, or fully proved. Feedback distinguishes culprit identification from proof; the full solution remains behind a post-verdict "Reveal solution" button.

## Required scope and optional additions

**Required delivery:** One complete fixed case with selectable questions and prewritten responses, evidence-dependent testimony, the turn budget, evidence-backed verdicts, accounts, saved progress and player-requested hints. The entire core flow requires no AI key or paid account.

**Outside required scope:** AI dialogue, free-text questioning, case variations, entirely AI-generated plots, alternative valid evidence sets, email verification, social login and email-based password recovery. Optional additions are unlikely to be implemented and receive no planned development time. If variations are later pursued, start with two or three authored patterns; generated plots remain a further extension.

AI-assisted development and testing remain part of the project; runtime AI is optional. Case facts and the solution remain fixed throughout each attempt.

## Accounts and delivery

Players register with a username and password and retain one active attempt plus the most recently completed attempt. Completed actions autosave; logging back in or reloading restores progress. Accusations and restarts require confirmation; cancelling preserves progress. Players can explicitly restart or replay the same case with reset progress and a fresh budget. Starting/restarting preserves the latest completed attempt; completing a new attempt replaces it. A replay does not provide a new mystery. Users cannot access one another's attempts.

PostgreSQL stores accounts, login sessions and the state needed to resume and assess attempts. Use an established authentication framework or library. The fullstack website and local PostgreSQL must start through one `docker-compose.yml`, including required initialization and case data, without separately installed application runtimes or database software. Document any configuration; the local game must run without external service credentials.

Retain Vercel with Supabase PostgreSQL for development and deployment testing, including main-branch deployments and PR previews. Keep the same application code and database schema across local and hosted environments; installations need not share accounts or saves. Infrastructure and hosting must use free services. Local Compose delivery remains required independently of hosted availability. Architecture will resolve hosting compatibility and environment configuration.

## Success criteria and playtesting

The functional acceptance criteria are:

1. From a clean checkout, `docker compose up --build` starts the complete game and database after documented local configuration, and the fixed case is playable without an API key or paid account.
2. Players can register and log in; a user cannot read or change another user's attempt.
3. Each completed new question or confrontation consumes exactly one of the initial 12 turns; switching and rereading are free, and technical failures or retries do not charge extra turns.
4. At zero turns, further questioning is blocked while review and accusation remain available.
5. Relevant answers and confrontations automatically collect the intended clues and unlock the intended follow-ups.
6. Reloading or logging back in restores the same transcript, evidence, remaining turns and character state.
7. Accusations accept at most three evidence items, end the attempt and produce the correct one of the three verdict outcomes under the authored proof rule.
8. The full solution is revealed only when requested after the verdict.

Start with 12 AI-agent sessions: six blind investigations and six directed sessions, with findings verified by students and blockers fixed/retested before three external human playtests without coaching. Further sessions may be needed. Record human completion times, confusing interactions and understanding of the verdict; not every player must win. Use results to assess the 15-minute pacing and initial turn budget.

## Schedule and assessment

Target a **near-complete product by 2026-11-21**, with subsequent time for final checks, corrections, reflection and submission preparation rather than a planned delay. Both code/functionality and group reflection are due **2026-12-05**. Weekly team hours remain open.

The portfolio comprises code/functionality (70%) and group reflection (30%); there is no oral examination. See [addendum.md](addendum.md) for assessment obligations, sources and implementation context.

## Remaining planning decisions

The product direction and case version 1.0 are approved. The [PRD readiness register](../../prds/prd-G08-holoien-bele-2026-11-08/prd.md#implementation-readiness) records the resolved product/content decisions and approved case contract. UX design, architecture and implementation stories are still required before coding. Framework/authentication, hosted configuration and test tooling remain downstream work. Weekly capacity remains open. Optional AI decisions are deferred unless that extension is pursued.
