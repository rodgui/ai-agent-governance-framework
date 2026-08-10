from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "docs/governance/ai-agent-policy-and-governance-v1.md"
POLICY_V1_SHA256 = "cdd8c232019a4b388ebb71d7f1dd82f3c568d039d416beab1838ee59f4047140"
EXCLUDED_DIRS = {".git", ".venv", "venv", "dist", "__pycache__", ".pytest_cache", ".ruff_cache"}
TEXT_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml", ".toml", ".txt"}
INLINE_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
CITATION_RE = re.compile(r"(?<!\!)\[(\d+)\]")
VENDOR_NAME_RE = re.compile(
    r"\b(?:Microsoft|Agent 365|Cloudflare|Azure|Copilot|Purview|Key Vault"
    r"|Entra (?:ID|Agent ID|Suite)|Defender (?:XDR|for Cloud|for Endpoint|for Identity|for Office 365))\b",
    flags=re.IGNORECASE,
)
STRUCTURED_VENDOR_NAME_RE = re.compile(
    r"\b(?:Microsoft|Agent 365|Cloudflare|Azure|Copilot|Entra|Purview|Defender|Key Vault)\b",
    flags=re.IGNORECASE,
)
LEGACY_POLICY_TEMPLATE_RE = re.compile(
    r"(?:\bPolicy\s+V1\b|Self-Assessment Form\s+—\s+AI Agents\s+\(V1\)"
    r"|AI Agent Publication Checklist\s+\(V1\))",
    flags=re.IGNORECASE,
)
ALLOWED_VENDOR_LITERALS = {
    ".github/workflows/quality-gates.yml": (
        "docs/explanations/diagrams/microsoft-customer-zero-agent-governance.png",
    ),
}
CANONICAL_TIERS = ("T1", "T2", "T3", "T4")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REPOSITORY_REF_RE = re.compile(
    r"^[A-Za-z0-9._/-]+\.(?:md|json|yaml|yml|png)(?:#[A-Za-z0-9._~!$&'()*+,;=:@/?%-]*)?$"
)
ALLOWED_STATUSES = {
    "accepted",
    "adopted",
    "approved",
    "completed",
    "deprecated",
    "draft",
    "in-progress",
    "maintained",
    "review",
    "stable",
    "superseded",
    "validated",
}


@dataclass(frozen=True)
class Issue:
    category: str
    path: str
    message: str


def relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def repository_files() -> list[Path]:
    files: list[Path] = []
    for current, dirs, names in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED_DIRS)
        base = Path(current)
        for name in sorted(names):
            files.append(base / name)
    return files


def parse_frontmatter(path: Path, text: str) -> tuple[dict[str, str], list[Issue]]:
    issues: list[Issue] = []
    if not text.startswith("---\n"):
        return {}, issues
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, [Issue("frontmatter", relative(path), "opening delimiter has no closing delimiter")]
    metadata: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw or raw.startswith(" ") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata, issues


def requires_frontmatter(path: Path) -> bool:
    rel = relative(path)
    exact = {
        "docs/fundamentals/README.md",
        "docs/governance/policy.md",
        "docs/governance/operating-model.md",
        "docs/architecture/overview.md",
        "docs/executive/governing-agents-at-scale.md",
        "consulting/README.md",
        "consulting/consulting-engagement-model.md",
        "docs/explanations/microsoft-agent-governance-case-study.md",
        "docs/guides/framework-implementation-playbook.md",
        "docs/guides/implementation-plan-90-days.md",
        "docs/guides/maturity-model.md",
        "docs/handbook/README.md",
    }
    domain_readmes = {
        "docs/adoption/README.md",
        "docs/auditability/README.md",
        "docs/data-access/README.md",
        "docs/evaluations/README.md",
        "docs/human-oversight/README.md",
        "docs/identity/README.md",
        "docs/lifecycle/README.md",
        "docs/model-governance/README.md",
        "docs/operations/README.md",
        "docs/registry/README.md",
        "docs/responsible-ai/README.md",
        "docs/risk-management/README.md",
        "docs/security/README.md",
        "docs/tool-governance/README.md",
        "docs/value/README.md",
    }
    return (
        rel in exact
        or rel in domain_readmes
        or rel.startswith("docs/patterns/")
        or rel.startswith("docs/architecture/decisions/") and path.name != "README.md"
        or rel.startswith("specs/001-handbook-consulting-product/")
    )


def validate_frontmatter(markdown_files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        metadata, parse_issues = parse_frontmatter(path, text)
        issues.extend(parse_issues)
        if not requires_frontmatter(path):
            continue
        if not metadata:
            issues.append(Issue("frontmatter", relative(path), "canonical document is missing front matter"))
            continue
        for key in ("title", "status", "last_reviewed"):
            if not metadata.get(key):
                issues.append(Issue("frontmatter", relative(path), f"missing required key: {key}"))
        status = metadata.get("status", "")
        if status and status not in ALLOWED_STATUSES:
            issues.append(Issue("frontmatter", relative(path), f"unknown status: {status}"))
        reviewed = metadata.get("last_reviewed", "")
        if reviewed and not DATE_RE.match(reviewed):
            issues.append(Issue("frontmatter", relative(path), f"invalid last_reviewed date: {reviewed}"))
    return issues


def frontmatter_related_values(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---\n", 4)
    if end < 0:
        return []
    values: list[str] = []
    in_related = False
    for raw in text[4:end].splitlines():
        if raw == "related:":
            in_related = True
            continue
        if not in_related:
            continue
        if raw and not raw.startswith(" "):
            break
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("- "):
            value = stripped[2:]
        elif ":" in stripped:
            _, value = stripped.split(":", 1)
        else:
            continue
        value = value.strip().strip('"').strip("'")
        if value and value not in {"null", "[]", "{}"}:
            values.append(value)
    return values


def validate_frontmatter_related_paths(markdown_files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw_target in frontmatter_related_values(text):
            if "://" in raw_target or raw_target.startswith(("mailto:", "#")):
                continue
            target = raw_target.split("#", 1)[0]
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                issues.append(Issue("frontmatter-related", relative(path), f"target does not exist: {raw_target}"))
            elif not has_exact_case(candidate):
                issues.append(Issue("frontmatter-related", relative(path), f"path casing does not match filesystem: {raw_target}"))
    return issues


def extract_link_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        return raw[1 : raw.index(">")]
    return raw.split(maxsplit=1)[0]


def has_exact_case(path: Path) -> bool:
    try:
        parts = path.resolve(strict=False).relative_to(ROOT.resolve()).parts
    except ValueError:
        return False
    current = ROOT.resolve()
    for part in parts:
        try:
            names = {entry.name for entry in current.iterdir()}
        except OSError:
            return False
        if part not in names:
            return False
        current /= part
    return True


def validate_markdown_links(markdown_files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for match in INLINE_LINK_RE.finditer(text):
            target = extract_link_target(match.group(1))
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#")):
                continue
            clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not clean:
                continue
            candidate = (ROOT / clean.lstrip("/")) if clean.startswith("/") else (path.parent / clean)
            candidate = Path(os.path.normpath(candidate))
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                issues.append(Issue("link", relative(path), f"local link escapes repository: {target}"))
                continue
            if not candidate.exists():
                issues.append(Issue("link", relative(path), f"missing local target: {target}"))
            elif not has_exact_case(candidate):
                issues.append(Issue("link", relative(path), f"path casing mismatch: {target}"))
    return issues


def validate_citations(markdown_files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        marker = "## Sources"
        if marker not in text:
            continue
        body, sources = text.rsplit(marker, 1)
        cited = set(CITATION_RE.findall(body))
        listed = set(CITATION_RE.findall(sources))
        missing = sorted(cited - listed, key=int)
        if missing:
            issues.append(Issue("citations", relative(path), f"citations missing from Sources block: {', '.join(missing)}"))
    return issues


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_json_strings(value: Any, location: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from iter_json_strings(child, f"{location}/{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_json_strings(child, f"{location}/{index}")
    elif isinstance(value, str):
        yield location, value


def validate_json_references(parsed: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    for source, document in parsed.items():
        for location, reference in iter_json_strings(document):
            if not REPOSITORY_REF_RE.fullmatch(reference):
                continue
            clean_reference = reference.split("#", 1)[0]
            candidate = Path(os.path.normpath(ROOT / clean_reference))
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                issues.append(Issue("json-reference", source, f"{location}: path escapes repository: {reference}"))
                continue
            if not candidate.exists():
                issues.append(Issue("json-reference", source, f"{location}: missing repository target: {reference}"))
            elif not has_exact_case(candidate):
                issues.append(Issue("json-reference", source, f"{location}: path casing mismatch: {reference}"))
    return issues


def validate_cross_record_invariants(parsed: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    registry = parsed.get("examples/agent-registry.example.json")
    blueprint = parsed.get("examples/agent-blueprint.example.json")
    if isinstance(registry, dict) and isinstance(blueprint, dict):
        if registry.get("agentId") != blueprint.get("agentId"):
            issues.append(Issue("cross-record", "examples", "registry and blueprint agentId values differ"))
        current = registry.get("currentBlueprint", {})
        if isinstance(current, dict):
            if current.get("path") != "examples/agent-blueprint.example.json":
                issues.append(Issue("cross-record", "examples/agent-registry.example.json", "currentBlueprint.path does not identify the canonical example blueprint"))
            if current.get("version") != blueprint.get("version"):
                issues.append(Issue("cross-record", "examples", "registry and blueprint version values differ"))

    if isinstance(registry, dict):
        lifecycle = registry.get("lifecycle", {})
        platforms = registry.get("platforms", [])
        status = lifecycle.get("status") if isinstance(lifecycle, dict) else None
        production = any(
            isinstance(platform, dict) and platform.get("environment") == "production"
            for platform in platforms
        )
        release_relevant = status in {"conditional", "approved", "active"} or production
        if release_relevant and not registry.get("evidenceLinks"):
            issues.append(
                Issue(
                    "cross-record",
                    "examples/agent-registry.example.json",
                    "release-relevant registry record has no evidenceLinks",
                )
            )
        attestation = registry.get("attestation", {})
        if release_relevant and isinstance(attestation, dict):
            attested_at = attestation.get("attestedAt")
            expires_at = attestation.get("expiresAt")
            last_reviewed = registry.get("lastReviewed")
            if isinstance(attested_at, str) and isinstance(expires_at, str) and attested_at > expires_at:
                issues.append(
                    Issue(
                        "cross-record",
                        "examples/agent-registry.example.json",
                        "attestation expires before it was issued",
                    )
                )
            if isinstance(expires_at, str) and isinstance(last_reviewed, str) and expires_at < last_reviewed:
                issues.append(
                    Issue(
                        "cross-record",
                        "examples/agent-registry.example.json",
                        "attestation expires before lastReviewed",
                    )
                )

    assessment_path = "examples/maturity-assessment.example.json"
    assessment = parsed.get(assessment_path)
    if isinstance(assessment, dict):
        evidence = assessment.get("evidenceRegister", [])
        evidence_ids: list[str] = []
        for item in evidence:
            if isinstance(item, dict) and isinstance(item.get("id"), str):
                evidence_ids.append(item["id"])
        duplicates = sorted({item for item in evidence_ids if evidence_ids.count(item) > 1})
        if duplicates:
            issues.append(Issue("cross-record", assessment_path, f"duplicate evidence IDs: {duplicates}"))
        known = set(evidence_ids)
        dimensions = assessment.get("dimensions", {})
        if isinstance(dimensions, dict):
            for name, dimension in dimensions.items():
                if not isinstance(dimension, dict):
                    continue
                unknown = sorted(set(dimension.get("evidenceRefs", [])) - known)
                if unknown:
                    issues.append(
                        Issue(
                            "cross-record",
                            assessment_path,
                            f"dimensions/{name}: unknown evidence refs: {unknown}",
                        )
                    )
        assessor = assessment.get("assessor", {})
        reviewer = assessment.get("review", {}).get("reviewer", {})
        if isinstance(assessor, dict) and isinstance(reviewer, dict):
            same_name = assessor.get("name") == reviewer.get("name")
            same_org = assessor.get("organization") == reviewer.get("organization")
            if same_name and same_org:
                issues.append(Issue("cross-record", assessment_path, "assessor and reviewer must not be the same identity"))
        sampling = assessment.get("sampling", {})
        if isinstance(sampling, dict):
            population = sampling.get("populationSize")
            sample = sampling.get("sampleSize")
            if isinstance(population, int) and isinstance(sample, int) and sample > population:
                issues.append(Issue("cross-record", assessment_path, "sampleSize exceeds populationSize"))
    return issues


def validate_json_and_schemas(json_files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    parsed: dict[str, Any] = {}
    for path in json_files:
        try:
            parsed[relative(path)] = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            issues.append(Issue("json", relative(path), str(exc)))

    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        return issues + [Issue("dependency", "jsonschema", "install jsonschema>=4.22,<5")]

    pairs = [
        ("schemas/agent-registry.schema.json", "examples/agent-registry.example.json"),
        ("schemas/agent-blueprint.schema.json", "examples/agent-blueprint.example.json"),
        ("schemas/control-catalog.schema.json", "examples/control-catalog.example.json"),
        ("schemas/control-catalog.schema.json", "controls/control-catalog.json"),
        ("schemas/maturity-assessment.schema.json", "examples/maturity-assessment.example.json"),
    ]
    missing_instance = object()
    schema_invalid_instances: set[str] = set()
    for schema_rel, instance_rel in pairs:
        schema = parsed.get(schema_rel)
        instance = parsed.get(instance_rel, missing_instance)
        if not isinstance(schema, dict) or instance is missing_instance:
            continue
        try:
            Draft202012Validator.check_schema(schema)
            validator = Draft202012Validator(schema, format_checker=FormatChecker())
            schema_errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
            if schema_errors:
                schema_invalid_instances.add(instance_rel)
            for error in schema_errors:
                location = "/".join(str(part) for part in error.path) or "$"
                issues.append(Issue("schema", instance_rel, f"{location}: {error.message}"))
        except Exception as exc:  # schema-library errors have heterogeneous types
            schema_invalid_instances.add(instance_rel)
            issues.append(Issue("schema", schema_rel, str(exc)))

    schema_valid_records = {
        relative_path: value
        for relative_path, value in parsed.items()
        if relative_path not in schema_invalid_instances
    }
    issues.extend(validate_json_references(parsed))
    issues.extend(validate_cross_record_invariants(schema_valid_records))

    guardrail_cases: list[tuple[str, Any, str]] = []
    registry_example = schema_valid_records.get("examples/agent-registry.example.json")
    if isinstance(registry_example, dict):
        without_attestation = copy.deepcopy(registry_example)
        without_attestation.pop("attestation", None)
        guardrail_cases.append(
            (
                "schemas/agent-registry.schema.json",
                without_attestation,
                "active or production registry record without attestation was accepted",
            )
        )
        without_evidence = copy.deepcopy(registry_example)
        without_evidence.pop("evidenceLinks", None)
        guardrail_cases.append(
            (
                "schemas/agent-registry.schema.json",
                without_evidence,
                "active or production registry record without evidenceLinks was accepted",
            )
        )
    blueprint_example = schema_valid_records.get("examples/agent-blueprint.example.json")
    if isinstance(blueprint_example, dict):
        without_release_evidence = copy.deepcopy(blueprint_example)
        without_release_evidence.get("governance", {}).pop("releaseEvidenceRef", None)
        guardrail_cases.append(
            (
                "schemas/agent-blueprint.schema.json",
                without_release_evidence,
                "production blueprint without release evidence was accepted",
            )
        )
        empty_release_evidence = copy.deepcopy(blueprint_example)
        empty_governance = empty_release_evidence.get("governance", {})
        if isinstance(empty_governance, dict):
            empty_governance["releaseEvidenceRef"] = ""
            empty_governance["assessmentRefs"] = []
            guardrail_cases.append(
                (
                    "schemas/agent-blueprint.schema.json",
                    empty_release_evidence,
                    "production blueprint with empty release and assessment references was accepted",
                )
            )
        create_marked_read_only = copy.deepcopy(blueprint_example)
        for tool in create_marked_read_only.get("tools", []):
            if isinstance(tool, dict) and tool.get("class") == "create":
                tool["stateChanging"] = False
                guardrail_cases.append(
                    (
                        "schemas/agent-blueprint.schema.json",
                        create_marked_read_only,
                        "create tool marked as non-state-changing was accepted",
                    )
                )
                break
        unsafe_tool = copy.deepcopy(blueprint_example)
        unsafe_tools = unsafe_tool.get("tools", [])
        if isinstance(unsafe_tools, list) and unsafe_tools and isinstance(unsafe_tools[0], dict):
            first_tool = unsafe_tools[0]
            first_tool.update(
                {
                    "class": "delete",
                    "stateChanging": True,
                    "reversible": False,
                    "approvalMode": "automated",
                }
            )
            guardrail_cases.append(
                (
                    "schemas/agent-blueprint.schema.json",
                    unsafe_tool,
                    "irreversible automated state-changing tool was accepted",
                )
            )
        empty_enforcement_refs = copy.deepcopy(blueprint_example)
        empty_governance = empty_enforcement_refs.get("governance", {})
        empty_tools = empty_enforcement_refs.get("tools", [])
        if isinstance(empty_governance, dict) and empty_tools and isinstance(empty_tools[0], dict):
            empty_governance["riskTier"] = "T4"
            empty_tools[0].update(
                {
                    "class": "delete",
                    "stateChanging": True,
                    "reversible": False,
                    "approvalMode": "human",
                    "gatewayRef": "",
                    "killSwitchRef": "",
                    "scopes": [],
                }
            )
            guardrail_cases.append(
                (
                    "schemas/agent-blueprint.schema.json",
                    empty_enforcement_refs,
                    "T4 state-changing tool with empty enforcement references was accepted",
                )
            )
    maturity_example = schema_valid_records.get("examples/maturity-assessment.example.json")
    if isinstance(maturity_example, dict):
        without_review = copy.deepcopy(maturity_example)
        without_review.pop("review", None)
        guardrail_cases.append(
            (
                "schemas/maturity-assessment.schema.json",
                without_review,
                "maturity assessment without reviewer disposition was accepted",
            )
        )
    for schema_rel, invalid_instance, message in guardrail_cases:
        schema = parsed.get(schema_rel)
        if not isinstance(schema, dict):
            continue
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        if not any(validator.iter_errors(invalid_instance)):
            issues.append(Issue("schema-guardrail", schema_rel, message))

    invariant_guardrails: list[tuple[dict[str, Any], str]] = []
    if isinstance(maturity_example, dict):
        unknown_evidence = copy.deepcopy(maturity_example)
        unknown_dimensions = unknown_evidence.get("dimensions", {})
        if isinstance(unknown_dimensions, dict) and unknown_dimensions:
            first_dimension = next(iter(unknown_dimensions.values()))
            if isinstance(first_dimension, dict):
                first_dimension["evidenceRefs"] = ["EV-NONEXISTENT"]
                invariant_guardrails.append((unknown_evidence, "unknown evidence refs"))

        same_reviewer = copy.deepcopy(maturity_example)
        assessor = same_reviewer.get("assessor", {})
        review = same_reviewer.get("review", {})
        if isinstance(assessor, dict) and isinstance(review, dict):
            review["reviewer"] = {
                "name": assessor.get("name"),
                "role": assessor.get("role"),
                "organization": assessor.get("organization"),
            }
            invariant_guardrails.append((same_reviewer, "assessor and reviewer must not be the same identity"))

        invalid_sample = copy.deepcopy(maturity_example)
        sampling = invalid_sample.get("sampling", {})
        population = sampling.get("populationSize") if isinstance(sampling, dict) else None
        if isinstance(population, int) and not isinstance(population, bool):
            sampling["sampleSize"] = population + 1
            invariant_guardrails.append((invalid_sample, "sampleSize exceeds populationSize"))

    for invalid_assessment, expected_message in invariant_guardrails:
        records = dict(schema_valid_records)
        records["examples/maturity-assessment.example.json"] = invalid_assessment
        observed = validate_cross_record_invariants(records)
        if not any(expected_message in issue.message for issue in observed):
            issues.append(
                Issue(
                    "invariant-guardrail",
                    "schemas/maturity-assessment.schema.json",
                    f"mutation was not rejected: {expected_message}",
                )
            )

    if isinstance(registry_example, dict):
        expired_attestation = copy.deepcopy(registry_example)
        attestation = expired_attestation.get("attestation", {})
        if isinstance(attestation, dict):
            attestation["expiresAt"] = "2000-01-01"
            records = dict(schema_valid_records)
            records["examples/agent-registry.example.json"] = expired_attestation
            observed = validate_cross_record_invariants(records)
            if not any("attestation expires before lastReviewed" in issue.message for issue in observed):
                issues.append(
                    Issue(
                        "invariant-guardrail",
                        "schemas/agent-registry.schema.json",
                        "expired active attestation mutation was not rejected",
                    )
                )

    escaped_fragment = validate_json_references(
        {"guardrail": {"reference": "../outside.md#section"}}
    )
    if not any("path escapes repository" in issue.message for issue in escaped_fragment):
        issues.append(
            Issue(
                "json-reference-guardrail",
                "tools/scripts/validate-repository.py",
                "path traversal with a JSON reference fragment was not rejected",
            )
        )

    catalog = schema_valid_records.get("controls/control-catalog.json")
    blueprint = schema_valid_records.get("examples/agent-blueprint.example.json")
    if isinstance(catalog, dict):
        controls = catalog.get("controls", [])
        ids = [
            control["id"]
            for control in controls
            if isinstance(control, dict) and isinstance(control.get("id"), str)
        ]
        duplicate_ids = sorted({control_id for control_id in ids if ids.count(control_id) > 1})
        if duplicate_ids:
            issues.append(Issue("controls", "controls/control-catalog.json", f"duplicate IDs: {duplicate_ids}"))
        if len(ids) < 30:
            issues.append(Issue("controls", "controls/control-catalog.json", f"expected at least 30 controls, found {len(ids)}"))
        domains = {control.get("domain") for control in controls if isinstance(control, dict)}
        if len(domains) < 10:
            issues.append(Issue("controls", "controls/control-catalog.json", f"expected at least 10 domains, found {len(domains)}"))
        if isinstance(blueprint, dict):
            referenced = set(blueprint.get("governance", {}).get("controlIds", []))
            unknown = sorted(referenced - set(ids))
            if unknown:
                issues.append(Issue("controls", "examples/agent-blueprint.example.json", f"unknown control IDs: {unknown}"))
    return issues


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as stream:
        if stream.read(8) != b"\x89PNG\r\n\x1a\n":
            raise ValueError("invalid PNG signature")
        length = struct.unpack(">I", stream.read(4))[0]
        kind = stream.read(4)
        if kind != b"IHDR" or length < 8:
            raise ValueError("missing IHDR")
        return struct.unpack(">II", stream.read(8))


def validate_assets() -> list[Issue]:
    issues: list[Issue] = []
    expected = [
        ROOT / "docs/architecture/diagrams/ai-agent-governance-framework.png",
        ROOT / "docs/explanations/diagrams/microsoft-customer-zero-agent-governance.png",
    ]
    for path in expected:
        if not path.exists():
            issues.append(Issue("asset", relative(path), "required visual is missing"))
            continue
        try:
            dimensions = png_dimensions(path)
            if dimensions != (1800, 2400):
                issues.append(Issue("asset", relative(path), f"expected 1800x2400, found {dimensions[0]}x{dimensions[1]}"))
        except ValueError as exc:
            issues.append(Issue("asset", relative(path), str(exc)))
    old = ROOT / "docs/architecture/diagrams/agent-governance-operating-model.png"
    if old.exists():
        issues.append(Issue("asset", relative(old), "ambiguous vendor-specific legacy visual must not exist"))
    return issues


def validate_policy_integrity() -> list[Issue]:
    digest = hashlib.sha256(POLICY_PATH.read_bytes()).hexdigest()
    if digest != POLICY_V1_SHA256:
        return [Issue("policy-history", relative(POLICY_PATH), f"Historical Policy v1 changed: expected {POLICY_V1_SHA256}, found {digest}")]
    return []


def validate_tier_taxonomy() -> list[Issue]:
    """Enforce ADR-0004: T1-T4 is the canonical risk-tier taxonomy."""
    issues: list[Issue] = []
    enum_locations = [
        ("schemas/control-catalog.schema.json", ("$defs", "control", "properties", "appliesToTiers", "items")),
        ("schemas/agent-blueprint.schema.json", ("properties", "governance", "properties", "riskTier")),
        ("schemas/agent-registry.schema.json", ("$defs", "risk", "properties", "tier")),
    ]
    for rel, trail in enum_locations:
        path = ROOT / rel
        if not path.exists():
            issues.append(Issue("tier-taxonomy", rel, "schema declaring the tier enum is missing"))
            continue
        node: Any = load_json(path)
        for key in trail:
            if not isinstance(node, dict) or key not in node:
                node = None
                break
            node = node[key]
        found = node.get("enum") if isinstance(node, dict) else None
        if found != list(CANONICAL_TIERS):
            issues.append(
                Issue("tier-taxonomy", rel, f"tier enum must be {list(CANONICAL_TIERS)}, found {found}")
            )

    catalog_path = ROOT / "controls/control-catalog.json"
    if catalog_path.exists():
        catalog = load_json(catalog_path)
        controls = catalog.get("controls", []) if isinstance(catalog, dict) else []
        for control in controls:
            if not isinstance(control, dict):
                continue
            tiers = control.get("appliesToTiers")
            if not isinstance(tiers, list):
                continue
            unknown = sorted(str(tier) for tier in tiers if tier not in CANONICAL_TIERS)
            if unknown:
                issues.append(
                    Issue(
                        "tier-taxonomy",
                        relative(catalog_path),
                        f"{control.get('id', '<unknown>')} declares non-canonical tier(s): {', '.join(unknown)}",
                    )
                )
    return issues


def validate_commercial_boundary() -> list[Issue]:
    issues: list[Issue] = []
    legacy_paths = [
        "docs/executive/consulting-engagement-model.md",
        "templates/consulting-proposal-template.md",
    ]
    for item in legacy_paths:
        if (ROOT / item).exists():
            issues.append(Issue("boundary", item, "commercial artifact must live under consulting/"))

    model_path = ROOT / "consulting/consulting-engagement-model.md"
    packaging_path = ROOT / "consulting/README.md"
    if not model_path.exists() or not packaging_path.exists():
        return issues

    model = model_path.read_text(encoding="utf-8")
    packaging = packaging_path.read_text(encoding="utf-8")
    offers = re.findall(r"^## Oferta (\d+) — (.+)$", model, flags=re.MULTILINE)
    numbers = [int(number) for number, _ in offers]
    if numbers != list(range(1, 10)):
        issues.append(Issue("boundary", relative(model_path), "expected exactly nine ordered offer modules"))

    package_rows = re.findall(
        r"^\| \*\*([1-3])\.[^|]+\*\* \| [^|]+ \| ([^|]+) \|$",
        packaging,
        flags=re.MULTILINE,
    )
    if [number for number, _ in package_rows] != ["1", "2", "3"]:
        issues.append(Issue("boundary", relative(packaging_path), "expected exactly three ordered package rows"))
    module_cells = "\n".join(modules for _, modules in package_rows)
    for _, title in offers:
        if module_cells.count(title) != 1:
            issues.append(
                Issue("boundary", relative(packaging_path), f"offer module must appear once in package rows: {title}")
            )
    return issues


def validate_vendor_neutrality(files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    allowed_prefixes = (
        "assessments/",
        "docs/architecture/decisions/",
        "docs/explanations/",
        "references/",
        "specs/",
    )
    allowed_files = {
        "CHANGELOG.md",
        "README.md",
        "ROADMAP.md",
        "docs/architecture/diagrams/README.md",
        "docs/governance/ai-agent-policy-and-governance-v1.md",
        "docs/handbook/README.md",
        "docs/index.md",
        "tools/scripts/README.md",
    }
    scanned_suffixes = {".md", ".json", ".yaml", ".yml", ".toml"}
    for path in files:
        rel = relative(path)
        if path.suffix.lower() not in scanned_suffixes:
            continue
        if rel in allowed_files or rel.startswith(allowed_prefixes):
            continue
        text = path.read_text(encoding="utf-8")
        for allowed_literal in ALLOWED_VENDOR_LITERALS.get(rel, ()):
            text = text.replace(allowed_literal, " " * len(allowed_literal))
        vendor_pattern = VENDOR_NAME_RE if path.suffix.lower() == ".md" else STRUCTURED_VENDOR_NAME_RE
        match = vendor_pattern.search(text)
        if match:
            line = text.count("\n", 0, match.start()) + 1
            issues.append(
                Issue("vendor-neutrality", rel, f"vendor name outside source/case/mapping area at line {line}")
            )
    return issues


def validate_policy_history_boundary(files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in files:
        rel = relative(path)
        if not rel.startswith("templates/") or path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        match = LEGACY_POLICY_TEMPLATE_RE.search(text)
        if match:
            line = text.count("\n", 0, match.start()) + 1
            issues.append(
                Issue(
                    "policy-history",
                    rel,
                    f"canonical template references historical Policy v1 at line {line}",
                )
            )
    return issues


def validate_product_boundaries(files: list[Path]) -> list[Issue]:
    return (
        validate_commercial_boundary()
        + validate_vendor_neutrality(files)
        + validate_policy_history_boundary(files)
    )


def validate_sensitive_content(files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    patterns = {
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
        "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
        "personal macOS path": re.compile(
            re.escape("/Users/" + "rodgui") + r"(?:/|\b)"
        ),
    }
    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in patterns.items():
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                issues.append(Issue("sensitive", relative(path), f"possible {label} at line {line}"))
        if "# Readme\n" in text:
            issues.append(Issue("structure", relative(path), "placeholder '# Readme' heading remains"))
    return issues


def validate_required_paths() -> list[Issue]:
    required = [
        "README.md",
        "ROADMAP.md",
        "docs/index.md",
        "docs/governance/policy.md",
        "docs/governance/history/README.md",
        "docs/handbook/README.md",
        "docs/guides/framework-implementation-playbook.md",
        "docs/guides/maturity-model.md",
        "docs/patterns/README.md",
        "controls/control-catalog.json",
        "schemas/agent-registry.schema.json",
        "schemas/agent-blueprint.schema.json",
        "schemas/control-catalog.schema.json",
        "schemas/maturity-assessment.schema.json",
        "consulting/README.md",
        "consulting/ROADMAP.md",
        "consulting/consulting-engagement-model.md",
        "consulting/templates/consulting-proposal-template.md",
        "tools/assets/fonts/DejaVuSans.ttf",
        "tools/assets/fonts/DejaVuSans-Bold.ttf",
        "tools/assets/fonts/LICENSE_DEJAVU",
    ]
    return [Issue("structure", item, "required path is missing") for item in required if not (ROOT / item).exists()]


def main() -> int:
    files = repository_files()
    markdown_files = [path for path in files if path.suffix.lower() == ".md"]
    json_files = [path for path in files if path.suffix.lower() == ".json"]

    issues: list[Issue] = []
    issues.extend(validate_required_paths())
    issues.extend(validate_frontmatter(markdown_files))
    issues.extend(validate_frontmatter_related_paths(markdown_files))
    issues.extend(validate_markdown_links(markdown_files))
    issues.extend(validate_citations(markdown_files))
    issues.extend(validate_json_and_schemas(json_files))
    issues.extend(validate_assets())
    issues.extend(validate_policy_integrity())
    issues.extend(validate_tier_taxonomy())
    issues.extend(validate_product_boundaries(files))
    issues.extend(validate_sensitive_content(files))

    if issues:
        print(f"FAIL: {len(issues)} issue(s)")
        for issue in sorted(issues, key=lambda item: (item.category, item.path, item.message)):
            print(f"[{issue.category}] {issue.path}: {issue.message}")
        return 1

    catalog = load_json(ROOT / "controls/control-catalog.json")
    controls = catalog.get("controls", []) if isinstance(catalog, dict) else []
    domains = {control.get("domain") for control in controls if isinstance(control, dict)}
    print(
        "PASS: repository validation "
        f"({len(markdown_files)} markdown, {len(json_files)} json, "
        f"{len(controls)} controls, {len(domains)} domains)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
