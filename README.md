# Research-First Creator

A Claude Agent Skill that acts as a research-first design gate for creating or substantially updating other Agent Skills.

Instead of jumping straight into drafting a `SKILL.md`, this skill requires:

1. Fresh multi-source research (30+ independent high-value sources across 8+ channel types)
2. An audit of similar existing skills
3. Extraction of expert practice and known failure modes
4. At least three non-redundant decision rounds with the user
5. A Design Freeze before implementation
6. Handoff to the normal skill-creator/builder for implementation, validation, and packaging

## Structure

- [`SKILL.md`](SKILL.md) — the skill definition and required workflow
- [`references/`](references/) — research protocol, existing-skill audit method, expert elicitation guide, decision-round structure, and the research ledger schema
- [`scripts/check_research_gate.py`](scripts/check_research_gate.py) — validates a research ledger against the completion criteria
- [`agents/openai.yaml`](agents/openai.yaml) — cross-platform agent interface metadata
- [`assets/icon.svg`](assets/icon.svg) — skill icon

## Usage

Drop this directory into your Claude Skills folder (e.g. `~/.claude/skills/research-first-creator`) so it is available for invocation. It activates automatically when you ask to create, build, or substantially revise a Skill, unless you explicitly ask to skip the research gate.
