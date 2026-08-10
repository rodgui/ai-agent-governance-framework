#!/usr/bin/env python3
"""Assemble the documentation site source and build it with MkDocs.

The canonical content is spread across top-level folders and links between them
are relative (``../../controls/README.md``). Copying those folders into a single
staging directory preserves the layout, so no link rewriting is needed and the
published site matches what a reader sees in the repository.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGING = ROOT / "site_src"

# Folders whose content is published. Everything else stays out of the site.
CONTENT_DIRS = (
    "docs",
    "controls",
    "schemas",
    "templates",
    "examples",
    "references",
    "assessments",
    "consulting",
    "tools",
)
CONTENT_FILES = ("README.md", "CHANGELOG.md", "ROADMAP.md", "LICENSE", "CONTRIBUTING.md")

# Extensions copied into the staging area. Schemas and examples are published as
# source so a reader can inspect the contract, not only its description.
PUBLISHED_SUFFIXES = {".md", ".json", ".png", ".svg", ".py"}


def stage() -> None:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)

    for name in CONTENT_FILES:
        source = ROOT / name
        if source.exists():
            shutil.copy2(source, STAGING / name)

    for directory in CONTENT_DIRS:
        source_root = ROOT / directory
        if not source_root.is_dir():
            continue
        for source in sorted(source_root.rglob("*")):
            if source.is_dir() or source.suffix.lower() not in PUBLISHED_SUFFIXES:
                continue
            destination = STAGING / source.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    copied = sum(1 for path in STAGING.rglob("*") if path.is_file())
    print(f"staged {copied} files into {STAGING.relative_to(ROOT)}")


def build(strict: bool, serve: bool) -> int:
    command = [sys.executable, "-m", "mkdocs", "serve" if serve else "build"]
    if strict:
        command.append("--strict")
    return subprocess.call(command, cwd=ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serve", action="store_true", help="serve locally instead of building")
    parser.add_argument("--no-strict", action="store_true", help="allow warnings")
    parser.add_argument("--stage-only", action="store_true", help="only assemble site_src")
    args = parser.parse_args()

    stage()
    if args.stage_only:
        return 0
    return build(strict=not args.no_strict, serve=args.serve)


if __name__ == "__main__":
    raise SystemExit(main())
