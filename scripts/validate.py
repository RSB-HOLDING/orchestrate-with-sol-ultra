#!/usr/bin/env python3
"""Validate the repository's Codex skill structure without dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = "orchestrate-with-sol-ultra"
REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/delegation-packet.md",
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def parse_frontmatter(content: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if not match:
        fail("SKILL.md must begin with YAML frontmatter")

    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in metadata:
            fail(f"duplicate frontmatter key: {key}")
        metadata[key] = value
    return metadata


def validate_skill() -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"required file is missing: {relative}")

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    metadata = parse_frontmatter(skill_text)
    if set(metadata) != {"name", "description"}:
        fail("SKILL.md frontmatter must contain only name and description")
    if metadata["name"] != SKILL_NAME:
        fail(f"skill name must be {SKILL_NAME!r}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata["name"]):
        fail("skill name must use lowercase hyphen-case")
    if len(metadata["name"]) > 64:
        fail("skill name exceeds 64 characters")
    if not metadata["description"] or len(metadata["description"]) > 1024:
        fail("skill description must contain 1-1024 characters")
    if "<" in metadata["description"] or ">" in metadata["description"]:
        fail("skill description cannot contain angle brackets")
    if "references/delegation-packet.md" not in skill_text:
        fail("SKILL.md must link directly to the delegation packet")

    agent_text = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    short_match = re.search(r'^\s*short_description:\s*"([^"]+)"\s*$', agent_text, re.MULTILINE)
    if not short_match or not 25 <= len(short_match.group(1)) <= 64:
        fail("openai.yaml short_description must contain 25-64 characters")
    if f"${SKILL_NAME}" not in agent_text:
        fail("openai.yaml default_prompt must explicitly mention the skill")
    if not re.search(r"^\s*allow_implicit_invocation:\s*true\s*$", agent_text, re.MULTILINE):
        fail("openai.yaml must preserve the intended implicit-invocation policy")


def validate_markdown() -> None:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        fences = sum(1 for line in text.splitlines() if line.strip().startswith("```"))
        if fences % 2:
            fail(f"unbalanced fenced code block in {path.relative_to(ROOT)}")

        for raw_target in link_pattern.findall(text):
            target = unquote(raw_target.strip().split("#", 1)[0])
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                fail(f"broken link in {path.relative_to(ROOT)}: {raw_target}")


def main() -> int:
    validate_skill()
    validate_markdown()
    print("PASS: skill structure, metadata, and Markdown links are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
