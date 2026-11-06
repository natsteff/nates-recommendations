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
EXCLUDED_REPOSITORIES = {
    "bathlamos/programmers-playing-cards",
    "codeforeauclaire/codeforeauclaire.github.io",
}
PRODUCT_NAMES = json.loads(Path(__file__).with_name("product-names.json").read_text(encoding="utf-8"))
STAR_CATEGORIES = json.loads(Path(__file__).with_name("star-categories.json").read_text(encoding="utf-8"))
CATEGORY_HEADINGS = {
    "homelab": "### Docker & Self-Hosted Apps",
    "desktop": "## Desktop & Mobile Apps",
    "web": "## Web Apps",
    "games": "## Browser Games",
    "other": "## Other GitHub Stars",
}


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
    has_own_projects = False
    categories = {name: key for key, names in STAR_CATEGORIES.items() for name in names}
    for page in pages:
        for repo in page:
            if repo.get("private") is not False or repo.get("visibility") != "public":
                continue
            name = repo["full_name"]
            if name.casefold() in EXCLUDED_REPOSITORIES:
                continue
            if not re.fullmatch(r"[A-Za-z0-9-]+/[A-Za-z0-9_.-]+", name):
                raise ValueError("Unexpected public repository name")
            summary = " ".join((repo["description"] or "").split())
            owner, slug = name.split("/")
            product = PRODUCT_NAMES.get(name.casefold(), re.sub(r"[-_]+", " ", slug).title())
            own_project = owner.casefold() == ACCOUNT
            has_own_projects |= own_project
            marker = r"\*" if own_project else ""
            line = f"- **{markdown(product)}**{marker} ([{name}](https://github.com/{name})) — {markdown(summary) or 'No description provided.'}"
            category = categories.get(name.casefold(), "other")
            entries[name] = (product.casefold(), category, line)
    sections = {key: [] for key in CATEGORY_HEADINGS}
    for name in sorted(entries, key=lambda name: (entries[name][0], name.casefold())):
        _, category, line = entries[name]
        sections[category].append(line)
    blocks = [
        heading + "\n\n" + "\n".join(sections[key])
        for key, heading in CATEGORY_HEADINGS.items()
        if sections[key]
    ]
    if has_own_projects:
        blocks.append(r"\* Shameless Self-Promotion")
    return "\n\n".join(blocks) or "_No public stars._"


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
