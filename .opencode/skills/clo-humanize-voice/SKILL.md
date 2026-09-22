---
name: clo-humanize-voice
description: Rewrite an AI-drafted CLO Substack article, Note, email, or reply so it reads in Jared's own specific voice — staccato openings, concrete metaphors instead of abstractions, named tools/companies instead of generic claims, one fully-built CLO example, learning stated as a flat strength, and a specific call-to-action instead of a soft close for long-form. Final personal-voice layer on every output register. Trigger on "make this sound like me," "humanize this," "does this sound like Jared," or before any article, Note, email, or reply draft is called done.
---

# Humanize Output — Jared's Voice, Every Register

Built from Jared's actual published article ("You Can't Govern What You Don't
Understand"), two drafted long-form pieces, and a corpus of his sent emails.
Quick-reference format — jump to the section you need. This is the
personal-voice layer for everything Jared publishes or sends: articles,
Notes, emails, and replies each get their own register below, all in one
place so nothing has to be pulled from an external skill mid-draft.

**Where this sits in the pipeline:** `humanize-writing` fixes generic AI
tells (uniformity, hedging, performed significance). `estate-guru-brand-voice`
checks compliance and terminology. Neither of those makes a draft sound like
*Jared specifically* — that's this skill's job. Run it last, on a draft
that's already cleared the other two. If you're just told "make this sound
like me" on a short piece, it's fine to run this skill standalone.

---

## 1. Core Identity — Articles & Notes

Five assumptions run under everything Jared publishes long-form. (Email and
replies run on a different set of assumptions — see section 2 and
`references/email-voice-guide.md`.)

**Urgency first, thesis never.** He opens on the problem or the stakes, in
short sentences, not on a scene-setter or a topic sentence.

**Concrete beats abstract, every time.** A real metaphor or a real number
replaces a general claim. "Significant risk" never survives a pass; "bring
down the house" does.

**Specificity is credibility.** He names the tool, the company, the number.
Never "AI tools" — always "Claude Code, Gemini, Grok, N8N, Eleven Labs."
Never "a tech company" — always "Underline provides estate planning
technology to attorneys in every state."

**One real example, fully built, beats five scattered ones.** Problem →
complication → what he built → the process → the outcome, told as a story,
not fragmented into bullets.

**Learning is a credibility flex, not a hedge.** "I'm still learning" stands
alone. It never gets a defensive follow-up bolted on.

---

## 2. Registers

Voice flexes by format — don't apply full-article structure to a two-line
Note.

**Full Substack article** — staccato open stating the stakes, 2–4 grounded
middle sections built around one real EstateGuru example, closes with a
specific, often multi-option call-to-action (see the "Reply with
WIKI/SKILLS/AUDIT/WALKTHROUGH" pattern in `references/article-examples.md`).

**Note (short-form)** — same staccato rhythm and at least one metaphor,
compressed to a few lines. There's no room for the full built-example arc, so
it needs to land on one sharp, specific claim instead of trying to compress
the whole story.

**Email or reply (a draft Jared will review before sending)** — a different
voice entirely from articles: plainer, faster, tied to one recipient and one
action. Article voice is for public writing that builds authority;
email/reply voice is for moving one specific thing forward with one
specific person. Full detail — five registers (cold outreach, internal
directive, follow-up, feedback, casual check-in), sentence patterns, and a
six-point calibration check — lives in
`references/email-voice-guide.md`; load it for any email or reply draft.
Condensed version if you just need the shape:
- Open with a bare first name for someone he knows (no "Hi," no comma), or
  one sentence of self-ID for a new contact.
- State the ask in the first or second sentence — no warm-up beyond one
  specific, real personal beat.
- Number anything with more than one item; never bury multiple asks in a
  paragraph.
- Name the specific uncertainty ("Not sure of comma, spelling...") instead
  of a vague hedge.
- Close with "Thanks, Jared" (internal) or "Thank you, Jared Moss" plus
  phone number (external/regulatory) — never "Best regards" or "Sincerely."

---

## 3. Sentence-Level Patterns — Articles & Notes

**Staccato opening.** Three to five words per sentence. No hedging, no
connectors joining them into one longer sentence.

**Unqualified warning.** "Will undeniably," never "might" or "could
potentially."

**Metaphor, not abstraction, for risk or change.** F1 pace. Ejected. Bring
down the house. The metaphor has to be visual — something the reader can
picture, not a bigger adjective.

**Professional language stated straight, then confronted.** Actual ABA rule
language (or whatever the real governing rule is) gets quoted, not
paraphrased into mush — then followed by a direct question that puts the
tension on the reader ("How are you zealous and competent at the same
time?").

**The built-example arc.** Problem stated with a real timeframe ("Three
months ago I needed to...") → the complication ("it's complicated, there are
no model rules yet") → what he built, tools named → the process as a visible
chain ("search → compile → cross-reference → map → automate") → the outcome,
with a number attached.

---

## 4. Rhetorical Moves — Articles & Notes

**Opens on stakes, never on throat-clearing.** No "In today's fast-paced
world."

**Cites something real, then asks the reader a direct question about their
own situation.** Not a rhetorical flourish — an actual question expecting an
answer.

**Tells one story problem → solution → outcome**, instead of a bulleted
generic framework.

**States what he doesn't know as a flat fact.** No defensive qualifier
chasing it.

**Closes with a named, specific action.** Often several lettered or worded
options, each with a one-word reply trigger ("Reply with WIKI"), not a soft
"let me know your thoughts."

---

## 5. Good vs. Bad — the tuning table

This is the part to edit when a draft comes back wrong. Tell Claude to swap
a Bad example for one it actually produced that you didn't like, add a new
row for a pattern you're seeing drift, or strike a row that no longer
applies — this table is the fine-tuning surface for this skill, not a fixed
list. Rows 1–8 are article/Notes voice; rows 9–10 are email/reply voice (the
fuller email-specific Do's/Don'ts list lives in
`references/email-voice-guide.md` section 6 — add rows there for anything
email-specific beyond these two).

| # | Pattern | GOOD (keep) | BAD (regression) |
|---|---|---|---|
| 1 | Staccato opening | "Tech companies move fast. Push boundaries. Aggressively pursue customer acquisition or revenue growth. If you don't understand these emerging technologies, you will undeniably hit a fork in the road and may be ejected." | "Tech companies are known for moving quickly and pushing boundaries as they aggressively pursue customer acquisition and revenue growth. It is important that you understand emerging technologies, or you may find yourself excluded from critical decision-making." |
| 2 | Metaphor over abstraction | "Tech companies are moving at F1 pace with the recent horsepower of AI." | "Tech companies are experiencing rapid technological advancement." |
| 3 | Named tools, not generic | "I use Claude Code, Gemini, Grok, N8N, and Eleven Labs." | "I use a variety of AI tools." |
| 4 | Named company, not generic | "Underline provides estate planning technology to attorneys in every state." | "I work at a tech company in the legal space." |
| 5 | One full real example | "Three months ago I needed to understand what disclaimers, if any, are required for a chatbot that answers questions about a client's estate documents... I built a database using Claude Code. Result: a 50-state review that updates automatically every 30 days." | "I recently undertook a comprehensive review of AI regulations across multiple states to ensure compliance with various legal requirements in different jurisdictions." |
| 6 | Learning stated as strength, unqualified | "I'm still learning. I rely on the experts to make it excellent." | "I'm still learning, but I've done extensive research and feel confident in my understanding." |
| 7 | Specific call-to-action | "I used Claude Code to build the 50-state AI legislation tracker. If you want the exact system prompt, reply with PROMPT and I'll send it to you." | "I'm happy to discuss my approach further. Please feel free to contact me if you have any questions or would like more information." |
| 8 | Unqualified claim | "You will undeniably hit a fork in the road." | "You might hit a fork in the road at some point." |
| 9 | Email open, known contact | "Bill —" (bare first name, own line, no comma) | "Hi Bill, I hope this email finds you well." |
| 10 | Email close | "Thank you, Jared Moss / 619-573-7900" | "Best regards, Jared Moss" |

---

## 6. Voice Calibration Tests — Articles & Notes

Run a draft against these seven yes/no checks. Fail two or more and it needs
another pass before it sounds like Jared. (For email/replies, use the
six-point check in `references/email-voice-guide.md` section 8 instead —
different register, different checks.)

1. **Urgency** — Does it open on the problem or the stakes, not a thesis or
   a scene-setter?
2. **Metaphor** — Is there at least one concrete, visual metaphor for risk
   or change, not just a bigger abstraction?
3. **Specificity** — Does it name the actual tools, companies, or numbers
   instead of "AI tools," "a client," or "many teams"?
4. **Grounding** — Is it built on one real, fully-told EstateGuru example
   (problem → build → outcome), not several scattered hypotheticals?
5. **Authority** — Is real rule language (ABA, statute, case) quoted
   straight, not paraphrased into something softer?
6. **Honesty** — Is what he's still learning stated as a flat fact, with no
   defensive hedge stapled on after it?
7. **Call to action** — Does it end with something a reader can literally
   act on — a word to reply with, a concrete ask — not "let me know your
   thoughts"?

---

## References & Memory

- `references/article-examples.md` — the two full drafted articles this
  skill was built from, for calibrating a whole piece rather than a single
  sentence.
- `references/email-voice-guide.md` — the full email/reply register: five
  sub-registers (cold outreach, internal directive, follow-up, feedback,
  casual check-in), sentence patterns, rhetorical moves, a quick-reference
  table, and its own six-point calibration check, built from a corpus of
  Jared's actual sent emails. Load this for any email or reply draft instead
  of trying to force article voice onto it.
- `/memory/jared-voice-profile.md` — the durable facts this skill draws on
  but doesn't duplicate: ABA rule citations, EstateGuru/Underline specifics,
  the tech stack Jared names, and a running log of which real proof points
  (Advisor Set Pricing, the knowledge wiki, the 50-state tracker) have
  already been used in a post, so a new draft doesn't quietly reuse the same
  story. Check it before building the "one real example" section of a new
  draft.
