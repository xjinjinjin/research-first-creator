# Research protocol

## 1. Start with a source map, not random browsing

Create a query matrix across these intents:

1. Existing implementation: `[task] skill`, `[task] SKILL.md`, `[task] agent skill`, repo/registry searches.
2. Authoritative rules: official specifications, vendor docs, standards, APIs, professional bodies.
3. Expert practice: named experts, maintainers, researchers, senior practitioners, conference talks, interviews, case studies.
4. Failure modes: postmortems, issues, bug reports, critiques, security advisories, benchmark failures.
5. Evaluation: tests, rubrics, benchmarks, acceptance criteria, quality checklists.
6. Adjacent methods: methods from neighboring fields that solve the same cognitive or workflow problem.

Use multiple query phrasings and follow citation/reference trails from strong sources.

## 2. Coverage floor

Default minimum:
- >=30 unique high-value source items;
- >=8 materially different source-channel types.

A source item is a specific page, paper, repository file, discussion, issue, talk, or post. Mirrors and reposts do not count as independent items.

Do not satisfy the quota with low-value duplicates.

## 3. Source grading

Grade each source:

- S: original specification, official docs, standard, original maintainer/author, primary source.
- A: peer-reviewed research, recognized expert, professional body, strong original case study.
- B: detailed practitioner evidence, credible repo, high-signal community discussion, technical post with reproducible detail.
- C: weak summary, repost, generic advice, unverified assertion. Use as a lead, not as decisive evidence.

Prefer mechanisms supported by S/A sources. Use B sources to discover real-world edge cases. Treat C sources as provisional.

## 4. Search saturation

After reaching 30 sources, continue in small batches (typically 5-10 strong candidates).

Track whether each new batch adds any new:
- mechanism;
- design conflict;
- failure mode;
- expert cue/judgment rule;
- evaluation criterion;
- materially different existing implementation.

Mark saturation only when a new batch adds essentially no new decision-relevant information. A repeated paraphrase is not a new mechanism.

If the topic is narrow and cannot support 30 high-value sources:
1. search broader adjacent terminology and older terminology;
2. follow citations and reference lists;
3. search practitioner channels and issue trackers;
4. if still scarce, document the exact scarcity and proceed with all high-quality evidence found.

Never add low-value pages merely to hit 30.

## 5. Research findings synthesis

Before questioning the user, synthesize the ledger into five buckets:

1. Existing solutions: strongest reusable mechanisms and gaps.
2. Expert tacit practice: cues, judgments, exceptions, and validation.
3. Failure modes: recurring ways similar workflows fail.
4. Design conflicts: credible alternative approaches with tradeoffs.
5. Recommended defaults: the smallest set of research-backed choices likely to improve the skill.

Only these decision-relevant findings need to be shown in chat. Keep the full ledger as an internal or file artifact when practical.
