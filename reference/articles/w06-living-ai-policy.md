# Your AI Policy Is a Dead Document. Build a Living One.

43% of legal teams have no AI policy. None. No plans to write one.

That's not caution. That's a bet that the rules won't catch up.

They're catching up.

Last month a founder asked me: "What's your AI policy?" I didn't send her a PDF. I opened a folder of markdown files on my laptop. Fifty-plus articles. Entity structure. UPL constraints. The 50-state AI regulation landscape. How my legal team uses Claude and what they're never allowed to feed it. Every article timestamped, sourced, and scored for how much I trust it.

She said: "That's your policy?"

That's the whole thing. And it updates itself every month.

---

## What a Wiki Actually Is

A knowledge wiki is a folder of plain markdown files that an AI agent reads, writes, and maintains for you. Each file covers one entity: a person, a project, a decision, a compliance pattern. Files link to each other with `[[wikilinks]]`, so the agent can follow a thread instead of re-reading everything.

The difference between a wiki and a policy document is that the agent maintains the wiki. You don't.

Andrej Karpathy published the canonical version of this pattern in April 2026. His framing: today's AI re-retrieves the same raw sources over and over, and nothing accumulates. A wiki inverts it. The LLM compiles raw sources into structured, interlinked pages once, then queries the wiki instead of the sources. Knowledge compounds. Read [his gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). It's short.

I built mine in Claude Code following the Leland AI Builder curriculum. It took a day to scaffold and another day to get it working with an evaluation loop.

---

## The Rule That Makes This Mandatory

ABA Formal Opinion 512, July 2024. First formal guidance on generative AI. It didn't invent a new rule. It pointed at Rule 1.1 and said competence now covers AI.

Competence means you can answer three questions:

1. What is the AI actually doing in your legal operations?
2. Where can it break, and what happens when it does?
3. Can you explain both to your board?

California went further. In March 2026 its Standing Committee approved proposed amendments to Rules 1.1, 1.4, 1.6, 3.3, 5.1, and 5.3. Those are disciplinary rules, not advisory opinions. They carry sanctions.

And courts are already moving. U.S. courts imposed over $145,000 in AI-filing sanctions in Q1 2026 alone. Lawyers filed hallucinated citations from tools they didn't understand. A Stanford study found leading legal research tools hallucinate on 17% to 34% of queries.

Here's the part that should worry you. When a regulator asks "do you have an AI policy," the answer isn't yes or no. The answer is: show me. A PDF you wrote in 2025 and never opened again doesn't survive that question. It proves you wrote a document. It doesn't prove you are still paying attention.

---

## The Industry Is Already Past You

87% of general counsel report using generative AI. That's up from 44% in 2025 and 20% in 2023. 92% of legal professionals touch at least one AI tool daily.

The time savings are real. 38% of lawyers save one to five hours a week. 14% save six to ten hours. Call it 260 hours a year, which is 32 working days you get back.

The money is real too. AI could save the U.S. legal industry roughly $20 billion a year. 50% of legal organizations reported revenue increases after implementation.

And the infrastructure is consolidating fast. Thomson Reuters bought Casetext and folded CoCounsel into Westlaw and Practical Law. LexisNexis renamed Lexis+ AI to Lexis+ with Protégé in February 2026.

Then look at Harvey. Founded 2022. AI-native from day one. On September 9, one week before I wrote this, it raised $550 million at a $15.5 billion valuation. More than $1.5 billion raised total. ARR above $400 million. Customers went from roughly 1,300 in March to over 3,000 now.

That's the market telling you where legal work is going. Harvey didn't retrofit AI onto a legacy research product. It started there.

Now the gap. 87% of CLOs use AI. 56% are using general-purpose tools like ChatGPT. Only 14% have adopted purpose-built legal tools with real governance. Less than half of firms train anyone on responsible use.

Usage went vertical. Governance didn't move. That gap is where the sanctions live.

---

## What I Built and Why

I run legal at Estate Guru. We provide estate planning technology to attorneys in every state, which means UPL constraints in 50 jurisdictions, attorney-client privilege running through a software platform, and a network of contracted attorneys who each carry their own bar obligations.

The question that started this: what disclaimers, if any, does a chatbot need when it answers questions about a client's estate documents?

There was no clean answer. No model rule. Fifty different state positions, some passed, some pending, cross-cut by FTC guidance. I couldn't find a single current source, so I built one.

That research became the first real article in my wiki. Then I kept going.

My wiki has five article types:

**People.** My legal team and the exec roster. Roles, how each person works, what they own.

**Priorities.** Active projects with real status and next milestones. Limited-scope legal services. The attorney product demo. The MSA network strategy.

**Company reference.** Facts that rarely change. Entity structure across WDEP, Estate Guru, Underline. The UPL rationale. Money transmission exemptions.

**Compliance patterns.** Generalizable lessons stripped of client identifiers. UPL-safe phrasing with banned phrases mapped to compliant alternatives. Recurring advisor questions.

**Playbook.** The frameworks. Risk and judgment. Voice and communication. AI regulation and governance.

Two rules make it defensible rather than just organized.

Every article opens with a source line and a confidence score from 0.0 to 1.0. The score tracks how directly the fact came from me. My own statements score 0.85 and up. Meeting transcripts land between 0.6 and 0.84. Secondhand accounts sit lower. Pure inference scores under 0.34. Anything below 0.5 gets flagged for review.

When sources conflict, the higher-authority source wins, and the superseded claim stays in the log rather than getting quietly overwritten. That's the audit trail. It shows not just what I concluded but what I considered and rejected.

I'm still learning this. I lean on the Leland curriculum and on people who build these systems full time. But the wiki is mine, it's running, and it answers the regulator's question.

---

## The Monthly Loop That Makes It Live

A wiki you build once and abandon is just a slower PDF. What turns it into living knowledge is two skills running on a schedule.

**`/ingest`** takes any new source, a Slack thread, a meeting transcript, a doc, a URL, and distills it into articles. Not a copy. It extracts durable facts and decisions, updates whichever existing articles the information touches, creates new ones where nothing related exists, adds wikilinks, and appends to the change log.

**`/lint`** is the health check. It reads every article and reports orphans, stale facts, contradictions between articles, and anything scoring below 0.5 confidence. It's read-only by design. It never edits or deletes on its own. It hands me a numbered list and I approve or reject each item.

Then you put `/lint` in the cloud so it runs whether or not your laptop is open. Here's the setup in the Claude Code desktop app:

1. Sidebar → Routines → New routine → Remote.
2. Name it Wiki Refresh. Model: Sonnet.
3. Paste a prompt telling it to run the lint pass and report findings as a numbered list with reasons, and to change nothing.
4. Under Repositories, add your wiki repo. Remote routines clone it at the start of each run.
5. In the Connectors tab, check only the tools it actually needs. Scope tight.
6. Set the trigger to Schedule, monthly, first of the month.
7. Create, then hit Run now to confirm it works before trusting the schedule.

Mine reports on the first of every month. I spend twenty minutes reviewing what it found, approve the fixes, and the wiki is current again.

That loop is the whole argument. Ingest adds knowledge. Lint catches decay. Confidence scores flag what was never verified. The schedule means it happens whether or not I remember. And I stay in the approval seat the entire time, which is where my professional judgment has to live anyway.

That's not a document. That's a governance system.

---

## Build Yours in Four Steps

This is the Leland L2S3 build, compressed.

**Step 1: Scope it before you create anything.**

Have your agent interview you. Your role and daily work. The people you work with. Your top three to five priorities. How you communicate. What's in scope and out of scope. One question at a time. Make it draft answers from what it already knows and cite where each came from, so you're confirming rather than dictating.

Then have it propose article types from that conversation. Not generic defaults. Yours.

**Step 2: Scaffold the structure and write the operating contract.**

```
knowledge-wiki/
├── CLAUDE.md
├── index.md
├── log.md
├── raw/
└── articles/
    ├── [type-1]/
    └── [type-N]/
```

The wiki's own CLAUDE.md is the operating contract. It defines what the wiki is for, the article types with an example each, the folder convention, the navigation rule, the source citation format, and the maintenance protocol. Add the source authority hierarchy and confidence scoring here. This file governs every article you add from here forward, so get it right before you fill anything in.

**Step 3: Capture wide, then distill.**

Drop real sources into `raw/` without filtering. Meeting notes. Role descriptions. Project docs. Anything naming your people or projects. Filtering at capture time is how you lose the thing you needed six months later.

Then have the agent read `raw/` and generate articles per your article types, updating `index.md` and appending to `log.md`. Review what it produced. Edit one yourself. Approve one as-is. Send one back for revision. That habit keeps you in the editor's seat.

Then add `[[wikilinks]]` between related articles. Open the folder in Obsidian and look at Graph View. Isolated nodes mean you need more cross-linking.

**Step 4: Build `/ingest` and `/lint`, then schedule the lint.**

Turn the manual prompts into slash-command skills in `.claude/skills/`. Test both. Then wire lint to a monthly remote routine as described above.

A weekend to scaffold. A month of feeding it. Then it maintains itself with twenty minutes of your review a month.

---

## Four Ways Forward

**Reply with WIKI** and I'll send you my wiki's CLAUDE.md operating contract, the article type definitions, and the source authority and confidence scoring rules. Strip out my Estate Guru specifics and you have a working skeleton.

**Reply with SKILLS** and I'll send the exact `/ingest` and `/lint` skill files plus the monthly remote routine prompt. Drop them in `.claude/skills/` and they run.

**Reply with AUDIT** with a short summary of what AI currently touches in your legal operations. I'll tell you which article types to build first and where your biggest documentation gap is.

**Reply with WALKTHROUGH** and I'll run a live 90-minute session on how I scoped mine, how the confidence scoring works in practice, and how to wire the monthly loop.

---

## The Close

Most CLOs think a policy protects them. It doesn't. The document isn't the protection. The evidence that you were paying attention is the protection.

A wiki produces that evidence as a byproduct of being useful. Every source line. Every confidence score. Every superseded claim in the log. Every monthly lint pass showing you checked. That's not bureaucracy. That's the paper trail you'll want when someone asks what you knew and when you knew it.

The 43% without a policy aren't being careful. They're uninsured.

Build the wiki. Feed it. Schedule the lint. Show your work.

---

## Next Week

How to put your wiki in front of your board. What they need to see, what they don't, and how to move the conversation from "do we have a policy" to "how fast can we ship."

For now: what's the messiest part of your current AI practices? Where do you most want clarity? That's the first article. Reply and tell me.
