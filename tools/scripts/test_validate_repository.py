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
        self.reset_json_tree()
        self.json_files = sorted(self.root.rglob("*.json"))
        setattr(validator, "ROOT", self.root)

    def reset_json_tree(self) -> None:
        for source in REPO_ROOT.rglob("*.json"):
            destination = self.root / source.relative_to(REPO_ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    def tearDown(self) -> None:
        setattr(validator, "ROOT", self.original_root)
        self.temporary.cleanup()

    def rewrite_json(self, relative_path: str, mutate) -> None:
        path = self.root / relative_path
        document = json.loads(path.read_text(encoding="utf-8"))
        mutate(document)
        path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def write_json_value(self, relative_path: str, value) -> None:
        path = self.root / relative_path
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

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

    def test_reports_schema_invalid_nested_types_without_crashing(self) -> None:
        cases = (
            ("examples/agent-blueprint.example.json", "tools", None),
            ("examples/agent-blueprint.example.json", "tools", {}),
            ("examples/agent-blueprint.example.json", "tools", "invalid"),
            ("examples/agent-blueprint.example.json", "governance", None),
            ("examples/agent-blueprint.example.json", "governance", []),
            ("examples/agent-blueprint.example.json", "governance", "invalid"),
            ("examples/maturity-assessment.example.json", "review", None),
            ("examples/maturity-assessment.example.json", "review", []),
            ("examples/maturity-assessment.example.json", "review", "invalid"),
            ("examples/maturity-assessment.example.json", "evidenceRegister", None),
            ("examples/maturity-assessment.example.json", "evidenceRegister", {}),
            ("examples/maturity-assessment.example.json", "evidenceRegister", "invalid"),
            ("examples/maturity-assessment.example.json", "sampling", None),
            ("examples/maturity-assessment.example.json", "sampling", []),
            ("examples/maturity-assessment.example.json", "sampling", "invalid"),
            ("examples/agent-registry.example.json", "deployment", None),
            ("examples/agent-registry.example.json", "deployment", []),
            ("examples/agent-registry.example.json", "deployment", "invalid"),
            ("examples/agent-registry.example.json", "attestation", None),
            ("examples/agent-registry.example.json", "attestation", []),
            ("examples/agent-registry.example.json", "attestation", "invalid"),
            ("controls/control-catalog.json", "controls", None),
            ("controls/control-catalog.json", "controls", {}),
            ("controls/control-catalog.json", "controls", "invalid"),
        )
        for relative_path, field, invalid_value in cases:
            with self.subTest(path=relative_path, field=field, value=invalid_value):
                self.reset_json_tree()
                self.rewrite_json(
                    relative_path,
                    lambda document, key=field, value=invalid_value: document.__setitem__(key, value),
                )
                issues = validator.validate_json_and_schemas(self.json_files)
                self.assertTrue(
                    any(issue.category == "schema" and issue.path == relative_path for issue in issues)
                )

    def test_reports_schema_invalid_top_level_values_without_crashing(self) -> None:
        records = (
            "examples/agent-registry.example.json",
            "examples/agent-blueprint.example.json",
            "examples/control-catalog.example.json",
            "controls/control-catalog.json",
            "examples/maturity-assessment.example.json",
        )
        for relative_path in records:
            for invalid_value in (None, [], "invalid"):
                with self.subTest(path=relative_path, value=invalid_value):
                    self.reset_json_tree()
                    self.write_json_value(relative_path, invalid_value)
                    issues = validator.validate_json_and_schemas(self.json_files)
                    self.assertTrue(
                        any(issue.category == "schema" and issue.path == relative_path for issue in issues)
                    )

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

    def test_accepts_all_canonical_governance_contract_examples(self) -> None:
        issues = validator.validate_json_and_schemas(self.json_files)
        contract_issues = [issue for issue in issues if issue.category != "json-reference"]
        self.assertEqual([], contract_issues)

    def test_rejects_unknown_model_catalog_binding(self) -> None:
        self.rewrite_json(
            "examples/agent-blueprint.example.json",
            lambda document: document["models"][0].__setitem__(
                "catalogEntryId", "MPC-NOT-CATALOGED-999"
            ),
        )
        issues = validator.validate_json_and_schemas(self.json_files)
        self.assertTrue(
            any(
                issue.category == "cross-record"
                and "unknown catalogEntryId MPC-NOT-CATALOGED-999" in issue.message
                for issue in issues
            )
        )

    def test_rejects_release_manifest_governance_mismatch(self) -> None:
        self.rewrite_json(
            "examples/release-evidence-manifest.example.json",
            lambda document: document.__setitem__("riskTier", "T4"),
        )
        issues = validator.validate_json_and_schemas(self.json_files)
        self.assertTrue(
            any(
                issue.category == "cross-record"
                and "manifest and blueprint risk tier values differ" in issue.message
                for issue in issues
            )
        )

    def test_rejects_release_manifest_artifact_hash_mismatch(self) -> None:
        self.rewrite_json(
            "examples/release-evidence-manifest.example.json",
            lambda document: document["artifactHashes"][0].__setitem__("sha256", "0" * 64),
        )
        issues = validator.validate_json_and_schemas(self.json_files)
        self.assertTrue(
            any(
                issue.category == "cross-record"
                and "artifact hash mismatch" in issue.message
                for issue in issues
            )
        )

    def test_requires_control_automation_mode(self) -> None:
        self.rewrite_json(
            "controls/control-catalog.json",
            lambda document: document["controls"][0].pop("automation"),
        )
        issues = validator.validate_json_and_schemas(self.json_files)
        self.assertTrue(
            any(
                issue.category == "schema"
                and issue.path == "controls/control-catalog.json"
                and "automation" in issue.message
                for issue in issues
            )
        )


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


class TierTaxonomyTests(unittest.TestCase):
    """ADR-0009: T1-T4 is the canonical risk-tier taxonomy."""

    def setUp(self) -> None:
        self.original_root = getattr(validator, "ROOT")
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        for source in REPO_ROOT.rglob("*.json"):
            destination = self.root / source.relative_to(REPO_ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        setattr(validator, "ROOT", self.root)

    def tearDown(self) -> None:
        setattr(validator, "ROOT", self.original_root)
        self.temporary.cleanup()

    def rewrite_json(self, relative_path: str, mutate) -> None:
        path = self.root / relative_path
        document = json.loads(path.read_text(encoding="utf-8"))
        mutate(document)
        path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def test_accepts_canonical_taxonomy(self) -> None:
        self.assertEqual([], validator.validate_tier_taxonomy())

    def test_rejects_extra_tier_in_registry_schema(self) -> None:
        self.rewrite_json(
            "schemas/agent-registry.schema.json",
            lambda document: document["$defs"]["risk"]["properties"]["tier"].__setitem__(
                "enum", ["T0", "T1", "T2", "T3", "T4"]
            ),
        )
        issues = validator.validate_tier_taxonomy()
        self.assertTrue(any(issue.category == "tier-taxonomy" for issue in issues))

    def test_rejects_extra_tier_in_blueprint_schema(self) -> None:
        self.rewrite_json(
            "schemas/agent-blueprint.schema.json",
            lambda document: document["properties"]["governance"]["properties"]["riskTier"].__setitem__(
                "enum", ["T1", "T2", "T3", "T4", "T5"]
            ),
        )
        issues = validator.validate_tier_taxonomy()
        self.assertTrue(any(issue.category == "tier-taxonomy" for issue in issues))

    def test_rejects_non_canonical_tier_in_control(self) -> None:
        self.rewrite_json(
            "controls/control-catalog.json",
            lambda document: document["controls"][0].__setitem__("appliesToTiers", ["T0", "T1"]),
        )
        issues = validator.validate_tier_taxonomy()
        self.assertTrue(
            any(issue.category == "tier-taxonomy" and "T0" in issue.message for issue in issues)
        )

    def test_reports_missing_schema(self) -> None:
        (self.root / "schemas/control-catalog.schema.json").unlink()
        issues = validator.validate_tier_taxonomy()
        self.assertTrue(any(issue.category == "tier-taxonomy" for issue in issues))

    def test_accepts_current_control_scopes(self) -> None:
        self.assertEqual([], validator.validate_control_scope())

    def test_rejects_blocking_organization_control(self) -> None:
        def promote(document):
            for control in document["controls"]:
                if control.get("scope") == "organization":
                    control["blocking"] = True
                    return
            raise AssertionError("catalog has no organization-scoped control")

        self.rewrite_json("controls/control-catalog.json", promote)
        issues = validator.validate_control_scope()
        self.assertTrue(any(issue.category == "control-scope" for issue in issues))


class CaseBundleTests(unittest.TestCase):
    """A second reference case must be verified by the same rules as the first."""

    def setUp(self) -> None:
        self.original_root = getattr(validator, "ROOT")
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        for source in REPO_ROOT.rglob("*.json"):
            destination = self.root / source.relative_to(REPO_ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        setattr(validator, "ROOT", self.root)
        self.case = "examples/cases/demo-case"

    def tearDown(self) -> None:
        setattr(validator, "ROOT", self.original_root)
        self.temporary.cleanup()

    def seed_case(self, mutate_registry=None, mutate_blueprint=None) -> list[Path]:
        """Copy the canonical case into examples/cases/demo-case, optionally corrupted."""
        registry = json.loads((self.root / "examples/agent-registry.example.json").read_text(encoding="utf-8"))
        blueprint = json.loads((self.root / "examples/agent-blueprint.example.json").read_text(encoding="utf-8"))
        registry["currentBlueprint"]["path"] = f"{self.case}/blueprint.json"
        if mutate_registry:
            mutate_registry(registry)
        if mutate_blueprint:
            mutate_blueprint(blueprint)
        target = self.root / self.case
        target.mkdir(parents=True, exist_ok=True)
        for name, document in (("registry.json", registry), ("blueprint.json", blueprint)):
            (target / name).write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        for role_file, source in (
            ("model-catalog.json", "examples/model-provider-catalog.example.json"),
            ("source-catalog.json", "examples/certified-source-catalog.example.json"),
            ("tool-catalog.json", "examples/enterprise-tool-registry.example.json"),
        ):
            shutil.copy2(self.root / source, target / role_file)
        return sorted(self.root.rglob("*.json"))

    def case_issues(self, issues) -> list:
        return [issue for issue in issues if issue.category == "cross-record" and self.case in issue.path]

    def test_discovers_flat_and_directory_bundles(self) -> None:
        json_files = self.seed_case()
        parsed = {validator.relative(path): validator.load_json(path) for path in json_files}
        bundles = validator.discover_case_bundles(parsed)
        labels = {bundle.get("caseLabel") for bundle in bundles}
        self.assertIn("examples", labels)
        self.assertIn(self.case, labels)

    def test_accepts_consistent_case_bundle(self) -> None:
        json_files = self.seed_case()
        self.assertEqual([], self.case_issues(validator.validate_json_and_schemas(json_files)))

    def test_rejects_tier_mismatch_inside_a_case(self) -> None:
        json_files = self.seed_case(
            mutate_blueprint=lambda document: document["governance"].__setitem__("riskTier", "T3")
        )
        issues = validator.validate_json_and_schemas(json_files)
        self.assertTrue(
            any("risk tier values differ" in issue.message for issue in self.case_issues(issues))
        )

    def test_rejects_unknown_catalog_binding_inside_a_case(self) -> None:
        json_files = self.seed_case(
            mutate_blueprint=lambda document: document["tools"][0].__setitem__(
                "catalogEntryId", "TLR-NOT-CATALOGED-999"
            )
        )
        issues = validator.validate_json_and_schemas(json_files)
        self.assertTrue(
            any("TLR-NOT-CATALOGED-999" in issue.message for issue in self.case_issues(issues))
        )

    def test_rejects_schema_invalid_record_inside_a_case(self) -> None:
        json_files = self.seed_case(mutate_registry=lambda document: document.pop("ownership"))
        issues = validator.validate_json_and_schemas(json_files)
        self.assertTrue(
            any(
                issue.category == "schema" and issue.path == f"{self.case}/registry.json"
                for issue in issues
            )
        )

    def test_case_failures_do_not_blame_the_canonical_example(self) -> None:
        json_files = self.seed_case(
            mutate_blueprint=lambda document: document["governance"].__setitem__("riskTier", "T3")
        )
        issues = validator.validate_json_and_schemas(json_files)
        self.assertEqual(
            [],
            [
                issue
                for issue in issues
                if issue.category == "cross-record" and issue.path == "examples"
            ],
        )


class TierLabelTests(unittest.TestCase):
    """ADR-0009 in prose: a tier column says T1-T4, not baixo/moderado/alto/critico."""

    def setUp(self) -> None:
        self.original_root = getattr(validator, "ROOT")
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        setattr(validator, "ROOT", self.root)

    def tearDown(self) -> None:
        setattr(validator, "ROOT", self.original_root)
        self.temporary.cleanup()

    def write(self, relative_path: str, body: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        return path

    def test_accepts_canonical_tier_labels(self) -> None:
        path = self.write(
            "docs/identity/README.md",
            "| Tier | Controle |\n|---|---|\n| T1 — baixo | scopes documentados |\n",
        )
        self.assertEqual([], validator.validate_tier_labels([path]))

    def test_rejects_prose_tier_label_in_first_column(self) -> None:
        path = self.write(
            "docs/identity/README.md",
            "| Tier | Controle |\n|---|---|\n| moderado | workload identity |\n",
        )
        issues = validator.validate_tier_labels([path])
        self.assertTrue(
            any(issue.category == "tier-taxonomy" and "moderado" in issue.message for issue in issues)
        )

    def test_allows_prose_word_outside_the_first_column(self) -> None:
        path = self.write(
            "docs/registry/discovery-and-forecast.md",
            "| Ação | Confiança |\n|---|---|\n| aprovar T1 | baixo |\n",
        )
        self.assertEqual([], validator.validate_tier_labels([path]))

    def test_skips_historical_policy(self) -> None:
        path = self.write(
            "docs/governance/ai-agent-policy-and-governance-v1.md",
            "| Tier | Controle |\n|---|---|\n| alto | revisão reforçada |\n",
        )
        self.assertEqual([], validator.validate_tier_labels([path]))

    def test_canonical_corpus_has_no_prose_tier_labels(self) -> None:
        setattr(validator, "ROOT", self.original_root)
        markdown = [path for path in validator.repository_files() if path.suffix == ".md"]
        self.assertEqual([], validator.validate_tier_labels(markdown))


class GovernanceContractV2Tests(unittest.TestCase):
    """Approved spec 002: structured governance contracts are explicit and versioned."""

    def load_json(self, relative_path: str):
        return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))

    def test_registry_v2_separates_lifecycle_operation_and_discovery(self) -> None:
        schema = self.load_json("schemas/agent-registry.schema.json")
        self.assertEqual("2.0", schema["properties"]["schemaVersion"]["const"])
        lifecycle = schema["$defs"]["lifecycle"]
        self.assertTrue({"stage", "operationalState", "transitionHistory"} <= set(lifecycle["required"]))
        self.assertTrue({"stage", "operationalState", "transitionHistory"} <= set(lifecycle["properties"]))
        discovery = schema["properties"]["discovery"]
        self.assertTrue({"status", "confidence", "signals"} <= set(discovery["required"]))
        self.assertEqual(
            ["confirmed", "probable", "suspected"],
            discovery["properties"]["status"]["enum"],
        )

    def test_blueprint_v2_requires_governed_model_source_and_tool_bindings(self) -> None:
        schema = self.load_json("schemas/agent-blueprint.schema.json")
        self.assertEqual("2.0", schema["properties"]["schemaVersion"]["const"])
        model = schema["properties"]["models"]["items"]
        self.assertTrue(
            {"modelVersion", "catalogEntryId", "evaluationRef"} <= set(model["required"])
        )
        source = schema["properties"]["data"]["properties"]["sources"]["items"]
        self.assertIn("catalogEntryId", source["required"])
        tool = schema["properties"]["tools"]["items"]
        self.assertIn("catalogEntryId", tool["required"])
        governance = schema["properties"]["governance"]
        self.assertTrue({"riskTier", "admissibility", "admissibilityRationale"} <= set(governance["required"]))
        self.assertEqual(
            ["permitted", "conditional", "restricted", "prohibited"],
            governance["properties"]["admissibility"]["enum"],
        )

    def test_control_catalog_breaking_contract_is_schema_v2(self) -> None:
        schema = self.load_json("schemas/control-catalog.schema.json")
        self.assertEqual("2.0", schema["properties"]["schemaVersion"]["const"])
        control_required = set(schema["$defs"]["control"]["required"])
        self.assertTrue({"automation", "frameworkMappings"} <= control_required)
        self.assertNotIn("schemaVersion", set(schema) - {"properties"})

    def test_reference_contracts_have_schemas_and_examples(self) -> None:
        pairs = (
            ("schemas/model-provider-catalog.schema.json", "examples/model-provider-catalog.example.json"),
            ("schemas/certified-source-catalog.schema.json", "examples/certified-source-catalog.example.json"),
            ("schemas/enterprise-tool-registry.schema.json", "examples/enterprise-tool-registry.example.json"),
            ("schemas/release-evidence-manifest.schema.json", "examples/release-evidence-manifest.example.json"),
            ("schemas/audit-event.schema.json", "examples/audit-event.example.json"),
        )
        for schema_path, example_path in pairs:
            with self.subTest(schema=schema_path, example=example_path):
                self.assertTrue((REPO_ROOT / schema_path).is_file())
                self.assertTrue((REPO_ROOT / example_path).is_file())


if __name__ == "__main__":
    unittest.main()
