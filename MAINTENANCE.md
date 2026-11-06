# Maintenance

The weekly refresh runs from Nate’s Codex chat on Mondays at 8:23 a.m.
America/Chicago. It uses the existing GitHub CLI sign-in on Nate’s Mac,
so the Mac and Codex need to be available. To refresh on demand, ask in the
same chat or run `ACCOUNT_TOKEN=1 python3 scripts/sync.py` from a current
default-branch checkout, then commit and push README.md if it changed.

The README dates the last successful refresh that changed the list.
Successful checks with identical recommendations leave Git history alone.

## Optional GitHub Actions refresh

The GitHub workflow is manual only. To use it, create a fine-grained
personal access token for `natsteff` with **Starring: Read-only** under user
permissions, limit repository access to public repositories, and set an
expiration. Store it as `STARS_READ_TOKEN` in **Settings → Secrets and
variables → Actions**. Open **Actions → Sync GitHub recommendations →
Run workflow** and select the default branch. The built-in workflow token
publishes changes. Keep the account token out of files and logs.
The local Codex refresh uses the GitHub CLI sign-in and requires no Actions secret.

## Editing the collection

Keep the GitHub stars markers in README.md. The script replaces only the content
between those markers after a successful paginated fetch. Other categories can
use separate Markdown files linked from the README.

Run the local tests with `python3 -m unittest discover -s scripts`.
