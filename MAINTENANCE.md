# Maintenance

GitHub Actions refreshes the GitHub recommendations on Mondays at 14:23 UTC.
To refresh manually, open **Actions → Sync GitHub recommendations → Run workflow**
and select the default branch. Successful runs with identical recommendations
leave Git history alone. The README dates the last successful refresh that changed
the list. Use the Actions run history for the date of a successful no-change check.

## Credentials

The workflow uses the built-in repository token for the named stars endpoint
and to commit README updates. If GitHub hides the account’s stars from that
token, create a fine-grained personal access token for `natsteff` with
**Starring: Read-only** under user permissions. Limit repository access to
public repositories and set an expiration. Store the token in **Settings →
Secrets and variables → Actions** as `STARS_READ_TOKEN`, then run the workflow.
This credential reads the account’s stars. The built-in token publishes changes.
Rotate the account token before it expires. Keep its value out of files and logs.

## Editing the collection

Keep the GitHub stars markers in README.md. The script replaces only the content
between those markers after a successful paginated fetch. Other categories can
use separate Markdown files linked from the README.

Run the local tests with `python3 -m unittest discover -s scripts`.
