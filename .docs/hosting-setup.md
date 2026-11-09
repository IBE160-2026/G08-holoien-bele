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
| Vercel | Daniel submitted a signup appeal; account/import pending; no deployment URL |
| GitHub CLI | 2.103.3 installed per-user; signed in as NorskNoobing using Windows keyring; repository WRITE access verified |
| Docker | Engine 29.9.2 and Compose v5.6.1 available; `docker run --rm hello-world` passed outside agent sandbox |
| Local hosted database connection | Ignored `.env` configured; session-pooler authentication and read-only `SELECT 1` passed from local Docker psql 17.11; client reports TLS 1.3 |

[Open the Supabase project](https://supabase.com/dashboard/project/jyscyqgsztgokuveolgt).

## Vercel account and import

1. Daniel submitted the required signup appeal; await Vercel's response. Once cleared, complete a Hobby account at [Vercel signup](https://vercel.com/signup), using Continue with GitHub and his course GitHub account. Daniel completes sign-in and any account terms himself.
2. Use one Vercel project for `IBE160-2026/G08-holoien-bele`. Check for an existing project before importing. The supplied teacher announcement says the organization GitHub integration is already installed; do not reinstall it or change GitHub settings as part of this task.
3. After F01 provides a deployable app, choose Add New / Project and import the group repository. Confirm the actual framework, root directory, build command and output from the app. Today the repository has planning artifacts and no runnable app, so these values cannot yet be verified.
4. Confirm production branch `main`; configure server-only environment variables against the agreed application contract. Keep preview data separate from production. R01 must decide how to achieve this within the free budget before database-backed previews run.
5. Deploy, verify the actual application and a PR preview, and add the observed production URL to README. A connected repo or successful static placeholder would not establish that the game works.

The announcement supplies course context; it does not make Supabase a course requirement. The team previously selected Supabase for hosted PostgreSQL and app-owned username/password authentication. Local delivery still uses the agreed Docker Compose stack with plain PostgreSQL.

## Database connection handoff for R01/F01

Use the project's Connect dialog to obtain the actual PostgreSQL connection details. Supabase recommends the transaction pooler for serverless workloads. The selected driver must use compatible pooling/prepared-statement settings and encrypted connections. Choose a migration connection separately according to the migration tool and available network support.

The root [`.env.example`](../.env.example) now provides a blank, server-only `DATABASE_URL` connection handoff. No application consumes this variable yet; F01 must implement environment loading and validation. Do not use `VITE_` or `NEXT_PUBLIC_` prefixes for a database connection string or password. Supabase API keys are not PostgreSQL passwords; this database-only design does not currently require a browser Supabase client or Supabase Auth.

Store credentials in provider environment settings and ignored local environment files. Never commit or paste credentials into this document, README, PR descriptions or session logs. Redeploy after changing Vercel environment variables; existing deployments keep their previous values.

## Shared Supabase access

Daniel owns the G08 Skarmory organization. Jakob does not yet have a Supabase account (reported by Daniel on 2026-11-09), so his membership is pending. GitHub repository membership does not automatically grant Supabase dashboard access. Each developer uses their own Supabase account; no shared account password is needed.

1. Jakob creates his own account at [Supabase Dashboard](https://supabase.com/dashboard). He does not need to create another project or organization for this group.
2. Daniel opens [G08 Skarmory team settings](https://supabase.com/dashboard/org/nmyliugrywszxubbkxsq/team), chooses the invitation control, enters Jakob's account email and selects **Developer**. This is the recommended development role; Daniel remains Owner. Developer grants project content access but not project-setting administration. Organization-scoped access covers all current and future projects in this group organization; project-scoped roles require Team/Enterprise plans.
3. Jakob accepts the email invitation within 24 hours and confirms he can open `g08-skarmory` and its SQL Editor. Invitation creation/acceptance has not been verified. The connected Supabase tool has no member-management operation, so these steps must be completed in the dashboard.
4. Each person connects their own Supabase coding-agent integration if wanted. Daniel's ChatGPT connection does not install or authorize one for Jakob.

## Credential workflow

The supplied teacher announcement says to put keys and database addresses under Vercel **Settings > Environment Variables**, keep local values in an ignored `.env` file, and never commit passwords/API keys/database connection strings. It warns that `VITE_` and `NEXT_PUBLIC_` variables are browser-visible. It does not specify a shared password vault or automatic database migration workflow.

Recommended minimal setup for this database-only application:

| Where | Configuration | Who sets it |
|---|---|---|
| Git repository | Blank `.env.example`, setup documentation and future migration files | Both developers through task PRs |
| Each developer machine | Ignored `.env` with a private `DATABASE_URL` | Each developer |
| Future Vercel Production | Server-only `DATABASE_URL` in project environment settings | Daniel as Vercel project owner |
| Future Vercel Preview | Its own test database connection; no production data | Daniel after preview separation is agreed |
| GitHub Actions | Local disposable database for tests; no hosted DB secret currently needed | F01 CI setup |

For local hosted-database testing, copy the template only if `.env` does not exist:

```powershell
if (-not (Test-Path -LiteralPath .env)) {
    Copy-Item -LiteralPath .env.example -Destination .env
}
```

Then edit `.env` privately. Get the actual pooler URI from the project's **Connect** dialog; retain its exact host, username and port, use the database password, and URL-encode any password characters that require it. Require encrypted transport (for URI-based clients, `sslmode=require`); use driver settings compatible with transaction pooling. API keys and Supabase account passwords are not PostgreSQL database passwords. Do not reset an existing database password merely to onboard a teammate; coordinate any necessary rotation because it invalidates clients using the old password. If an existing database password must be handed off, use a private password-manager share rather than GitHub, chat or a committed file. A database runtime role and a migration role can be defined with the actual schema during F01; no role/password changes were made by this preparation.

Dashboard membership and PostgreSQL credentials are separate. Membership does not guarantee the database password can be recovered. No actual connection secret is committed. The initial Supabase connector query verified provider-side access only; a subsequent local PostgreSQL client test also passed as recorded below. Full application connection verification follows when a backend exists and Vercel credentials are configured.

For Daniel's first local client test, an ignored `.env` has been created from the template. In **Connect > Direct**, choose **Session pooler** for a local IPv4-compatible client and copy its URI. Substitute the URL-encoded database password privately and require SSL. The initial project-creation tool did not return a database password. If it was not saved elsewhere, Daniel must set a new one through **Database > Settings > Reset database password** and update `.env` himself. No password reset has been performed by the agent.

The official `postgres:17-alpine` Docker image is cached for a disposable PostgreSQL client test (`psql` 17.11 verified). It is only a client for the hosted database in this check; no local database server or volume was created. Daniel saved the private URI/password in `.env`; the agent added the missing `sslmode=require` option without displaying the secret. Session-pooler authentication and read-only `SELECT 1` passed from this machine, and psql's `\conninfo` reported TLS 1.3. Database-side `pg_stat_ssl` is not the client-to-pooler TLS check; use the client's connection information for this hop. No tables or application data changed, and test containers used `--rm`. This does not establish that the future backend loads `.env` correctly.

Once Vercel signup is approved, import the existing GitHub repo, add `DATABASE_URL` for the intended environment, and deploy the actual backend. Pushing code to GitHub does not upload local `.env` values. Keep the current shared hosted database to disposable development/test data until production/preview separation is established. Do not enable paid database branching or provision another project as an implicit part of onboarding.

## Local tool setup

GitHub CLI is installed at `%LOCALAPPDATA%\Programs\GitHub CLI\bin\gh.exe`; its bin directory was added to the user PATH. Open a new terminal if an existing session cannot find `gh`. Windows Package Manager downloads timed out twice; the official release API download verified against GitHub's SHA256 and the MSI signature. The MSI returned error 1603, so installation used the official checksum-verified portable archive instead. `gh auth status` confirms keyring storage and HTTPS; `gh repo view` confirms WRITE access to this repository. The existing Git credential helper was preserved.

Docker's `desktop-linux` context responds outside the restricted agent sandbox. The earlier named-pipe permission error occurred within that sandbox; no Docker group memberships, service settings or pipe permissions were changed. Docker's official `hello-world` image pulled and ran successfully with `--rm`; the image remains cached. This verifies basic engine operation, not the future application Compose stack.

## Shared agent skills

Official [Supabase agent skills](https://github.com/supabase/agent-skills) are vendored at revision `c9be0e931b7930f7d02126d04774d904c381e7d7` under `.agents/skills/supabase/` and `.agents/skills/supabase-postgres-best-practices/`, including references and MIT license notices. `.claude/skills/` has entry points that load those canonical copies. The Codex skill-installer helper installed the pinned repository-local source; no global installation or application package dependency was added.

After pulling this setup branch (or main after its PR merges), Daniel and Jakob can use the same guidance in Codex and Claude Code. Newly installed skills become available on the next turn; reopen the project/session if a client still shows its old catalog. These are instructions for coding agents; each person still needs their own Supabase account and any desired MCP/plugin authorization. They do not connect the application or distribute database secrets. Update the pinned skills deliberately in a task PR and keep the Claude entry points aligned; avoid a blanket skills update that also changes the existing BMAD setup.

## Remaining verification

- Vercel account, project import, Git linkage and production branch.
- R01/F01 app framework, server-only environment contract, migration process and preview data separation.
- Runtime connection from the deployed application, account isolation and persisted progress.
- Production URL in README and working per-PR preview.
- Jakob's Supabase account, invitation acceptance and project access.
- Actual local/Vercel backend connection test; the independent local PostgreSQL client connection is verified.

## References

- [Vercel Git deployments](https://vercel.com/docs/git)
- [Vercel environment variables](https://vercel.com/docs/environment-variables)
- [Supabase PostgreSQL connections](https://supabase.com/docs/guides/database/connecting-to-postgres)
- [Supabase environment management](https://supabase.com/docs/guides/deployment/managing-environments)
- [Supabase organization roles and invitations](https://supabase.com/docs/guides/platform/access-control)
