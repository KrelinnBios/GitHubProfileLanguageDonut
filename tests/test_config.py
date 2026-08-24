import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from language_donut.config import load_config


class ConfigTests(unittest.TestCase):
    def test_repository_exclusions_are_normalized(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"
            path.write_text(
                json.dumps(
                    {
                        "owner": " KrelinnBios ",
                        "excluded_repositories": ["Owner/Hidden", " Repo "],
                    }
                ),
                encoding="utf-8",
            )

            result = load_config(path)

            self.assertEqual("KrelinnBios", result["owner"])
            self.assertEqual(
                {"owner/hidden", "repo"}, result["excluded_repositories"]
            )

    def test_configuration_root_must_be_an_object(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"
            path.write_text("[]", encoding="utf-8")

            with self.assertRaisesRegex(RuntimeError, "root must be a JSON object"):
                load_config(path)


if __name__ == "__main__":
    unittest.main()
