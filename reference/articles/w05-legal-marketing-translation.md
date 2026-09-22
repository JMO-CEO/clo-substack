# Legal and Marketing Don't Have a Trust Problem. They Have a Translation Problem.

54% of marketing leaders name legal review as a top-three barrier to campaign speed. Not budget. Not creative. Legal review itself.

My CMO put it more bluntly last quarter: "Why does it take legal two weeks to approve marketing copy?"

She wasn't really asking about speed. She was asking why legal and marketing can't just talk to each other.

Here's the answer. Legal writing hedges, discloses, and buries the strongest claim under three qualifiers. Marketing writing leads with the benefit and asks the reader to trust it. Same facts, opposite instincts. Put them in a room together after the copy is already written, and you get a fight, not a review.

So we stopped doing it after the copy was written.

---

## Why "Helps" and "Ensures" Are Not the Same Word

For a legal-tech company, this isn't a style disagreement. It's ABA Model Rules 7.1 through 7.4 territory. A claim can be completely true and still be misleading if it implies a result the facts don't support. "Helps attorneys manage compliance" clears that bar. "Ensures compliance" doesn't. One word, and it's the difference between a marketing line and a bar complaint.

Marketing people are trained to sell outcomes. Lawyers are trained to never promise one. Neither side is wrong. They're optimizing for different things, and nobody had written down where the line actually sits.

That gap is where every slow review lives.

---

## What Slow Review Actually Costs

The ABA's own 2024 tech survey put average manual compliance review, in regulated industries, at two to three weeks per campaign. One CPG marketer I read about saw legal turnaround jump from 3 days to 11 after EU enforcement action on AI-related claims. Turnaround didn't get slower because the law changed that much. It got slower because nobody had a framework, so every claim got treated as a fresh judgment call.

Multiply that by every campaign, every landing page, every rebrand. Your product team ships weekly. Your marketing team ships quarterly, and legal is the reason why.

That's not caution. That's drag with no safety benefit, because slow review isn't more accurate review. It's just slower.

---

## What I Built and Why

Our co-counsel network Dumbar was mid-rebrand this year. New site, new brand identity, new positioning, all built with their design agency. Attorney-facing platforms can't touch messaging casually. Every claim about compliance capability, attorney conduct, or malpractice coverage sits inside UPL boundaries and bar advertising rules.

The old model was: marketing writes, legal reads everything, legal sends it back. That model works. It also would have taken the rebrand past six months and left marketing resenting legal by month two.

So instead of reviewing output, I built a framework marketing could check their own work against.

I wrote a CLAUDE.md file scoped to marketing claims specifically, not a legal memo, a working reference. It covers which claim categories are safe to ship without review, which need a legal pass, which need outside counsel, and the exact phrasing that's already survived bar scrutiny. "Helps manage compliance" is in the safe column with a note explaining why. "Ensures compliance" is flagged, with the rule it violates named next to it.

Then I fed that file into Claude for Legal's product-legal marketing-claims-review skill. Marketing drops a draft claim in, and the skill checks it against the framework, tells them which bucket it falls into, and suggests the safe phrasing when something is close but not quite there. Anything genuinely new gets flagged for me or outside counsel. Everything else, marketing ships on their own.

My paralegal team got the same file. Their job isn't reading every draft that goes out. It's watching what ships, flagging anything that drifts from the framework, and updating the safe-phrasing list when new bar guidance lands. They're also running it against everything already published: the help center, the blog, old landing pages. Same framework, same categories, applied backward.

---

## Why This Actually Moved

Before: marketing writes, legal reads it in three to five days, sends back one or two rounds of changes, marketing revises, legal signs off. Two to three weeks, most weeks.

After: marketing checks the claim against the framework themselves, adjusts the one or two things the plugin flags, and ships. Legal sees only what genuinely needs judgment. Three to five days, most weeks.

Dumbar's full rebrand went from a projected six-month legal-gated timeline to ten weeks, with legal touching maybe a dozen pages out of hundreds.

The part that mattered wasn't the plugin. It was that the framework was visible. Marketing wasn't guessing whether legal would approve something anymore. They could read the file and know before they wrote a word.

This only holds if the framework itself is right, built from actual bar opinions and real review history, not a quick checklist someone wrote in an afternoon. And it only holds if someone keeps updating it. Ours came out of eighteen months of real compliance decisions. That's why marketing trusts it enough to ship without me in the loop.

---

## Build Yours in Three Steps

**Step 1: Pick one claim category, not all of them.** Don't try to write a framework for every kind of marketing claim your company makes. Pick the one that generates the most legal review requests right now. For us that was attorney-capability claims. For a fintech it might be rate or return language. Scope tight or the file never gets written.

**Step 2: Write the file from real decisions, not hypotheticals.** Pull your last twelve months of marketing legal reviews. What got approved, what got rejected, and why. Turn the why into the safe-phrasing list and the escalation rule. A framework built from actual precedent is one marketing will trust. One built from a Tuesday-afternoon guess isn't.

**Step 3: Give marketing the file before you give them the plugin.** The plugin is convenient. The file is what actually builds trust, because marketing can read it themselves and see the reasoning, not just get a yes or no from a tool. Once they trust the file, wire it into the review skill so checking it takes thirty seconds instead of a Slack message to legal.

---

## Four Ways Forward

**Reply with FRAMEWORK** and I'll send the exact structure of the CLAUDE.md file: the claim categories, the safe-phrasing list format, and the escalation matrix. Strip out our specifics and it's a skeleton for any regulated marketing team.

**Reply with PLUGIN** and I'll walk you through setting up the product-legal marketing-claims-review skill, feeding it your framework, and wiring it into how your marketing team actually works day to day.

**Reply with AUDIT** and send me your last three campaigns that hit legal friction. I'll tell you what triggered the delay and where a framework would have changed the timeline.

**Reply with BUILD** and tell me your single biggest marketing claim category, the one you write about most. I'll help you scope that one framework first, before you try to boil the ocean.

---

## The Close

Most legal teams think the choice is speed or safety. It isn't. The choice is whether your judgment lives in your head, where marketing has to guess at it every time, or in a framework marketing can read for themselves.

Gatekeeping doesn't make compliance better. It just makes it slower, and slower isn't the same thing as safer.

Write the framework once. Let marketing check their own work against it. Save your actual judgment for the calls that need it.

---

## Next Week

Week 7 covers the flip side: when to be stricter, even if it costs velocity. Not every claim belongs in a framework. Some need you in the room every time.

For now: what's the one marketing claim category that keeps landing on your desk? That's the framework worth building first.
