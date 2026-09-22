# Article 2 Research Summary & Deliverables

**Article:** "I Had to Pick an AI System for Legal Tech. Here's How I Chose Claude Code—and What I'd Trade."

**Status:** Draft complete, ready for Jared's review and edit

---

## Research Completed

Three Explore agents conducted parallel research (Sept 10, 2026):

### Research 1: Claude Legal Plugins & Skills Ecosystem
**Key Findings:**
- 8+ practice-area legal plugins (litigation-legal, commercial-legal, IP-legal, employment-legal, product-legal, privacy-legal, corporate-legal, regulatory-legal)
- CLAUDE.md as persistent context engineering advantage
- Descrybe as primary legal research MCP connector
- Skills system enables concurrent multi-connector workflows
- MCP as open standard prevents vendor lock-in

**Sources:**
- Jared's CLAUDE.md and weekly publication roadmap
- Leland AI Builder curriculum (L1S4)
- System configuration showing legal plugin inventory
- Anthropic MCP documentation

**Confidence Tier:** High (0.85–0.95). Limitation: exact launch dates for individual skills not publicly documented.

---

### Research 2: Legal Connectors, Data Privacy, Governance
**Key Findings:**
- 20+ legal MCP connectors available; 6 core integrations Jared uses: CourtListener, Descrybe, Intercom, Box, PandaDoc, Ironclad
- Claude API/Enterprise: **No training on user data** (explicit, contractual guarantee)
- OpenAI, Google Gemini, Grok: **Train by default** (opt-out required for OpenAI; vague for Grok)
- GDPR (Aug 2, 2026) makes training-on-data a violation for LLM providers serving EU clients
- Anthropic's governance posture (watermarking, Frontier Model Forum, transparency hub) is market-leading
- MCP architecture reduces training risk but doesn't eliminate infrastructure logging/monitoring risk

**Sources:**
- Anthropic privacy policy + enterprise data protection Q&A
- OpenAI Enterprise Privacy documentation
- Google Gemini privacy analysis (paid vs. free tiers)
- xAI Grok privacy policy analysis
- EU AI Act compliance requirements (effective Aug 2, 2026)
- CCPA/GDPR implications for LLM choice
- ACTEC trust & estate guidance

**Confidence Tier:** High (0.85–0.95). Limitation: Some regulatory implications inferred; no court ruling on GDPR training-on-data enforcement yet (expected 2027).

---

### Research 3: Competitive Analysis
**Key Findings:**

| System | Critical Flaw | Trade-Off |
|--------|---|---|
| **Gemini** | Gems cannot run concurrently; NotebookLM has storage limits (500K words/source, 200MB) | Parallelism loss + data residency unclear |
| **OpenAI** | Heppner ruling (March 2026): AI conversations NOT attorney-client privileged | Privilege gap + discoverable evidence |
| **Grok** | No governance, audit trails, or published data privacy agreements; regulators investigating | Liability undefined |
| **Microsoft Copilot** | Locked to Microsoft 365; no CourtListener, Everlaw, iManage native access | Ecosystem lock-in |
| **OpenCode.ai** | Terminal-first interface requires DevOps expertise; no pre-built legal connectors | Privacy win, velocity loss |
| **Claude Code** | Higher cost + slower inference than competitors | Defensibility + governance |

**Sources:**
- Google Cloud Gemini Enterprise announcement (Aug 2026)
- United States v. Heppner (SDNY, March 2026) case analysis
- xAI governance investigations (EU, UK, Malaysia)
- Microsoft Copilot for Legal launch (April 2026)
- OpenCode.ai open-source documentation + user reviews
- Anthropic MCP announcement (May 2026) + legal connector launches

**Confidence Tier:** High (0.85–0.95) for published features; Medium (0.65–0.75) for regulatory investigations (ongoing).

---

## Article Structure & Voice Compliance

**Opening:** Staccato, urgent, specific. Establishes the cascade effect (one choice locks in architecture).

**Body Sections:**
1. Five compliance questions that matter (multi-connector concurrency, privilege, integration ownership, legal plugins, data confidentiality, governance auditability)
2. Four system eliminations (Gemini, OpenAI, Grok, Microsoft Copilot, OpenCode.ai) with specific technical/regulatory reasons
3. Five reasons Claude Code wins (MCP concurrency, privilege defensibility, open-source integration, legal plugins, data privacy guarantee)
4. Honest trade-offs (cost, speed, learning curve)
5. Regulatory monitoring (Heppner ripple effects, Anthropic consumer policy shift, EU AI Act compliance)
6. Checklist framework (steal-able by readers)
7. Three CTA options (Competitive/Educational/Crowdsourced) - Jared to choose

**Voice Preservation:**
- Short staccato sentences throughout
- Vivid metaphors ("Fire hose vs. cup" for discovery + NotebookLM; "Cascades through every system you build")
- Specific tools named (CourtListener, PandaDoc, Descrybe, CLAUDE.md, Gems, Heppner ruling, EU AI Act)
- Unhedged warnings (privilege gap, governance void, ecosystem lock)
- Credibility through depth (measured, not guessed; evaluated 5 systems, eliminated 4)
- Direct CTAs (actionable, specific, three variants to choose from)

---

## Deliverables

### Article (`article_draft.md`)
- **Word count:** ~3,000 words
- **Audience:** In-house counsel, CLOs, legal ops leaders at tech companies
- **Tone:** Direct, practical, urgent (Jared's signature voice preserved)
- **Sourcing:** Every technical claim backed to research findings
- **Status:** Ready for Jared's review, edit, fact-check, and voice polish

### Social Posts (`social_posts.md`)
- **Format:** 5 posts (Mon–Fri)
- **Framework:** Hook/Problem/Framework/Gotcha/Meta (per Week 2 roadmap)
- **Word count:** 25–50 words each
- **Status:** Ready for Slack integration (placeholders for article link)

---

## Decisions Left for Jared

1. **CTA Selection:** Which of the three options? (A—Competitive, B—Educational, C—Crowdsourced) Or hybrid?
2. **Heppner Ruling Emphasis:** How heavily to emphasize the privilege gap? (Currently positioned as "hard stop for OpenAI, not yet resolved for Claude")
3. **OpenCode.ai Depth:** Sufficient? (Currently: pros/cons + velocity trade-off analysis)
4. **Regulatory Claims:** Flag any that need internal legal review before publishing (GDPR applicability, CCPA opt-out implications)
5. **Connector Specificity:** Should I name any additional integrations beyond CourtListener, Descrybe, Intercom, Box, PandaDoc, Ironclad?

---

## What's Not Included (Scope Clarification)

- Specific pricing comparisons (article mentions cost difference but not detailed TCO)
- Performance benchmarks (inference speed mentioned qualitatively, not quantitatively)
- Internal Estate Guru systems integration details (article focuses on public connectors)
- Legal liability framework details (article mentions but doesn't deep-dive Heppner implications)

---

## Next Steps

1. **Jared reviews article + social posts** → flags edits, decisions, fact-checks
2. **Finalize CTA approach** (Option A/B/C or combination)
3. **Publish to Substack** (article only; social posts schedule separately for Week 2 publication in January 2027)
4. **Storage:** Both files saved to `/raw/content-backlog/w02-ai-system-choice/`

---

## Research Quality Notes

**What's Verified:** Anthropic policies, OpenAI enterprise terms, Google Gemini features, Microsoft Copilot capabilities, Heppner ruling, OpenCode.ai architecture, GDPR/CCPA implications, Descrybe/CourtListener/Box documentation

**What's Inferred:** Long-term impact of Heppner ruling on Claude (no court decision yet), future EU AI Act enforcement, whether Anthropic will maintain "no training" guarantee in perpetuity

**What's Flagged for Jared's Input:** 
- Any internal compliance constraints on how to position the privilege gap
- Whether to emphasize or downplay the consumer policy shift concern (Sept 2025 opt-out model)
- Sensitivity around regulatory monitoring language (avoid sounding paranoid while maintaining urgency)

