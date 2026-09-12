#!/usr/bin/env python3
"""Validate a Research Ledger for the research-first skill creation gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path

VALID_GRADES = {"S", "A", "B", "C"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_research_gate.py <ledger.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: cannot read ledger: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    sources = data.get("sources")
    if not isinstance(sources, list):
        print("FAIL: sources must be a list")
        return 1

    urls: list[str] = []
    channels: set[str] = set()
    expert_sources = 0
    failure_sources = 0

    for i, src in enumerate(sources, 1):
        if not isinstance(src, dict):
            fail(errors, f"source #{i} is not an object")
            continue
        url = str(src.get("url", "")).strip()
        title = str(src.get("title", "")).strip()
        channel = str(src.get("channel", "")).strip()
        grade = str(src.get("grade", "")).strip().upper()
        roles = src.get("roles", [])
        mechanism = str(src.get("mechanism", "")).strip()
        impact = str(src.get("design_impact", "")).strip()

        if not title:
            fail(errors, f"source #{i} missing title")
        if not url.startswith(("http://", "https://")):
            fail(errors, f"source #{i} has invalid/missing URL")
        else:
            urls.append(url.rstrip("/"))
        if not channel:
            fail(errors, f"source #{i} missing channel")
        else:
            channels.add(channel)
        if grade not in VALID_GRADES:
            fail(errors, f"source #{i} grade must be one of {sorted(VALID_GRADES)}")
        if not mechanism:
            fail(errors, f"source #{i} missing mechanism")
        if not impact:
            fail(errors, f"source #{i} missing design_impact")
        if isinstance(roles, list):
            if "expert_practice" in roles:
                expert_sources += 1
            if "failure_mode" in roles or "security" in roles:
                failure_sources += 1
        else:
            fail(errors, f"source #{i} roles must be a list")

    unique_urls = set(urls)
    if len(unique_urls) != len(urls):
        fail(errors, "duplicate source URLs detected; independent sources must be unique items")

    narrow = data.get("narrow_domain_exception", {}) or {}
    narrow_used = bool(narrow.get("used", False))
    narrow_reason = str(narrow.get("reason", "")).strip()

    if len(unique_urls) < 30:
        if narrow_used and narrow_reason:
            warnings.append(
                f"narrow-domain exception used: {len(unique_urls)} sources (<30); reason: {narrow_reason}"
            )
        else:
            fail(errors, f"need >=30 independent sources; found {len(unique_urls)}")

    if len(channels) < 8:
        fail(errors, f"need >=8 source-channel types; found {len(channels)}: {sorted(channels)}")

    saturation = data.get("saturation", {}) or {}
    if not saturation.get("reached", False):
        fail(errors, "search saturation is not documented as reached")
    sat_note = str(saturation.get("note", "")).strip()
    if not sat_note:
        fail(errors, "saturation.note is required")

    audit = data.get("similar_skill_audit", {}) or {}
    if not audit.get("search_completed", False):
        fail(errors, "similar-skill search must be completed")
    try:
        candidate_count = int(audit.get("candidate_count", 0))
    except Exception:
        candidate_count = -1
        fail(errors, "similar_skill_audit.candidate_count must be an integer")
    compared = audit.get("compared", []) or []
    if not isinstance(compared, list):
        fail(errors, "similar_skill_audit.compared must be a list")
        compared = []
    distinct_compared = {str(x).strip() for x in compared if str(x).strip()}
    if candidate_count >= 3 and len(distinct_compared) < 3:
        fail(errors, "at least 3 similar skills must be compared when 3+ candidates exist")
    if 0 <= candidate_count < 3:
        if len(distinct_compared) < candidate_count:
            fail(errors, "compare every similar-skill candidate when fewer than 3 exist")
        if candidate_count < 3 and not str(audit.get("scarcity_note", "")).strip():
            fail(errors, "scarcity_note is required when fewer than 3 similar skills exist")

    if expert_sources == 0:
        warnings.append("no source is tagged expert_practice; verify that expert tacit knowledge was actually searched")
    if failure_sources == 0:
        warnings.append("no source is tagged failure_mode/security; verify that failure modes were actually searched")

    print(f"Sources: {len(unique_urls)}")
    print(f"Channels: {len(channels)} ({', '.join(sorted(channels))})")
    print(f"Expert-practice sources: {expert_sources}")
    print(f"Failure/security sources: {failure_sources}")
    print(f"Similar candidates: {candidate_count}; compared: {len(distinct_compared)}")

    for warning in warnings:
        print(f"WARN: {warning}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: research gate requirements are satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
