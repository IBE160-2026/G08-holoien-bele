# Hosting setup

## Verified setup

Daniel confirmed ownership of the group's Vercel and Supabase projects on 2026-11-09. H01 covers provider setup; R01/F01 retain framework, schema, migration and application configuration decisions.

| Item | Verified state |
|---|---|
| Supabase organization | G08 Skarmory (`nmyliugrywszxubbkxsq`), Free plan |
| Supabase project | `g08-skarmory` (`jyscyqgsztgokuveolgt`) |
| Region | Stockholm, `eu-north-1`, explicitly confirmed by Daniel |
| Cost quote | $0/month for project creation; no paid plan or add-on requested |
| Database | PostgreSQL 17.11; test query succeeded; provider reports `ACTIVE_HEALTHY` |
| Schema | `public` has no tables; no application migrations run |
| Security advisor | No findings on the empty project; application security remains untested |
| Vercel | Account creation/import not verified; no deployment URL |

[Open the Supabase project](https://supabase.com/dashboard/project/jyscyqgsztgokuveolgt).

## Vercel account and import

1. Daniel creates a Hobby account at [Vercel signup](https://vercel.com/signup), using Continue with GitHub and his course GitHub account. Daniel completes sign-in and any account terms himself.
2. Use one Vercel project for `IBE160-2026/G08-holoien-bele`. Check for an existing project before importing. The supplied teacher announcement says the organization GitHub integration is already installed; do not reinstall it or change GitHub settings as part of this task.
3. After F01 provides a deployable app, choose Add New / Project and import the group repository. Confirm the actual framework, root directory, build command and output from the app. Today the repository has planning artifacts and no runnable app, so these values cannot yet be verified.
4. Confirm production branch `main`; configure server-only environment variables against the agreed application contract. Keep preview data separate from production. R01 must decide how to achieve this within the free budget before database-backed previews run.
5. Deploy, verify the actual application and a PR preview, and add the observed production URL to README. A connected repo or successful static placeholder would not establish that the game works.

The announcement supplies course context; it does not make Supabase a course requirement. The team previously selected Supabase for hosted PostgreSQL and app-owned username/password authentication. Local delivery still uses the agreed Docker Compose stack with plain PostgreSQL.

## Database connection handoff for R01/F01

Use the project's Connect dialog to obtain the actual PostgreSQL connection details. Supabase recommends the transaction pooler for serverless workloads. The selected driver must use compatible pooling/prepared-statement settings and encrypted connections. Choose a migration connection separately according to the migration tool and available network support.

The application has no environment contract yet. `DATABASE_URL` is a possible server-only name, not a configured or implemented variable. Do not use `VITE_` or `NEXT_PUBLIC_` prefixes for a database connection string or password. Supabase API keys are not PostgreSQL passwords; this database-only design does not currently require a browser Supabase client or Supabase Auth.

Store credentials in provider environment settings and ignored local environment files. Never commit or paste credentials into this document, README, PR descriptions or session logs. Redeploy after changing Vercel environment variables; existing deployments keep their previous values.

## Remaining verification

- Vercel account, project import, Git linkage and production branch.
- R01/F01 app framework, server-only environment contract, migration process and preview data separation.
- Runtime connection from the deployed application, account isolation and persisted progress.
- Production URL in README and working per-PR preview.
- GitHub CLI was not found on this machine; optional teacher-recommended installation/login remains user setup work.

## References

- [Vercel Git deployments](https://vercel.com/docs/git)
- [Vercel environment variables](https://vercel.com/docs/environment-variables)
- [Supabase PostgreSQL connections](https://supabase.com/docs/guides/database/connecting-to-postgres)
- [Supabase environment management](https://supabase.com/docs/guides/deployment/managing-environments)
