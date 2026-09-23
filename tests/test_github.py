import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from language_donut.github import public_repositories


class PublicRepositoryTests(unittest.TestCase):
    @patch("language_donut.github.github_json")
    def test_exclusions_are_case_insensitive_and_accept_full_names(self, request):
        request.return_value = [
            {"name": "Profile", "full_name": "Owner/Profile"},
            {"name": "Hidden", "full_name": "Owner/Hidden"},
            {"name": "Visible", "full_name": "Owner/Visible"},
        ]
        config = {
            "excluded_repositories": {"owner/hidden"},
            "include_archived": False,
            "include_forks": False,
        }

        repositories = public_repositories("Owner", config)

        self.assertEqual(["Profile", "Visible"], repositories)

        config["excluded_repositories"].add("owner/profile")
        self.assertEqual(["Visible"], public_repositories("Owner", config))

    @patch("language_donut.github.github_json")
    def test_archived_repositories_are_included_and_forks_excluded(self, request):
        request.return_value = [
            {"name": "Profile", "full_name": "Owner/Profile"},
            {
                "name": "Archived",
                "full_name": "Owner/Archived",
                "archived": True,
            },
            {"name": "Fork", "full_name": "Owner/Fork", "fork": True},
        ]
        config = {
            "excluded_repositories": set(),
            "include_archived": True,
            "include_forks": False,
        }

        repositories = public_repositories("Owner", config)

        self.assertEqual(["Profile", "Archived"], repositories)


if __name__ == "__main__":
    unittest.main()
