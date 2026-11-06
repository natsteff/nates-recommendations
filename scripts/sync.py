"""Render public GitHub stars into the GitHub section of README.md."""
import html
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

START = "<!-- github-stars:start -->\n"
END = "<!-- github-stars:end -->"
README = Path(__file__).resolve().parents[1] / "README.md"
ACCOUNT = "natsteff"
PRODUCT_NAMES = json.loads(Path(__file__).with_name("product-names.json").read_text(encoding="utf-8"))


def github(*args):
    result = subprocess.run(
        ["gh", "api", *args], capture_output=True, text=True, check=False
    )
    if result.returncode:
        raise SystemExit("GitHub API request failed. Check the workflow credential and retry.")
    return json.loads(result.stdout)


def markdown(text):
    return re.sub(r"([!\[\]()*_`~\\])", r"\\\1", html.escape(text))


def render(pages):
    entries = {}
    for page in pages:
        for repo in page:
            if repo.get("private") is not False or repo.get("visibility") != "public":
                continue
            name = repo["full_name"]
            if not re.fullmatch(r"[A-Za-z0-9-]+/[A-Za-z0-9_.-]+", name):
                raise ValueError("Unexpected public repository name")
            summary = " ".join((repo["description"] or "").split())
            owner, slug = name.split("/")
            product = PRODUCT_NAMES.get(name.casefold(), re.sub(r"[-_]+", " ", slug).title())
            line = f"- **{markdown(product)}** ([{name}](https://github.com/{name})) — {markdown(summary) or 'No description provided.'}"
            entries[name] = (product.casefold(), owner.casefold() == ACCOUNT, line)
    ordered = sorted(entries, key=lambda name: (entries[name][0], name.casefold()))
    recommendations = [entries[name][2] for name in ordered if not entries[name][1]]
    own = [entries[name][2] for name in ordered if entries[name][1]]
    return "\n".join([
        *(recommendations or ["_No public stars from other owners._"]),
        "", "### Shameless Self-Promotion", "",
        *(own or ["_No public stars from my own repositories._"]),
    ])


def update(readme, entries, today):
    before, generated = readme.split(START)
    old, after = generated.split(END)
    if old.partition("\n\n")[2] == entries + "\n":
        return readme
    return f"{before}{START}Last successful sync that changed this list (UTC) · {today}\n\n{entries}\n{END}{after}"


def main():
    if os.environ.get("ACCOUNT_TOKEN") == "1":
        if github("user")["login"] != ACCOUNT:
            raise SystemExit("The stars credential must belong to natsteff.")
        endpoint = "user/starred"
    else:
        endpoint = f"users/{ACCOUNT}/starred"
    pages = github(f"{endpoint}?per_page=100", "--paginate", "--slurp")
    if endpoint != "user/starred" and not any(pages):
        raise SystemExit("The repository token returned no visible stars. Configure STARS_READ_TOKEN for account access.")
    entries = render(pages)
    original = README.read_text(encoding="utf-8")
    revised = update(original, entries, datetime.now(timezone.utc).date().isoformat())
    if revised != original:
        README.write_text(revised, encoding="utf-8")


if __name__ == "__main__":
    main()
