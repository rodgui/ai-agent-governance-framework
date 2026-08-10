from __future__ import annotations

import importlib.util
import json
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
        for directory in (
            ".github/workflows",
            "consulting",
            "docs/patterns",
            "docs/explanations",
            "controls",
            "templates",
        ):
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
        self.canonical_template = self.root / "templates/canonical.md"
        self.canonical_template.write_text("# Modular template\n", encoding="utf-8")
        self.workflow = self.root / ".github/workflows/quality-gates.yml"
        self.workflow.write_text(
            "asset: docs/explanations/diagrams/microsoft-customer-zero-agent-governance.png\n",
            encoding="utf-8",
        )
        self.files = [
            self.root / "consulting/README.md",
            self.root / "consulting/consulting-engagement-model.md",
            self.core_markdown,
            self.case_markdown,
            self.core_json,
            self.canonical_template,
            self.workflow,
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

    def test_rejects_lowercase_vendor_name_in_core_json(self) -> None:
        self.core_json.write_text('{"platform": "microsoft"}\n', encoding="utf-8")
        issues = validator.validate_product_boundaries(self.files)
        self.assertTrue(any(issue.category == "vendor-neutrality" and issue.path == "controls/core.json" for issue in issues))

    def test_rejects_ambiguous_lowercase_vendor_names_in_structured_core(self) -> None:
        for vendor in ("entra", "defender"):
            with self.subTest(vendor=vendor):
                self.core_json.write_text(json.dumps({"platform": vendor}) + "\n", encoding="utf-8")
                issues = validator.validate_product_boundaries(self.files)
                self.assertTrue(
                    any(issue.category == "vendor-neutrality" and issue.path == "controls/core.json" for issue in issues)
                )

    def test_accepts_capitalized_portuguese_verbs_in_core_markdown(self) -> None:
        self.core_markdown.write_text(
            "Entra em produção somente após o gate. Defender a neutralidade é obrigatório.\n",
            encoding="utf-8",
        )
        issues = validator.validate_product_boundaries(self.files)
        self.assertFalse(any(issue.category == "vendor-neutrality" and issue.path == "docs/patterns/core.md" for issue in issues))

    def test_rejects_ambiguous_vendor_names_with_product_context_in_core_markdown(self) -> None:
        for vendor in ("Entra ID", "entra id", "Defender for Cloud", "defender for cloud", "key vault"):
            with self.subTest(vendor=vendor):
                self.core_markdown.write_text(f"Plataforma obrigatória: {vendor}.\n", encoding="utf-8")
                issues = validator.validate_product_boundaries(self.files)
                self.assertTrue(
                    any(
                        issue.category == "vendor-neutrality"
                        and issue.path == "docs/patterns/core.md"
                        for issue in issues
                    )
                )

    def test_accepts_unrelated_template_version_label(self) -> None:
        self.canonical_template.write_text("# Risk Assessment (V1)\n", encoding="utf-8")
        issues = validator.validate_product_boundaries(self.files)
        self.assertFalse(
            any(issue.category == "policy-history" and issue.path == "templates/canonical.md" for issue in issues)
        )

    def test_rejects_vendor_dependency_in_quality_gate_workflow(self) -> None:
        self.workflow.write_text(
            self.workflow.read_text(encoding="utf-8") + "uses: microsoft/vendor-action@v1\n",
            encoding="utf-8",
        )
        issues = validator.validate_product_boundaries(self.files)
        self.assertTrue(
            any(
                issue.category == "vendor-neutrality"
                and issue.path == ".github/workflows/quality-gates.yml"
                for issue in issues
            )
        )

    def test_rejects_tenth_offer_heading(self) -> None:
        model = self.root / "consulting/consulting-engagement-model.md"
        model.write_text(model.read_text(encoding="utf-8") + "\n## Oferta 10 — Extra\n", encoding="utf-8")
        issues = validator.validate_product_boundaries(self.files)
        self.assertTrue(any("exactly nine ordered offer modules" in issue.message for issue in issues))

    def test_rejects_policy_v1_label_in_canonical_template(self) -> None:
        self.canonical_template.write_text("# Self-Assessment Form — AI Agents (V1)\n", encoding="utf-8")
        issues = validator.validate_product_boundaries(self.files)
        self.assertTrue(any(issue.category == "policy-history" for issue in issues))


class JsonValidationRobustnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.original_root = getattr(validator, "ROOT")
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        for source in REPO_ROOT.rglob("*.json"):
            destination = self.root / source.relative_to(REPO_ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        self.json_files = sorted(self.root.rglob("*.json"))
        setattr(validator, "ROOT", self.root)

    def tearDown(self) -> None:
        setattr(validator, "ROOT", self.original_root)
        self.temporary.cleanup()

    def rewrite_json(self, relative_path: str, mutate) -> None:
        path = self.root / relative_path
        document = json.loads(path.read_text(encoding="utf-8"))
        mutate(document)
        path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def test_accepts_empty_blueprint_tools_without_crashing(self) -> None:
        self.rewrite_json("examples/agent-blueprint.example.json", lambda document: document.__setitem__("tools", []))
        issues = validator.validate_json_and_schemas(self.json_files)
        self.assertFalse(
            any(
                issue.category == "schema" and issue.path == "examples/agent-blueprint.example.json"
                for issue in issues
            )
        )

    def test_reports_noninteger_population_without_crashing(self) -> None:
        self.rewrite_json(
            "examples/maturity-assessment.example.json",
            lambda document: document["sampling"].__setitem__("populationSize", "10"),
        )
        issues = validator.validate_json_and_schemas(self.json_files)
        self.assertTrue(any(issue.category == "schema" for issue in issues))

    def test_requires_catalog_last_reviewed(self) -> None:
        self.rewrite_json("controls/control-catalog.json", lambda document: document.pop("lastReviewed"))
        issues = validator.validate_json_and_schemas(self.json_files)
        self.assertTrue(
            any(
                issue.category == "schema"
                and issue.path == "controls/control-catalog.json"
                and "lastReviewed" in issue.message
                for issue in issues
            )
        )

    def test_rejects_duplicate_control_ids_at_repository_level(self) -> None:
        self.rewrite_json(
            "controls/control-catalog.json",
            lambda document: document["controls"].append(document["controls"][0].copy()),
        )
        issues = validator.validate_json_and_schemas(self.json_files)
        self.assertTrue(any(issue.category == "controls" and "duplicate IDs" in issue.message for issue in issues))


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
