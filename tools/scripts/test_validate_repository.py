from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/scripts/validate-repository.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("agf_validator_under_test", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load repository validator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


validator = load_validator()


class ProductBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.original_root = getattr(validator, "ROOT")
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        for directory in ("consulting", "docs/patterns", "docs/explanations", "controls"):
            (self.root / directory).mkdir(parents=True)

        shutil.copy2(REPO_ROOT / "consulting/README.md", self.root / "consulting/README.md")
        shutil.copy2(
            REPO_ROOT / "consulting/consulting-engagement-model.md",
            self.root / "consulting/consulting-engagement-model.md",
        )
        self.core_markdown = self.root / "docs/patterns/core.md"
        self.core_markdown.write_text("Nenhuma tool entra em produção sem owner.\n", encoding="utf-8")
        self.case_markdown = self.root / "docs/explanations/case.md"
        self.case_markdown.write_text("Microsoft aparece apenas como caso opcional.\n", encoding="utf-8")
        self.core_json = self.root / "controls/core.json"
        self.core_json.write_text('{"platform": "portable"}\n', encoding="utf-8")
        self.files = [
            self.root / "consulting/README.md",
            self.root / "consulting/consulting-engagement-model.md",
            self.core_markdown,
            self.case_markdown,
            self.core_json,
        ]
        setattr(validator, "ROOT", self.root)

    def tearDown(self) -> None:
        setattr(validator, "ROOT", self.original_root)
        self.temporary.cleanup()

    def test_accepts_valid_packaging_and_optional_case(self) -> None:
        self.assertEqual([], validator.validate_product_boundaries(self.files))

    def test_rejects_legacy_commercial_path(self) -> None:
        legacy = self.root / "docs/executive/consulting-engagement-model.md"
        legacy.parent.mkdir(parents=True)
        legacy.write_text("commercial leak\n", encoding="utf-8")
        issues = validator.validate_product_boundaries(self.files + [legacy])
        self.assertTrue(any(issue.category == "boundary" and issue.path == str(legacy.relative_to(self.root)) for issue in issues))

    def test_rejects_module_missing_from_package_rows(self) -> None:
        packaging = self.root / "consulting/README.md"
        packaging.write_text(
            packaging.read_text(encoding="utf-8").replace("Governance Readiness Assessment", "Missing Module"),
            encoding="utf-8",
        )
        issues = validator.validate_product_boundaries(self.files)
        self.assertTrue(any("offer module must appear once" in issue.message for issue in issues))

    def test_rejects_vendor_name_in_core_json(self) -> None:
        self.core_json.write_text('{"platform": "Microsoft"}\n', encoding="utf-8")
        issues = validator.validate_product_boundaries(self.files)
        self.assertTrue(any(issue.category == "vendor-neutrality" and issue.path == "controls/core.json" for issue in issues))


class FrontmatterRelatedPathTests(unittest.TestCase):
    def setUp(self) -> None:
        self.original_root = getattr(validator, "ROOT")
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "docs").mkdir()
        setattr(validator, "ROOT", self.root)

    def tearDown(self) -> None:
        setattr(validator, "ROOT", self.original_root)
        self.temporary.cleanup()

    def test_accepts_existing_related_list_target(self) -> None:
        target = self.root / "docs/target.md"
        target.write_text("# Target\n", encoding="utf-8")
        source = self.root / "docs/source.md"
        source.write_text("---\nrelated:\n  - target.md\n---\n\n# Source\n", encoding="utf-8")
        self.assertEqual([], validator.validate_frontmatter_related_paths([source]))

    def test_rejects_missing_related_mapping_target(self) -> None:
        source = self.root / "docs/source.md"
        source.write_text("---\nrelated:\n  policy: missing.md\n---\n\n# Source\n", encoding="utf-8")
        issues = validator.validate_frontmatter_related_paths([source])
        self.assertTrue(any(issue.category == "frontmatter-related" for issue in issues))


if __name__ == "__main__":
    unittest.main()
