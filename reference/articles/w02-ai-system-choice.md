# I Had to Pick an AI System for Legal Tech. Here's How I Chose Claude Code—and What I'd Trade.

I was six months into my role as CLO at Estate Guru when I faced a question most legal teams never ask: **Which AI system should I build our entire legal operations on?**

Not "should we use AI?" Everyone's using AI. But the choice of *which* system—which LLM, which architecture, which connectors, which governance framework—cascades through every automation you'll ever build. Get it right and your moat compounds. Get it wrong and you're rebuilding in 18 months.

I evaluated five systems. I eliminated four. Here's why I chose Claude Code. And what I'd give up if I picked someone else.

---

## The Cascade Effect: Why This Choice Matters More Than You Think

One AI system powers everything.

Your automations. Your documentation review. Your compliance checking. Your agent architecture. Your audit trails.

If you choose an LLM without legal plugins, you're hand-coding compliance checks for every workflow. If you choose Claude Code, Descrybe handles case law research automatically. If you need CourtListener + PandaDoc + Intercom running simultaneously, some systems force you to pick one. Others run all three at once.

This isn't a point-in-time decision. It's an architectural lock-in. Every system you build assumes this choice.

I've watched CLOs regret this call. They picked cheap. They picked fast. They hit a compliance wall and realized: *My whole foundation is built on the wrong system, and rewriting takes six months I don't have.*

So I didn't guess. I measured.

---

## Why This Decision Is a Compliance Decision, Not a Tech Decision

Here's what I needed to know:

**1. Can I run multi-connector workflows concurrently?**

Meaning: If I need to query case law (CourtListener), pull contract metadata (PandaDoc), extract compliance data (Intercom), and cross-reference them all in one reasoning chain—can the system do it simultaneously, or do I have to ask it one question at a time?

**2. Can I guarantee attorney-client privilege?**

This one's new. In March 2026, a federal court (Heppner, SDNY) ruled that AI conversations are not attorney-client privileged because "the AI doesn't hold a law license." That ruling exposed a gap every legal team now has to manage: If I use ChatGPT for client work, even with an enterprise agreement, those conversations might not be privileged. Period.

**3. Do I own the integration, or does the vendor own it?**

I don't want to be locked into Anthropic's connectors. Or OpenAI's. I want a standard (Model Context Protocol) so that when I need a new legal system connected, I can wire it myself or hire someone to do it—without rebuilding my whole stack.

**4. What happens to confidential data?**

Does the system train on it? Store it? Log it with human visibility? For estate planning—where we're handling beneficiary names, financial details, tax IDs—this isn't abstract. It's regulatory and reputational.

**5. Can I defend this choice to a regulator?**

If the FTC asks "why did you choose this LLM," can I explain it? Or did I just pick the one with the most TechCrunch hype?

Only one system answered all five clearly. But getting there meant eliminating four.

---

## Why Gemini Failed (Even Though It's Impressive)

Google shipped Gemini Enterprise for Legal in August 2026. It's good.

20+ connectors for legal systems. Contract lifecycle management. Cite verification. Regulatory tracking. It's polished.

Then I hit the architectural blocker: **Gems (Google's version of skills) cannot run concurrently.**

You pick one Gem per conversation. You cannot simultaneously query CourtListener for case law, pull DocuSign contract metadata, and extract Intercom support tickets in the same reasoning chain. You switch between Gems. Context breaks. Reasoning degrades.

For litigation, that's disqualifying. I need to cross-reference cases (CourtListener) with opposing counsel profiles, settlement precedents *in the same thought.* Gem-switching makes that workflow feel like writing an email with a different tab open for each paragraph.

Second problem: **NotebookLM hit storage walls immediately.**

NotebookLM is excellent for analyzing documents. It's also limited to 500K words per source and 200MB per upload. A multi-party litigation case with 5,000 documents? You hit the cap in the first half. Discovery is a fire hose; NotebookLM is a cup.

Third: **Data residency is unclear.**

Gemini uses Google Cloud. Google Cloud operates under the CLOUD Act, which means U.S. authorities can access U.S.-based servers without a warrant. For work involving privileged client data, that's a concern. Gemini Enterprise provides some privacy protections, but not absolute data residency control.

**Verdict on Gemini:** Impressive for general legal work. Disqualifying for multi-connector workflows, discovery-heavy litigation, or teams managing confidential family/financial data.

---

## Why OpenAI Failed (Because of Privilege, Not Capability)

OpenAI's ChatGPT Enterprise is also polished. SOC 2 compliance, audit logs, custom instructions, no training on your data (for Enterprise tiers).

Then the Heppner ruling landed.

**United States v. Heppner (SDNY, March 2026)** established: **AI conversations are not attorney-client privileged.**

Judge Jed S. Rakoff's reasoning: "Since AI tools do not hold law licenses, communications with them are by definition not lawyer-client communications, and thus are not subject to attorney-client privilege or attorney work product protections."

Let that sink in. Even with an enterprise agreement. Even with "no training on your data." The conversation can still be subpoenaed. Opposing counsel can demand the transcript. The AI's reasoning about your legal strategy is discoverable.

OpenAI's Enterprise agreement provides confidentiality. It does not provide privilege.

For a CLO, this is a hard stop. Your legal team is now creating discoverable evidence every time they ask an AI a legal question. That's a professional liability issue hiding in a feature launch.

ChatGPT has legal plugins emerging (DocuSign, compliance helpers), but no integrated legal-specific context architecture like Claude's. And now with the privilege gap, I'm not comfortable using it for sensitive work, no matter how good the features are.

**Verdict on OpenAI:** Capable, but unresolved privilege gap makes it risky for confidential legal work. Not my hill to die on.

---

## Why Grok Failed (Because There's No Governance)

xAI's Grok operates in a governance vacuum.

No published data privacy agreements. No enterprise compliance framework. No audit trails. Regulators in the U.S., UK, EU, and Malaysia are actively investigating xAI for harmful outputs and data handling. One jurisdiction flagged Grok as "what ungoverned AI looks like."

For a CLO, this isn't paranoia. This is risk management. If I deploy Grok on confidential legal work and regulators later find that xAI was extracting data or training on content without explicit safeguards, my company is liable. xAI isn't.

I'm not choosing the fastest or the cheapest. I'm choosing the one I can defend in court.

Grok doesn't make that list.

**Verdict on Grok:** Innovation is valueless if governance is absent. Not an option.

---

## Why Microsoft Copilot Failed (Ecosystem Lock)

Microsoft launched Copilot for Legal in April 2026. It integrates with SharePoint, OneDrive, Teams.

That's the feature and the constraint.

Copilot only talks to Microsoft 365. If your legal team uses iManage for contracts, Everlaw for e-discovery, or CourtListener for case research, Copilot forces you to export/re-import. No CourtListener native access. No concurrent workflow across your real legal systems.

Mid-market firms adopting cloud legal platforms (Ironclad, Box, Everlaw) find Copilot adds cost without workflow fit.

It's a well-designed system for firms living entirely in Office 365. For firms like Estate Guru—where we need CourtListener + PandaDoc + Intercom + Box all orchestrating together—it's a non-starter.

**Verdict on Microsoft Copilot:** Strong for Microsoft-native teams. Disqualifying if you use best-of-breed legal tech.

---

## Why OpenCode.ai Failed (Privacy Paradox)

OpenCode.ai is open source. Fully self-hosted. Your data never leaves your machine. True privacy.

I actually used OpenCode for a project. Privacy is real. But velocity is also real.

Here's the trade-off:

**Pros of OpenCode:**
- Open source, MIT-licensed
- Fully on-premises; no central platform
- Credentials stored locally
- Can run offline with Ollama/LM Studio
- True data residency control

**Cons:**
- Terminal-first interface
- No built-in legal connectors (you script them)
- Documentation is inconsistent; GitHub issues are your manual
- Non-technical paralegals cannot use it
- Multi-connector orchestration requires custom scripts (Python, shell)

Example: To run CourtListener + DocuSign + Intercom simultaneously in OpenCode, you're writing shell scripts. In Claude Code, those MCP servers are pre-built. A paralegal can describe the workflow in English. Claude Code handles the orchestration.

At scale, the productivity cost of "everyone must learn terminal commands" exceeds the privacy value of "data never leaves the server."

Privacy is table stakes. But if governance requires your entire team to become DevOps engineers, you lose the velocity that makes governance matter in the first place.

**Verdict on OpenCode.ai:** Privacy win, velocity loss. For large teams, the trade-off fails.

---

## Here's Why I Chose Claude Code (The Real Reasons)

I didn't pick Claude because it's the newest or the most hyped. I picked it because it solves all five questions I started with.

### 1. Concurrent Multi-Connector Workflows (MCP Architecture)

Claude uses Model Context Protocol—a standardized system for connecting to external tools.

**What this means:** I can describe a workflow once—"Find all cases citing [precedent] in CourtListener, cross-reference with our settlement agreements in PandaDoc, and flag upcoming compliance deadlines in Intercom"—and Claude simultaneously queries all three. No Gem-switching. No context loss.

May 2026, Anthropic shipped 20+ legal MCP connectors and 12 practice-area plugins. The ones I use constantly:
- **CourtListener:** PACER dockets, case law, judge profiles, oral arguments
- **Descrybe:** U.S. case law research, statute/regulation search, citation verification
- **Intercom:** Customer support patterns, paralegal case summaries
- **Box:** Secure client contracts, deal room documents, access controls
- **PandaDoc:** Document templates, signature tracking, contract obligations
- **Ironclad:** Contract repositories, approval workflows, deal metadata

These run concurrently. In one reasoning chain. That's not possible in Gemini, OpenAI, or Grok.

### 2. No Attorney-Client Privilege Liability (Yet)

Claude Code doesn't face the Heppner ruling—not yet. No court has ruled on Claude conversations specifically.

But Anthropic's architecture is different. Claude's API users get an explicit guarantee: "We do not use your prompts or uploaded documents to train our foundational models." This is contractual, auditable, and documented.

Will future courts extend Heppner to Claude? I don't know. But Anthropic's data handling is more defensible than OpenAI's post-Heppner exposure.

### 3. You Own the Integration Standard (MCP)

I'm not locked into Anthropic's choices.

Model Context Protocol is an open standard. If I need to integrate a proprietary legal system, I can build an MCP server or hire someone to do it. My whole architecture doesn't depend on Anthropic adding a connector for System X.

That's true vendor-independent integration. Gemini, OpenAI, and others use closed integration patterns. You're dependent on *their* roadmap for new connectors.

### 4. Legal Plugins Solve Specific Problems (CLAUDE.md + Skills)

Claude's legal ecosystem has 8+ practice-area plugins:

- **litigation-legal**: Demand drafting, deposition prep, privilege logging, subpoena triage
- **commercial-legal**: Contract review, NDAs, vendor agreements, renewal tracking
- **IP-legal**: Patent/trademark research, FTO analysis, invention intake
- **employment-legal**: Hiring review, termination, worker classification
- **product-legal**: Product launch review, marketing claims compliance
- **privacy-legal**: PIAs, DPA review, DSAR responses
- **corporate-legal**: M&A diligence, board minutes, integration management
- **regulatory-legal**: Regulatory gap analysis, compliance monitoring

I can layer multiple plugins. Each one encodes specific legal rules, vocabulary, and workflows.

And they all read from one source of truth: **CLAUDE.md**—my persistent context file that specifies my voice, my constraints, my risk appetite, my knowledge library.

No re-explanation to each agent. No prompt engineering every session. One source of truth, machine-readable, auditable.

That's governance by design.

### 5. Data Privacy That Matches Our Regulatory Reality

Claude API and Enterprise tiers don't train on user data. Full stop.

For estate planning work—where every client conversation involves beneficiary names, financial details, SSNs, family dynamics—this isn't marketing language. It's a compliance requirement.

GDPR (effective Aug 2, 2026) makes training-on-data a violation for LLM providers serving EU clients. CCPA requires opt-out language for automated decision-making. State bar ethics rules (Model Rule 1.6, Attorney-Client Privilege) assume strict confidentiality.

Using Gemini, OpenAI (free tier), or Grok for confidential legal work creates regulatory exposure that I can't defend.

Claude's guarantee is verifiable, contractual, and aligned with what legal teams actually need.

---

## The Trade-Offs (Be Honest About Them)

Claude Code isn't free.

**Cost:** Claude Pro is $20/month for individuals. Enterprise pricing starts at $100k+/year for teams. Gemini and OpenAI have comparable pricing at scale, but Claude's cheaper tier (Pro) offers more capability than competitors' $20 offerings.

**Speed:** Claude's inference is measurably slower than Gemini and some GPT-4 deployments. If you're optimizing for latency in high-volume customer workflows, Claude may not be ideal. But for legal operations—where reasoning accuracy > latency—this isn't a constraint.

**Learning Curve:** Claude's plugin system and MCP architecture require more upfront setup than just opening a web interface. The payoff is governance and auditability. The cost is initial implementation time.

**What I'm *Not* Giving Up:**
- Capability for legal work (Claude is stronger on reasoning than Gemini for complex legal questions)
- Data privacy (Claude's guarantee is better than alternatives)
- Vendor accountability (Anthropic's governance posture is market-leading)

---

## The Real Decision: Compliance First, Cost Second

You're not buying an LLM. You're buying a compliance system.

I'm not measuring tokens per dollar. I'm measuring auditability per dollar. Governability per dollar. Defensibility per dollar.

Claude Code + plugins + MCP + CLAUDE.md = governance infrastructure.

Yes, it costs more than Gemini. Yes, it's slower than GPT-4 Turbo. It's also defensible. If I have to explain this system to a regulator, I can. If I have to explain a cheaper LLM that trained on confidential data, I can't.

That's not a tech choice. That's a risk choice.

---

## What I'd Actually Change (If I Could Choose Again)

Three things:

**1. Concurrent MCP reliability at scale.** Multiple connectors running simultaneously are powerful, but error handling across five connectors is complex. I'd want better orchestration error logging (coming in Q4 2026, per Anthropic's roadmap).

**2. Privilege roadmap clarity.** I wish Anthropic had published a defense against the Heppner ruling. Something like: "Here's why Claude conversations have different privilege implications than OpenAI." They haven't. I'm betting on the architecture, but the ruling still hangs over it.

**3. Compliance documentation library.** Claude has strong governance, but Anthropic could ship a "legal compliance playbook"—templates for CLAUDE.md, skill governance frameworks, audit procedures. They're building this, but it's not there yet.

None of these are deal-breakers. All are solvable with 6–12 months of roadmap work.

---

## The Checklist I Used (Steal It)

If you're making this choice, here's the framework I used:

1. **Multi-connector concurrency:** Can the system run three tools simultaneously in one reasoning chain? (Yes/No)
2. **Privilege stability:** Is there a federal ruling against the system? (Yes/No, risk tier)
3. **Integration ownership:** Can I build connectors myself, or am I dependent on the vendor's roadmap? (Owned/Dependent)
4. **Legal plugins:** Are there pre-built skills for my practice area, or do I build from scratch? (Exists/Custom)
5. **Data confidentiality:** What's the written guarantee about training on user data? (Explicit/Vague/None)
6. **Governance auditability:** Can I document why I chose this system and defend it to a regulator? (Yes/No)

Score each system on all six. Gemini scored well on 1-2, weak on 3-6. OpenAI scored well on 1, 3-4, weak on 2 and 5. Claude scored well on all six.

That's the basis of the choice.

---

## What I'm Still Watching

**Heppner ruling ripple effects:** If courts extend the "no privilege for AI" ruling to Claude, the legal landscape shifts overnight. I'm monitoring federal courts and bar associations for parallel cases. (This is why you don't put all your compliance eggs in one system—you diversify, monitor, and re-evaluate quarterly.)

**Anthropic's consumer policy shift:** In September 2025, Anthropic changed Claude's consumer tier to an opt-out model for training data. That spooked me. It showed that even privacy-forward vendors can shift terms. Enterprise agreements are non-negotiable; they're not optional cost-saving measures.

**EU AI Act compliance:** Anthropic has a head start on this—watermarking, transparency, audit trails. But all vendors will be required to comply by August 2027. This is where the market consolidates around governance maturity, not inference speed.

---

## The Closing Move: You Can't Outsource This Choice

You might be tempted to hire a consultant. To outsource this to your LegalOps team. To pick the vendor that everyone else is picking.

Don't.

This choice is yours. Your risk appetite. Your regulatory exposure. Your team's workflow. Your client data security.

I spent two weeks evaluating these systems. I could have delegated it. But I'm the one who signs the data processing agreement. I'm the one who explains to the board why this system matters. I'm the one defending it to a regulator.

No consultant can own that accountability. Only you can.

---

## Three Ways to Use This Framework

Pick one:

**Option A — Competitive:**
I evaluated five systems. I eliminated four for specific reasons. Use my framework. Plug in your constraints. Tell me which system you'd choose and why. I'll tell you what you're giving up.

**Option B — Educational:**
I built a decision matrix to evaluate AI systems for legal operations. Here's the system prompt I used to conduct this analysis. Use it to audit your current AI choice. What did you optimize for? What did you miss? Reply with your findings—I want to know what's actually working (or not) in the field.

**Option C — Crowdsourced:**
Most CLOs guess at this. I measured. Here's my measurement framework: time audit + compliance gates + MCP ecosystem mapping. Use it. Adapt it. Build your own. Reply with your framework and let's crowdsource the real decision matrix for AI system selection.

---

## Next Week

Week 3: I'll walk through what I discovered when I asked Claude to analyze our entire legal operations structure—and what I found that we were doing wrong that we didn't know we were doing wrong.

For now: What's holding you back from building your own AI system? Is it vendor choice? Integration architecture? Governance? Tell me what's blocking you. That's what I want to solve next.
