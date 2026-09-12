<div align="center">

# 🔬 Research-First Creator

**A research-and-design gate that stands between "I want a Skill" and "here's a Skill" — so what gets built is grounded in evidence, not guesswork.**

**在"我想要一个 Skill"和"这是你的 Skill"之间，插入一道以证据为准绳的研究与设计关卡。**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](#license)
[![Platform](https://img.shields.io/badge/platform-Claude%20%7C%20ChatGPT%20%7C%20Codex%20%7C%20Atlas-6b46c1.svg)](agents/openai.yaml)
[![Sources](https://img.shields.io/badge/design%20basis-40%2B%20cross--vendor%20sources-orange.svg)](references/design-rationale.md)

[English](#english) · [中文](#中文)

</div>

---

<a id="english"></a>
## English

### The problem it solves

Ask almost any assistant to "build me a Skill" and it does the same thing: a few clarifying questions, then straight to drafting `SKILL.md`. The result usually *works*, but it quietly inherits whatever the assistant already believed about the domain — untested against how experts actually operate, unchecked against skills that already solve the same problem, and often too generic to be worth maintaining.

**Research-First Creator refuses to skip that step.** It sits upstream of any skill builder and enforces one rule: *research and design before implementation, every time* — unless you explicitly say "skip research."

### What makes it different

Most skill-creation tools on the market are **drafting assistants**. This is a **design gate**. The distinction shows up directly in the workflow:

| Capability | Typical skill-creator (Anthropic / Microsoft / community forks) | Research-First Creator |
|---|---|---|
| Starting point | Interview → draft `SKILL.md` | Research → audit → elicitation → **3+ decision rounds** → design freeze → *then* hand off to the drafting builder |
| Evidence requirement | None enforced | **≥30 independent sources across ≥8 channel types**, graded S/A/B/C by authority, with a documented saturation check |
| Competing solutions | Rarely reviewed | Mandatory audit of the **3 closest existing skills** (or all candidates, with scarcity documented) — what to keep, modify, or reject, and why |
| Expert knowledge | Generic best-practice tips | Extracts the actual reasoning chain experts use: `scenario → cues → judgment rule → action → exception → common error → validation` |
| Third-party trust | Often copies patterns wholesale | Treats every external skill as **untrusted supply-chain input** — read-only inspection, no blind execution, no copied secrets/hooks/instructions |
| Verifiability | "Trust me, I researched it" | A machine-checkable **Research Ledger**, validated by [`scripts/check_research_gate.py`](scripts/check_research_gate.py) against explicit pass/fail criteria |
| Weak ideas | Built as requested | Will **tell you** when your first idea is weaker than an evidence-backed alternative, and explain the tradeoff — instead of silently complying or silently overriding you |

In short: other tools optimize for *getting to a file fast*. This one optimizes for *not building the wrong thing well*.

### Why this matters

- **Skills compound.** A skill built on a shaky first impression gets reused, forked, and trusted by other agents. Front-loading research is cheap; unwinding a bad skill after it's in production is not.
- **The Skill ecosystem is now a supply chain.** With registries and marketplaces growing across Claude, ChatGPT, and other platforms, copying a popular skill's instructions or scripts without review is a real injection/security risk — this gate builds that review in by default instead of treating it as optional.
- **"Looks reasonable" isn't "grounded in practice."** Generic advice from a model's training data drifts from what practitioners actually do when things go wrong. The expert-elicitation step specifically hunts for real incidents, exceptions, and failure modes — not tips.
- **It's falsifiable, not just thorough-sounding.** The Research Ledger schema and gate-check script mean "I did the research" is a claim that can be verified, not just asserted.

### How it works

1. Classify the request; skip only on an explicit opt-out.
2. Research across ≥8 channel types (official specs, vendor docs, GitHub source, peer-reviewed work, practitioner threads, postmortems, security research, benchmarks…) until saturation, targeting ≥30 independent high-value sources.
3. Audit the closest existing skills — what to keep, modify, or reject.
4. Extract expert practice as concrete scenario → judgment → exception chains, not generic tips.
5. Build a Research Ledger and validate it (script-checked when code execution is available).
6. Present findings, then run ≥3 non-redundant decision rounds with you (scope → architecture/tradeoffs → constraints/quality bar).
7. Challenge your assumptions when the evidence says a different design is stronger.
8. Issue a **Design Freeze** — a single, complete spec covering scope, workflow, forbidden behaviors, adopted/rejected mechanisms, and quality criteria.
9. Hand off to the normal skill-creator/builder for implementation, then validate with real trigger/non-trigger/edge-case tests.

### Repository layout

```
research-first-creator/
├── SKILL.md                          # entrypoint: the gate's required workflow
├── references/
│   ├── research-protocol.md          # source channels, grading, saturation rules
│   ├── existing-skill-audit.md       # comparison method + supply-chain trust boundary
│   ├── expert-elicitation.md         # how to extract tacit expert knowledge
│   ├── decision-rounds.md            # 3-round questioning + Design Freeze format
│   ├── research-ledger-schema.md     # ledger fields for manual verification
│   └── design-rationale.md           # the 40+ sources used to design this skill itself
├── scripts/
│   └── check_research_gate.py        # validates a ledger.json against pass/fail criteria
├── agents/openai.yaml                # cross-platform interface metadata
└── assets/icon.svg
```

### Install

Copy this folder into your skills directory, e.g.:

```bash
git clone https://github.com/xjinjinjin/research-first-creator.git ~/.claude/skills/research-first-creator
```

It activates automatically whenever you ask to create, build, redesign, or substantially rework a Skill — no manual invocation needed, unless you say "skip research."

### Design basis

This meta-skill isn't a personal opinion piece either — its own design was built the same way it asks you to build skills: [40+ sources across 10+ channel types](references/design-rationale.md), including the official Agent Skills specification, Anthropic and Microsoft's own skill-creators, peer-reviewed knowledge-elicitation methodology (Critical Decision Method, Cognitive Task Analysis), and skill-security research (SkillGuard, Skills SafetyBench).

---

<a id="中文"></a>
## 中文

### 解决什么问题

几乎所有"帮我做一个 Skill"的助手都走同一条路：问几个澄清问题，然后直接开始写 `SKILL.md`。结果通常"能用"，但悄悄继承了模型对该领域已有的一切先入之见——没有对照真正的专家做法验证过，没有和已经解决同一问题的其他 Skill 对比过，往往也因为过于通用而不值得长期维护。

**Research-First Creator 拒绝跳过这一步。** 它位于任何 Skill 构建器的上游，强制执行一条规则：*每次都先研究、先设计，再动手实现*——除非你明确说"跳过研究"。

### 它与同类的区别

市面上大多数"Skill 创建工具"（包括 Anthropic、Microsoft 官方版本以及众多社区分支）本质上是**起草助手**；而这是一道**设计关卡**。差异体现在工作流的每一步：

| 能力项 | 常见 Skill 创建工具（官方 / 社区分支） | Research-First Creator |
|---|---|---|
| 起点 | 访谈 → 直接起草 `SKILL.md` | 研究 → 同类审计 → 专家知识提取 → **至少 3 轮决策** → 设计冻结 → 才交给起草构建器 |
| 证据门槛 | 无强制要求 | **至少 30 个独立来源、覆盖至少 8 类渠道**，按 S/A/B/C 权威分级，并记录搜索饱和证据 |
| 竞品参考 | 很少系统比较 | 强制审计**最接近的 3 个已有 Skill**（不足 3 个则比较全部候选并说明稀缺原因），逐一记录"保留/修改/拒绝"及理由 |
| 专家知识 | 泛泛的"最佳实践"提示 | 提取专家真实的推理链：`场景 → 线索 → 判断规则 → 行动 → 例外 → 常见错误 → 验证方式` |
| 第三方信任边界 | 常常整段照搬 | 把每个外部 Skill 都当作**未经信任的供应链输入**——只读检查、不盲目执行、不照抄密钥/钩子/隐藏指令 |
| 可验证性 | "相信我，我研究过了" | 提供机器可校验的**研究台账（Research Ledger）**，由 [`scripts/check_research_gate.py`](scripts/check_research_gate.py) 按明确的通过/失败标准自动核验 |
| 面对薄弱想法 | 照单全收地实现 | 当你最初的方案明显弱于有证据支撑的替代方案时，会**主动指出**并说明取舍，而不是默默照做或默默替你改主意 |

一句话总结：别的工具追求"尽快出一个文件"，这个工具追求"不要把错的东西做得很漂亮"。

### 为什么重要

- **Skill 会被复用和传播。** 建立在一时印象上的 Skill 一旦投入使用，会被反复调用、被他人 fork、被其他 Agent 信任。前置研究的成本很低，事后为一个方向错误的 Skill "打补丁"的成本很高。
- **Skill 生态已经是一条供应链。** 随着 Claude、ChatGPT 等平台的 Skill 市场和注册中心不断扩张，未经审查直接照搬热门 Skill 的指令或脚本，本身就是提示注入/供应链安全的真实风险——这道关卡把审查当作默认动作，而不是可选项。
- **"看起来合理"不等于"扎根于实践"。** 模型训练数据里的通用建议，往往和专家在真正出问题时的实际做法有差距。专家知识提取环节专门挖掘真实事故、例外情况和失败模式，而不是空洞的技巧清单。
- **可证伪，而不只是听起来严谨。** 研究台账的 schema 和自动核验脚本，让"我做过研究"从一句自我声明，变成一个可以被检验的事实。

### 工作原理

1. 判断请求类型；只有在你明确要求跳过时才跳过研究关卡。
2. 覆盖至少 8 类信息渠道（官方规范、厂商文档、GitHub 源码、同行评审文献、从业者讨论、事后复盘、安全研究、评测基准……）进行搜索，直到饱和，目标是至少 30 个独立高价值来源。
3. 审计最接近的已有 Skill——决定保留、修改还是拒绝其中的机制。
4. 以"场景 → 判断 → 例外"的具体链条提取专家实践，而非泛泛建议。
5. 建立研究台账并核验（有代码执行能力时用脚本核验）。
6. 展示研究发现，随后与你进行至少 3 轮不重复的决策沟通（范围 → 架构与取舍 → 约束与质量标准）。
7. 当证据支持更优方案时，主动挑战你最初的设想。
8. 发出**设计冻结（Design Freeze）**——一份完整规格，涵盖范围、工作流、禁止行为、采纳/拒绝的机制、质量标准。
9. 交给常规的 skill-creator/构建器完成实现，再用真实的触发/非触发/边界用例进行验证。

### 仓库结构

```
research-first-creator/
├── SKILL.md                          # 入口：关卡的强制工作流
├── references/
│   ├── research-protocol.md          # 信息渠道、分级方法、饱和判定规则
│   ├── existing-skill-audit.md       # 同类比较方法 + 供应链信任边界
│   ├── expert-elicitation.md         # 如何提取专家的隐性知识
│   ├── decision-rounds.md            # 三轮提问结构 + 设计冻结格式
│   ├── research-ledger-schema.md     # 供人工核验的台账字段说明
│   └── design-rationale.md           # 设计本 Skill 时使用的 40+ 篇资料
├── scripts/
│   └── check_research_gate.py        # 按通过/失败标准自动核验 ledger.json
├── agents/openai.yaml                # 跨平台接口元数据
└── assets/icon.svg
```

### 安装方式

将本目录复制到你的 skills 目录，例如：

```bash
git clone https://github.com/xjinjinjin/research-first-creator.git ~/.claude/skills/research-first-creator
```

之后，只要你要求创建、构建、重新设计或大幅调整某个 Skill，它会自动触发，无需手动调用——除非你说"跳过研究"。

### 设计依据

这个元 Skill 本身也不是凭个人观点写成的——它自己的设计过程，用的正是它要求你遵循的方法：参考了 [40 余篇、覆盖 10 余种渠道的资料](references/design-rationale.md)，包括官方 Agent Skills 规范、Anthropic 与 Microsoft 各自的 skill-creator、专家知识提取的同行评审方法论（关键决策法 Critical Decision Method、认知任务分析 Cognitive Task Analysis），以及 Skill 安全研究（SkillGuard、Skills SafetyBench）。

---

<div align="center">

**License:** MIT · **Compatible with:** Claude, ChatGPT, Codex, Atlas ([see `agents/openai.yaml`](agents/openai.yaml))

</div>
