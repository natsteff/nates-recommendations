import unittest

from sync import END, START, render, update


def repository(name, description="A summary", public=True):
    return {
        "full_name": name, "description": description,
        "private": not public, "visibility": "public" if public else "private",
    }


class SyncTests(unittest.TestCase):
    def test_pages_visibility_links_summaries_and_owner_marker(self):
        output = render([
            [repository("other/old", "[summary]<test>"), repository("other/private", public=False)],
            [repository("natsteff/own", None), repository("other/old", "[summary]<test>")],
        ])
        self.assertIn(r"**Old** ([other/old](https://github.com/other/old)) — \[summary\]&lt;test&gt;", output)
        self.assertEqual(output.count("other/old)"), 1)
        self.assertIn(r"**Own**\* ([natsteff/own](https://github.com/natsteff/own)) — No description provided.", output)
        self.assertEqual(output.count(r"\* Shameless Self-Promotion"), 1)
        self.assertNotIn("private", output)

    def test_excluded_repository_is_omitted_even_if_returned_as_public(self):
        output = render([[
            repository("CodeForEauClaire/codeforeauclaire.github.io"),
            repository("Bathlamos/programmers-playing-cards"),
        ]])
        self.assertNotIn("codeforeauclaire.github.io", output)
        self.assertNotIn("programmers-playing-cards", output)

    def test_sort_by_product_name_with_canonical_spelling(self):
        output = render([[
            repository("getwud/wud"),
            repository("nicolargo/glances"),
            repository("alexta69/metube"),
            repository("natsteff/tagcraft"),
            repository("natsteff/FGS-Studio"),
        ]])
        names = [line.split("**")[1] for line in output.splitlines() if line.startswith("- ")]
        self.assertEqual(names, ["Glances", "MeTube", "What’s Up Docker?", "TagCraft", "FGS Studio"])

    def test_category_order_and_default_for_new_stars(self):
        output = render([[
            repository("unmapped/new-tool"),
            repository("localsend/localsend"),
            repository("jellyfin/jellyfin"),
            repository("natsteff/tagcraft"),
        ]])
        headings = [line for line in output.splitlines() if line.startswith("##")]
        self.assertEqual(headings, [
            "## Docker & Self-Hosted Apps",
            "## Desktop & Mobile Apps",
            "## Other GitHub Stars",
        ])
        homelab, other = output.split("## Other GitHub Stars", 1)
        self.assertIn("**LocalSend**", homelab)
        self.assertIn(r"**TagCraft**\*", homelab.split("## Desktop & Mobile Apps")[1])
        self.assertTrue(other.startswith("\n\n- **New Tool**"))

    def test_star_unstar_and_no_change(self):
        readme = f"# Title\n## Homelab Recommendations\n### Infrastructure\n- Curated item\n{START}Pending\n{END}\n## Another category\n"
        original = update(readme, render([[repository("other/old")]]), "2026-11-06")
        new_entries = render([[repository("other/new")]])
        updated = update(original, new_entries, "2026-11-07")
        self.assertNotIn("other/old", updated)
        self.assertIn("other/new", updated)
        self.assertIn(new_entries + "\n\nLast successful sync that changed this list (UTC) · 2026-11-07\n" + END, updated)
        self.assertIn("- Curated item", updated)
        self.assertTrue(updated.endswith("## Another category\n"))
        self.assertEqual(update(updated, new_entries, "2026-11-08"), updated)

    def test_empty_account_list_removes_old_entries(self):
        self.assertIn("No public stars", render([[]]))
