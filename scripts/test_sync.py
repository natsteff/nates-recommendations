import unittest

from sync import END, START, render, update


def repository(name, description="A summary", public=True):
    return {
        "full_name": name, "description": description,
        "private": not public, "visibility": "public" if public else "private",
    }


class SyncTests(unittest.TestCase):
    def test_pages_visibility_links_summaries_and_owner_sections(self):
        output = render([
            [repository("other/old", "[summary]<test>"), repository("other/private", public=False)],
            [repository("natsteff/own", None), repository("other/old", "[summary]<test>")],
        ])
        recommendations, self_promotion = output.split("### Shameless Self-Promotion")
        self.assertIn(r"**Old** ([other/old](https://github.com/other/old)) — \[summary\]&lt;test&gt;", recommendations)
        self.assertEqual(output.count("other/old)"), 1)
        self.assertIn("**Own** ([natsteff/own](https://github.com/natsteff/own)) — No description provided.", self_promotion)
        self.assertNotIn("private", output)
        self.assertNotIn("natsteff/own", recommendations)

    def test_sort_by_product_name_with_canonical_spelling(self):
        output = render([[
            repository("getwud/wud"),
            repository("nicolargo/glances"),
            repository("alexta69/metube"),
            repository("natsteff/tagcraft"),
            repository("natsteff/FGS-Studio"),
        ]])
        names = [line.split("**")[1] for line in output.splitlines() if line.startswith("- ")]
        self.assertEqual(names, ["Glances", "MeTube", "What’s Up Docker?", "FGS Studio", "TagCraft"])

    def test_star_unstar_and_no_change(self):
        readme = f"# Title\n{START}Pending\n{END}\n## Another category\n"
        original = update(readme, render([[repository("other/old")]]), "2026-11-06")
        new_entries = render([[repository("other/new")]])
        updated = update(original, new_entries, "2026-11-07")
        self.assertNotIn("other/old", updated)
        self.assertIn("other/new", updated)
        self.assertIn("2026-11-07", updated)
        self.assertTrue(updated.endswith("## Another category\n"))
        self.assertEqual(update(updated, new_entries, "2026-11-08"), updated)

    def test_empty_account_list_removes_old_entries(self):
        self.assertIn("No public stars", render([[]]))
