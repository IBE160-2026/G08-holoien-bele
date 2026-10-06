# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G08 – G08-holoien |
| **Product brief** | `.docs/planning-artifacts/briefs/brief-G08-holoien-bele-2026-09-16/brief.md` (commit `35282da`), lest sammen med `addendum.md` i samme mappe |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

## Samlet vurdering

- **Godt utgangspunkt med justeringer.** Gruppen kan gå videre og innarbeide punktene under.

**Det som er bra:**

1. Kjerneflyten i «AI Detective Game» er tydelig beskrevet i fire steg: les saksbriefing, avhør 3–4 vitner/mistenkte, konfronter forklaringer med bevis, og anklag en skyldig med støttende bevis. Reglene for spørrebudsjett, tidlig anklage og forskjellen mellom «riktig skyldig» og «fullt bevist sak» gir konkrete regler som kan bli tester.
2. Dere har en sunn trinnvis plan: først én fast, forfattet sak («Initial test version»), deretter varianter fra forfattede mønstre, og helt KI-genererte plott bare som valgfri utvidelse. Integritetsregelen om at sakens fakta fastsettes før spillet og bevares gjennom hele forsøket, er et godt grep for å holde KI-dialogen under kontroll.

**De viktigste endringene:**

1. Planlegg hvordan sensor kan kjøre og teste spillet uten deres OpenRouter-nøkkel. I dag står det at live dialog krever internett og en OpenRouter-nøkkel, og at nøkkelhåndtering ved vurdering er åpen. Legg inn en testmodus med forhåndsskrevne svar for den faste saken, slik at hele kjerneflyten kan gjennomføres med `docker compose up --build` uten nøkkel.
2. Gjør valideringsmålene testbare. «Players can explain their accusation …» og «dialogue preserves character knowledge» er vanskelige å sjekke. Formuler i tillegg funksjonelle kriterier, for eksempel «en anklage med riktig skyldig, men uten nødvendig bevis, gir resultatet ‘riktig skyldig, ikke bevist’» og «en bruker får ikke åpnet en annen brukers forsøk».
3. Avgrens «Target delivery» med et tall. «A new case variation for each attempt» med uavklart antall mønstre og variasjonsregler kan vokse ukontrollert. Bestem for eksempel to–tre saksmønstre og hvilke elementer som varierer, og flytt resten til senere trinn.

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Vanskelig**

**Sammenlignbart med:** 3) KI-styrt simulering av prosjektledelse (vanskelig), fordi spillet har en tilstandsmaskin med regler som må stemme (avsløringer, budsjett, dom) og KI som skal oppføre seg konsistent innenfor den. Første testversjon med én fast sak ligger nærmere 7) Kurs-FAQ-chatbot (middels).

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Høy | Spørrebudsjett og telleregler, hva hver karakter får avsløre, hvilke bevis som utløser nye forklaringer, og regler for «tilstrekkelig bevis». Flere av disse er fortsatt åpne beslutninger. |
| Datamodell – antall entiteter og relasjoner mellom dem | Høy | Bruker, sesjon, forsøk, saksfakta, karakter, karaktertilstand, bevis, påstander, samtalehistorikk og anklage – med relasjoner mellom bevis og påstander. |
| Brukere, roller og innlogging | Middels | Én rolle, men egen registrering/innlogging og streng isolering av lagrede spill per bruker. Bruk et etablert bibliotek, slik dere selv foreslår. |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Høy | KI skal spille karakterer som lyver og holder på hemmeligheter uten å lekke skjult kunnskap. Dere må validere svar og ha definert oppførsel når et svar ikke består kontrollen. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Middels | OpenRouter er påkrevd for live dialog. Supabase er valgfritt og kan med fordel droppes helt. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Brukerne spiller hver for seg. Ingen sanntid mellom spillere. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Lav | Ingen opplasting. Saksmønstre kan ligge som versjonerte datafiler. |
| Sikkerhet og personvern | Middels | Passordhashing, sesjoner, eierskapskontroll og API-nøkkel på serveren. Lite personopplysninger utover brukernavn. |

**Hva vanskelighetsgraden betyr for dere:**

- _Vanskelig:_ Et vanskelig prosjekt gir større mulighet for toppkarakter, men også større risiko. For dere er den minimale versjonen allerede definert: én fast sak med avhør, bevis, budsjett, dom og lagring. Gjør den ferdig, testet og kjørbar via Docker før dere starter på saksvarianter.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | Risiko | Den faste saken er realistisk for to personer. Saksvarianter med sjekk av at hver variant er løsbar, er et stort ekstra stykke arbeid. Måldatoen 2026-11-21 gir lite slakk hvis varianter tas inn i samme runde. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | Risiko | Kjerneflyten er konkret, men listen «Open decisions» (telleregler, bevisregler, antall mønstre, rammeverk) må avklares i PRD-en. Ellers fyller KI-en hullene for dere. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | OK | Webapp med PostgreSQL, etablert autentisering og Docker Compose er godt dokumentert. Velg rammeverk tidlig i arkitekturen, og hold dere til én backend. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | Risiko | Spillreglene er deres egne og kan kontrolleres. Det vanskelige er å avgjøre om karakterene lekker hemmeligheter eller sier noe som strider mot saksfaktaene. Lag en fast liste med «fristende» spørsmål og forventet oppførsel som dere kjører mot hver prompt-endring. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | OK | Budsjett, avsløringsoverganger, dom og eierskap kan testes automatisk når de ligger i kode, slik addendumet foreslår. Selve dialogen må testes manuelt eller med mock-svar. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Stor risiko | Docker Compose er bra, men uten OpenRouter-nøkkel stopper avhørene. Uten en testmodus kan ikke sensor gjennomføre kjerneflyten. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | OpenRouter koster per kall, og budsjett og nøkkel ved vurdering er åpne. Sett et utgiftstak, gjør modellen konfigurerbar, og bygg en mock-modus. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart med justert omfang.** Se forslagene under.

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Definer v1 som den faste saken med alle mekanikker (budsjett, bevis, konfrontasjon, dom, lagring, innlogging) og en mock-modus for dialog. Legg saksvarianter i trinn 2, begrenset til to–tre forfattede mønstre der bare navn, motiv og noen bevisdetaljer varierer. Helt KI-genererte plott kan stå i Vision.
2. Dropp Supabase og valgfri hosting fra planen inntil lokal kjøring med Docker er ferdig. Det fjerner en hel konfigurasjonsflate (TLS, pooling, miljøer) som ikke gir uttelling hvis kjerneflyten ikke er stabil.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

Briefen bruker egne overskrifter («Product and audience», «Core experience», «Scope and development stages» osv.). Det er greit, men vurderingen under er gjort mot malens deler.

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | OK | «Product and audience» forklarer raskt hva spillet er: et tekstbasert detektivspill på en politistasjon, ca. 15 minutter og 3–4 avhørsobjekter. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | Juster | Problemet er indirekte formulert som verdien av å kunne stille frie spørsmål. Skriv en setning om hva som mangler i eksisterende detektivspill for spilleren, så PRD-en har et tydelig «hvorfor». |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | OK | «Core experience» beskriver spilleropplevelsen godt. Docker-, Supabase- og OpenRouter-detaljene hører derimot hjemme i arkitekturen og kan flyttes ut av briefen. |
| What Makes This Different – er vurderingen ærlig og realistisk? | OK | Det er ærlig at dette er en hypotese, ikke dokumentert etterspørsel, og addendumet viser til et lignende spill (Vaudeville). |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | Juster | «People who enjoy crime fiction and logical puzzles» er en start. Beskriv én primærspiller mer konkret, for eksempel om de spiller på PC eller mobil, og om de er vant til tekstspill. Det påvirker designet av avhørsskjermen. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | Endre | Kriteriene er kalt «proposed validation targets» og er delvis subjektive. Legg til funksjonelle, testbare kriterier for dom, budsjett, lagring/gjenopptak og isolasjon mellom brukere. |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | Juster | Trinnene er gode, men «Target delivery» mangler en grense for antall mønstre og variasjoner. Legg også til en eksplisitt «ikke med»-liste (for eksempel e-postverifisering, hosting og KI-genererte plott). |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | OK | Helt KI-genererte plott er tydelig merket som valgfri utvidelse og ikke et krav. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | Juster | Brief og addendum er grundige og har allerede blitt revidert (25. september). Ta de åpne beslutningene inn i PRD-en med begrunnelse, så sensor kan se hvordan dere landet dem. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | Juster | Kjerneflyten er tydelig og har nok innhold. Risikoen ligger i saksvariantene – sett et tak. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | Endre | Spillreglene er testbare, men suksesskriteriene må skrives om til konkrete testtilfeller, og dere trenger en plan for å teste KI-dialogen (fast spørsmålssett og mock). |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Juster | Skjermbildene kan utledes (briefing, avhør, bevisoversikt, anklage, resultat). Lag gjerne enkle skisser i UX-steget, inkludert visning av gjenstående spørsmål. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | OK | Én PostgreSQL, én backend og Docker Compose er fornuftig. Unngå å bygge for to miljøer (lokal og Supabase) samtidig. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Endre | `docker compose up --build` er et godt mål, men kjerneflyten krever i dag en OpenRouter-nøkkel. Legg inn mock-modus og beskriv den i README. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Juster | Briefen sier at nøkkelen skal ligge på serveren. Planlegg `.env.example`, `.gitignore` for `.env`, og en egen mappe for saksmønstre. Addendumet inneholder en lokal filsti fra en personlig maskin – den kan fjernes. |

## 3. Neste steg for gruppen

1. Skriv om «Success and assessment» med 5–8 funksjonelle, testbare kriterier (dom, budsjett, lagring, isolasjon, Docker-oppstart) og legg til en eksplisitt «ikke med i v1»-liste.
2. Ta stilling til de viktigste åpne beslutningene (telleregel for spørsmål, regel for tilstrekkelig bevis, antall saksmønstre) og skriv dem inn i PRD-en.
3. Bestem i arkitekturen hvordan mock-/testmodus for dialogen skal fungere, og hvordan sensor skal kjøre appen uten deres OpenRouter-nøkkel.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
