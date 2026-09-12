# Decision rounds and Design Freeze

Always conduct at least three distinct user decision rounds after showing research findings, unless the user explicitly opted out of the research gate.

Do not compress all questions into one giant questionnaire. Each round should use the answers from the previous round and the research evidence.

## Round 1 — Job and boundary

Resolve the shape of the skill:
- What exact user requests should trigger it?
- What adjacent requests should not trigger it?
- What inputs can it receive?
- What usable output/artifact should it produce?
- What tools, connectors, local files, or runtimes may it use?
- What 2-4 realistic examples define success?

Do not re-ask facts already given.

## Round 2 — Research-backed design choices

Present the meaningful alternatives discovered during research.

Good questions look like:
- "Three strong implementations use A, while domain experts prefer B in high-stakes cases. A is faster; B exposes judgment rules. Which should be the default?"
- "Existing skills put the whole playbook in SKILL.md, but repeated failure reports favor progressive references. I recommend the latter. Do you want strict or adaptive loading?"

Avoid generic questions such as "anything else?".

## Round 3 — Quality, failure, and governance

Resolve:
- hard quality thresholds;
- when the skill must stop or ask the user;
- permissions and dangerous actions;
- acceptable automation level;
- source/citation requirements;
- validation/eval cases;
- maintenance and freshness expectations;
- what to do when evidence conflicts.

## Round 4+ — Only for material unresolved choices

Continue when an unresolved choice would change:
- architecture;
- safety;
- output contract;
- tool permissions;
- key expert methodology;
- validation criteria.

Do not continue for cosmetic preferences that the model can safely choose.

## Challenging the initial premise

If evidence shows the user's initial implementation is materially weaker:
1. state the conflict plainly;
2. show the evidence pattern;
3. explain the practical tradeoff;
4. recommend an alternative;
5. let the user decide.

Do not silently substitute the alternative.

## Design Freeze template

Use a compact version of this structure:

### Design Freeze
- **Name:**
- **Core job:**
- **Triggers:**
- **Non-triggers:**
- **Inputs:**
- **Outputs:**
- **Mandatory workflow:**
- **Tools/connectors:**
- **Must not:**
- **Adopted external mechanisms:**
- **Rejected mechanisms:**
- **Quality/evals:**
- **Remaining assumptions:**

After presenting the freeze, continue directly to implementation unless it exposes a major misunderstanding or the user interrupts.
