# Research Ledger schema

When practical, represent the research as JSON with this shape:

```json
{
  "topic": "target skill topic",
  "similar_skill_audit": {
    "search_completed": true,
    "candidate_count": 4,
    "compared": ["url-1", "url-2", "url-3"],
    "scarcity_note": ""
  },
  "saturation": {
    "reached": true,
    "last_batch_size": 6,
    "new_decision_relevant_mechanisms": 0,
    "note": "The final batch repeated already-captured mechanisms."
  },
  "narrow_domain_exception": {
    "used": false,
    "reason": ""
  },
  "sources": [
    {
      "id": "S01",
      "title": "Source title",
      "url": "https://example.com/item",
      "channel": "official-spec",
      "grade": "S",
      "roles": ["design_evidence"],
      "mechanism": "What this source teaches",
      "design_impact": "How it changes the target skill",
      "decision": "adopt",
      "reason": "Why"
    }
  ]
}
```

## Required checks

- `url` values must be unique enough to represent independent source items.
- `grade` must be one of `S`, `A`, `B`, `C`.
- `channel` should describe the actual source type, not an invented synonym used to inflate channel count.
- `roles` may include: `existing_skill`, `expert_practice`, `failure_mode`, `design_evidence`, `security`, `evaluation`.
- Each important source needs a mechanism and design impact, not only a citation.
- By default, require >=30 sources and >=8 channel types.
- If `narrow_domain_exception.used=true`, fewer than 30 sources is allowed only when the exception reason is substantive and saturation is reached.
- If `candidate_count>=3`, `compared` must contain at least 3 distinct candidate URLs.
- If `candidate_count<3`, compare every candidate found and explain scarcity.
- `saturation.reached` must be true before moving to user questioning.

Run `scripts/check_research_gate.py <ledger.json>` when execution is available.
