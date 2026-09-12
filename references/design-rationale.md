# Design rationale and research basis

> Snapshot used to design this meta-skill. Runtime use must perform fresh research; this file is rationale, not a substitute for current evidence.

## Design conclusions

1. Existing skill creators generally start at clarification/drafting. This meta-skill should sit upstream as a discovery and design gate, then hand off to the normal builder.
2. Progressive disclosure is a repeated specification and practitioner theme: keep the entrypoint lean, move detailed protocols to references, and reserve scripts for deterministic checks.
3. Source count is a coverage floor, not a voting system. Authoritative and primary sources carry more weight than many weak summaries.
4. Expert knowledge should be elicited from concrete incidents and decisions, capturing cues, judgment rules, exceptions, errors, and validation criteria rather than generic advice.
5. Third-party skills are supply-chain inputs. Inspect before execution, compare description to behavior, and reuse mechanisms rather than blindly copying instructions.
6. Quality requires behavioral evals and exact contract validation, not only syntactic packaging checks.

## Sources reviewed (40 independent items; 10+ channel types)

| # | Channel | Grade | Source | Main contribution |
|---:|---|:---:|---|---|
| S01 | official-spec | S | [Agent Skills open specification repository](https://github.com/agentskills/agentskills) | Defines the portable skill folder model and progressive resource structure. |
| S02 | official-spec | S | [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx) | Specifies SKILL.md structure and metadata constraints. |
| S03 | vendor-docs | S | [Anthropic: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Frames skills as dynamically loaded procedural knowledge and context. |
| S04 | github-source | S | [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Uses user interview, progressive disclosure, eval prompts, and iterative improvement. |
| S05 | vendor-docs | S | [OpenAI Help: Skills in ChatGPT](https://help.openai.com/en/articles/20001066) | Describes skills as reusable workflows with instructions, examples, and code. |
| S06 | vendor-docs | S | [OpenAI Academy: Using skills](https://openai.com/academy/skills/) | Positions skills as reusable workflows for recurring work. |
| S07 | vendor-docs | S | [X developer docs: skill.md](https://docs.x.com/tools/skill-md) | Shows capability summaries, workflows, inputs, constraints, and discovery endpoints. |
| S08 | github-source | A | [Microsoft skill-creator](https://github.com/microsoft/skills/blob/main/.github/skills/skill-creator/SKILL.md) | A large vendor skill creator that encodes explicit workflow and platform requirements. |
| S09 | github-source | A | [mgechev skills best practices](https://github.com/mgechev/skills-best-practices/blob/main/README.md) | Emphasizes lean context, validation, and progressive resource loading. |
| S10 | github-source | A | [mblode agent-skills-creator](https://github.com/mblode/agent-skills/blob/main/skills/agent-skills-creator/SKILL.md) | Adds patterns, routing evals, audits, and keep/cut/merge decisions. |
| S11 | github-source | B | [nyosegawa agent skill best practices](https://github.com/nyosegawa/skills/blob/main/agent-skill-best-practices.md) | Identifies giant SKILL.md files as a context failure and advocates progressive disclosure. |
| S12 | github-source | B | [skill-creator-plus](https://github.com/aktsmm/agent-skills/blob/master/skill-creator-plus/SKILL.md) | Uses review checklists and explicit done criteria for skills. |
| S13 | github-source | B | [openlark agent-skills standard skill](https://github.com/openlark/skills/blob/main/skills/agent-skills/SKILL.md) | Routes detailed skill guidance into references and includes anti-patterns. |
| S14 | github-source | B | [DeerHide writing-skills](https://github.com/DeerHide/agent_skills/blob/main/skills/writing-skills/SKILL.md) | Consolidates cross-vendor skill-writing guidance. |
| S15 | github-source | B | [austindixson skill-creator](https://github.com/austindixson/skill-creator/blob/main/SKILL.md) | Combines drafting with test prompts and iterative evaluation. |
| S16 | github-source | B | [oryanmoshe writing-skills](https://github.com/oryanmoshe/agent-skills/blob/main/skills/writing-skills/SKILL.md) | Uses trigger-rich descriptions and avoids bloated reference material in the entrypoint. |
| S17 | security-research | B | [SkillGuard](https://github.com/Ag1rin/SkillGuard) | Scans skills for prompt injection, hidden instructions, credential leakage, and unsafe code. |
| S18 | security-research | B | [superagent skill-security](https://github.com/superagent-ai/skills/blob/main/skills/skill-security/SKILL.md) | Combines deterministic scanning with semantic contract checks. |
| S19 | evaluation-benchmark | B | [Skills SafetyBench](https://github.com/pyxnpyx/Skills-SafetyBench-EN) | Frames prompt injection, leakage, privilege escalation, and supply chain risks as skill-evaluation targets. |
| S20 | security-research | B | [K-Dense scientific-agent-skills security policy](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/SECURITY.md) | Treats misleading behavior, prompt injection, unsafe credentials, and malicious bundled code as in-scope skill risks. |
| S21 | x-practitioner | B | [Kaxil Naik on X: skills encode judgment](https://x.com/kaxil/status/2037503513350005134) | Describes iterating skills from real incidents and encoding personal engineering judgment, with references/scripts as support. |
| S22 | x-practitioner | B | [Ruben Hassid on X: specificity is the skill](https://x.com/rubenhassid/status/2039311247611412981) | Argues that a useful skill captures concrete recurring structure rather than vague task labels. |
| S23 | x-practitioner | C | [Nav Toor on X: prompt/scripts/MCP patterns](https://x.com/heynavtoor/status/2036861280859124100) | Distinguishes prompt-only, prompt+scripts, and prompt+MCP/subagent patterns. |
| S24 | reddit-community | B | [Reddit: I was wrong about Agent Skills](https://www.reddit.com/r/ClaudeAI/comments/1opxgq4/i_was_wrong_about_agent_skills_and_how_i_refactor/) | Reports context explosion from 800-1200 line skills and benefits from three-tier progressive disclosure. |
| S25 | reddit-community | C | [Reddit: Busy person's intro to Claude Skills](https://www.reddit.com/r/ClaudeAI/comments/1pq0ui4/the_busy_persons_intro_to_claude_skills_a_feature/) | Highlights reuse, automatic loading, and progressive disclosure in practice. |
| S26 | reddit-community | B | [Reddit: Agent Skills need runtime structure](https://www.reddit.com/r/ClaudeAI/comments/1q88p1b/why_agent_skills_need_a_defined_runtime_structure/) | Points out fragility when installation, dependencies, state, and runtime locations are unspecified. |
| S27 | reddit-community | C | [Reddit: skill marketplace and security scans](https://www.reddit.com/r/claude/comments/1rkjqjf/i_built_a_marketplace_for_skillmd_skills_because/) | Practitioner experience says many discovered skills are low quality and need formatting/security checks. |
| S28 | reddit-community | C | [Reddit: registry with versioning and security scans](https://www.reddit.com/r/ClaudeCode/comments/1r8tv4v/built_an_open_registry_for_agent_skills_with/) | Emphasizes versioning, rollback, and change visibility for skills. |
| S29 | peer-reviewed | A | [Hoffman, Crandall & Shadbolt 1998 Critical Decision Method](https://journals.sagepub.com/doi/10.1518/001872098779480442) | Uses multiple-pass event retrospection and probe questions to elicit expert knowledge and decision requirements. |
| S30 | peer-reviewed | A | [Brown, Power & Gore: Cognitive Task Analysis](https://journals.sagepub.com/doi/10.1177/10944281241271216) | Shows CTA as a rigorous method for eliciting complex expert cognition in context. |
| S31 | peer-reviewed | A | [Hoffman et al. 1995 Eliciting Knowledge from Experts](https://www.sciencedirect.com/science/article/pii/S0749597885710394) | Classifies elicitation approaches across task analysis, interviews, and contrived tasks. |
| S32 | peer-reviewed | A | [Hart 1985 Knowledge elicitation: issues and methods](https://www.sciencedirect.com/science/article/pii/0010448585902933) | Reviews interview, protocol analysis, induction, and repertory-grid approaches. |
| S33 | peer-reviewed | A | [Wood & Ford 1993 Structuring interviews with experts](https://onlinelibrary.wiley.com/doi/abs/10.1002/int.4550080106) | Warns against reductive bias and separates knowledge elicitation from implementation. |
| S34 | peer-reviewed | A | [Klein et al. 1989 Critical decision method](https://doi.org/10.1109/21.31053) | Elicits perceptual cues, conceptual discriminations, typicality judgments, and critical decisions under complexity. |
| S35 | government-manual | A | [GOV.UK Service Manual: Capturing research questions](https://www.gov.uk/service-manual/user-research/capturing-research-questions) | Advocates explicit research questions and revisiting them as learning evolves. |
| S36 | systematic-review | S | [Cochrane Handbook: searching for and selecting studies](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) | Recommends broad searching including grey literature, prior reviews, reference lists, and other sources to reduce bias. |
| S37 | expert-method | B | [JTBD Switch Interview](https://jobstobedone.org/switch-interview/) | Reconstructs real decision timelines instead of asking abstract feature preferences. |
| S38 | github-discussion | B | [Anthropic issue: optional frontmatter fields](https://github.com/anthropics/skills/issues/249) | Shows that even official skill-creator guidance can lag or conflict with the open specification. |
| S39 | github-source | S | [Anthropic skill-creator eval schemas](https://github.com/anthropics/skills/blob/main/skills/skill-creator/references/schemas.md) | Defines structured eval prompts and expectations for skill testing. |
| S40 | github-discussion | B | [Anthropic PR: expectations/assertions inconsistency](https://github.com/anthropics/skills/pull/1443) | A small schema-name mismatch broke consistency across documentation and tooling. |
