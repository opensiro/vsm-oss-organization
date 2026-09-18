from __future__ import annotations

import base64
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "mint_github_app_token.py"
SPEC = importlib.util.spec_from_file_location("mint_github_app_token", SCRIPT)
assert SPEC and SPEC.loader
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class GithubAppTokenHelperTests(unittest.TestCase):
    def test_parse_permission(self) -> None:
        self.assertEqual(("contents", "write"), mod.parse_permission("contents=write"))
        self.assertEqual(("issues", "read"), mod.parse_permission(" issues = read "))
        with self.assertRaises(ValueError):
            mod.parse_permission("contents=admin")

    def test_b64url_has_no_padding(self) -> None:
        encoded = mod.b64url(b"abcde")
        self.assertNotIn("=", encoded)
        restored = base64.urlsafe_b64decode(encoded + "=" * (-len(encoded) % 4))
        self.assertEqual(b"abcde", restored)

    def test_canonical_json_is_stable(self) -> None:
        left = mod.canonical_json({"b": 1, "a": 2})
        right = mod.canonical_json({"a": 2, "b": 1})
        self.assertEqual(left, right)
        self.assertEqual({"a": 2, "b": 1}, json.loads(left))

    def test_secret_writer_is_create_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "token"
            mod.write_secret(path, "secret")
            self.assertEqual("secret\n", path.read_text())
            with self.assertRaises(FileExistsError):
                mod.write_secret(path, "replacement")


if __name__ == "__main__":
    unittest.main()
