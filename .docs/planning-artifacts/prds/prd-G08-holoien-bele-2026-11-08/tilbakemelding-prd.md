# Tilbakemelding på PRD

| | |
|---|---|
| **Gruppe** | G08 – G08-holoien |
| **PRD vurdert** | `.docs/planning-artifacts/prds/prd-G08-holoien-bele-2026-11-08/prd.md` (status `final`, sist endret 2026-11-08, commit 54aa5fd), lest sammen med `addendum.md` |
| **Dato** | 2026-11-12 |
| **Type** | Formativ tilbakemelding, ikke karakter |

## 1. Samlet inntrykk

Dette er en uvanlig presis PRD: kravene har testbare akseptansekriterier med grenseverdier, saken er ferdig forfattet, og valget om å droppe KI i kjøretid fjerner de to største risikoene fra briefen (nøkkel og usikre KI-svar). Risikoen er nå ikke presisjon, men størrelse og tid: dere har lagt inn mye robusthet (kontoregler, samtidighetsvern, to leveringsmiljøer) med under tre uker til måldatoen 2026-11-21, og dokumentet blander krav med prosesshistorikk, slik at det er tungt å hente fra.

## 2. Dette fungerer godt

1. **Testbare krav.** FR-1 gir grenseverdier («usernames of length 2/25 and passwords of length 14/129 are rejected»), og FR-12 har en tabell der hver rad gir nøyaktig ett utfall. Slike krav kan bli testtilfeller nesten direkte.
2. **Ærlig avgrensning.** «Outside required scope: runtime AI, free-text questioning, case variations …» og «a player-need hypothesis, not a validated market gap» viser at dere ikke bygger på påstander dere ikke kan dokumentere. Saksvarianter og KI-kjøretid er tatt ut, slik tilbakemeldingen på briefen anbefalte.
3. **Beslutninger er synlige.** Tabellen D-1–D-6 under «Implementation readiness» viser hva som er avgjort og hvor det er dokumentert. NFR-1 sier hva som skjer når to faner sender ulike handlinger («save the first valid action; reject later actions based on the outdated state»), i stedet for å la en utvikler gjette.

## 3. Oversikt per dimensjon

| Dimensjon | Vurdering | Kort begrunnelse |
|---|---|---|
| Beslutningsklarhet | sterk | Valg er markert som avgjort, med eier og målfil (D-1–D-6). |
| Substans | sterk | Ingen pynt: «Alex» er uttrykkelig «illustrative», og NFR-ene har tall (19 av 20 under to sekunder). |
| Strategisk sammenheng | god | Tydelig tese om en lett tilgjengelig etterforskning, men SM-ene måler byggekvalitet, ikke tesen. |
| Testbarhet | sterk | Akseptansekriterier med grenseverdier; noen FR-er (FR-1, NFR-1) er for store til å kunne testes ett og ett. |
| Scope og avgrensning | god | Utelatelser er eksplisitte, men omfanget er stort for to–tre uker og har ingen prioritering. |
| Brukbarhet for neste fase | god | Glossar, ID-er og krysshenvisninger fungerer, men dokumentet er langt og har motstridende rester. |
| Formtilpasning | god | Passer et lite spill; prosess- og godkjenningstekst hører ikke hjemme i kravdokumentet. |

## 4. Viktigste forbedringer

### 4.1 Omfang og prioritering mot tidsplanen
- **Alvorlighet:** høy
- **Hvor:** NFR-1, NFR-3, FR-1 og «Weekly capacity … remains open»
- **Problem og hvorfor det betyr noe:** PRD-en krever lokal Compose-kjøring og Vercel/Supabase-deploy, delt IP-begrensning på tvers av instanser, tidsavbrudd på sesjoner, fellesliste over vanlige passord, avvisning av utdaterte handlinger ved samtidighet, 12 agentøkter og 3 menneskeøkter. UX, arkitektur og stories er ikke ferdige, og innleveringen er 2026-12-05. Alt står som like påkrevd, så dere vet ikke hva dere kutter først. Tilbakemeldingen på briefen anbefalte å droppe Supabase/hosting til lokal kjøring var ferdig; PRD-en beholder det som NFR-3.
- **Forslag:** Legg et prioritetsmerke på hver FR/NFR: «må», «bør», «kan». Eksempel: «NFR-3 Hosted development — *bør*; gjøres først når FR-1–FR-13 og NFR-2 består.» Skriv også om FR-1 til én enkel DB-basert teller for pålogging i stedet for «shared enforcement across instances» hvis dere ikke kjører flere instanser.

### 4.2 Motstridende og utdaterte formuleringer
- **Alvorlighet:** medium
- **Hvor:** FR-15 («The case specification must define the exact milestone-to-hint selection … before implementation») mot D-2 («Resolved»); FR-9 («adjustable through documented playtesting») mot siste avsnitt i «Implementation readiness» («may not … change the 12-turn starting budget»)
- **Problem og hvorfor det betyr noe:** En agent eller utvikler som leser FR-15 tror hintreglene mangler. Hvem som kan endre 12 turer, er uklart. Slike motsetninger gir feil stories.
- **Forslag:** Slett den utdaterte setningen i FR-15 og henvis til hint-tabellen i `case-spec.md`. Skriv i FR-9: «Budsjettet er 12; endring krever en beslutning fra gruppen som logges i addendumet.»

### 4.3 Prosesshistorikk blandet inn i kravene
- **Alvorlighet:** medium
- **Hvor:** «Purpose and source precedence» («refined by the user's PRD decisions on 2026-11-08»), «The user approved the complete authored case», NFR-6 («an agent cannot waive its own misses»)
- **Problem og hvorfor det betyr noe:** Godkjenningshistorikk og regler for agenter hører til i `.memlog.md`/addendum, ikke i kravene. De gjør dokumentet på ca. 3 500 ord tyngre og skjuler selve kravene for UX og stories.
- **Forslag:** Behold ett avsnitt om hva PRD-en bygger på, og flytt godkjenningsdatoer og agentregler til addendumet. Eksempel: «NFR-6: Misses must be corrected or accepted by a recorded team decision.»

### 4.4 FR-1 og NFR-1 er for store til å bli stories
- **Alvorlighet:** medium
- **Hvor:** FR-1 (ca. 600 ord med sju regelgrupper), NFR-1
- **Problem og hvorfor det betyr noe:** Registrering, innlogging, passordregler, begrensning, sesjonsutløp og gjenoppretting ligger under ett ID. Én story vil dekke alt, og en test kan ikke peke på ett krav.
- **Forslag:** Del i f.eks. FR-1a Registrering, FR-1b Pålogging og begrensning, FR-1c Sesjon og utløp, og la NFR-1 få tre kontrollerbare punkter (atomisk lagring, retry er idempotent, utdatert handling avvises).

### 4.5 Suksesskriterier som tester tesen
- **Alvorlighet:** medium
- **Hvor:** §Success criteria, «SM-1 — Functional completion: Verify FR-1 through FR-15 …», «SM-C1»
- **Problem og hvorfor det betyr noe:** SM-1 er en testplan, ikke et mål. Tesen er «approachable investigation … in approximately 15 minutes», men ingen SM sier hva som skal skje hvis testerne ikke forstår dommen. SM-C1 viser ikke til hvilken SM den balanserer.
- **Forslag:** Legg til en beslutningsregel for SM-3, uten prosentkrav: «Hvis minst to av tre testere ikke kan forklare hvorfor dommen ble som den ble, revideres verdikttekstene (FR-12) før levering.» Merk SM-C1 med «Counterbalances SM-3».

## 5. Mekaniske funn

- **Rekkefølge:** UJ-ene står som UJ-1, UJ-4, UJ-3, UJ-2. ID-ene er unike, men rekkefølgen forvirrer.
- **Begrepsbruk:** «clue», «evidence item» og «proof items» brukes om det samme som Glossary kaller *Evidence item* og *Key evidence*. «Character state» (FR-3) og «established authentication facilities» (FR-1, NFR-7) er udefinerte.
- **Personvern:** IP-adresser lagres for begrensning av pålogging. Skriv hvor lenge de oppbevares.
- **Antakelser:** PRD-en har ingen `[ASSUMPTION]`-merker og sier selv at ingen uavklarte antakelser brukes; det er konsekvent.
- **Krysshenvisninger:** FR/UJ/SM-henvisninger og lenker til `case-spec.md`/`case-data.json` fungerer.

## 6. Før dere går videre

**Må avklares før UX, arkitektur og epics:**
- Prioritering må/bør/kan for kravene (4.1), og om hosting skal vente.
- Rydd motsetningene i FR-9 og FR-15 (4.2).
- UX-dokumentene `DESIGN.md` og `EXPERIENCE.md` er foreløpig tomme maler, og PRD-en sier selv at ingen UI-stories kan starte uten dem.

**Kan vente:** del av FR-1/NFR-1 (4.4), glossarrydding, formulering av SM-C1, ukentlig kapasitet (men sjekk den hvis 2026-11-21 er i fare).

**Oppfølging av briefen:** ja. Testmodus/nøkkel er løst ved å fjerne KI i kjøretid, suksesskriteriene er gjort testbare, saksvarianter er tatt ut, åpne beslutninger er lukket og «ikke med» er eksplisitt. Rådet om å droppe Supabase/hosting er ikke fulgt (NFR-3).

## 7. Refleksjonsspørsmål

1. Mange av de strengeste reglene (15 tegn, begrensning per IP, 30 minutters sesjon) er beskrevet i detalj. Hvilke av dem valgte dere selv fordi spillet trenger dem, og hvilke tok dere imot fra KI-forslag uten å spørre om de var verdt tiden?
2. Dere har 12 planlagte agentøkter som skal teste spillet før menneskene. Hva gjør dere for å vite at en agents funn faktisk er et reelt problem, og ikke bare noe agenten fant på?

_Vurdert mot kvalitetsrubrikken i bmad-prd. Dette er veiledning, ikke sensur._
