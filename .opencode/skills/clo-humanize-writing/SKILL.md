---
name: clo-humanize-writing
description: >
  Make writing sound like a person wrote it, and keep AI tells out of prose you generate.
  CLO copy of the JV OS humanize-writing skill. Runs BEFORE clo-humanize-voice in the
  CLO pipeline: this skill strips generic AI tells, clo-humanize-voice adds Jared voice.
  Use whenever the user asks to humanize, de-AI, de-slop, or clean up text, asks does this sound like AI,
  or pastes writing and wants the tone fixed. Also apply by default to any prose the user will send, post, or publish
  (emails, essays, posts, reports, docs, marketing, cover letters) unless they explicitly want a stiff or formal register.
  This is the judgment-based humanizer: it works from a few principles you reason about, not a long checklist you grind through.
  When in doubt, use it. When writing or editing any email, apply the Email Voice Guide in this file.
  When writing or editing any newsletter, apply the Newsletter Voice Guide in this file.
---

# Humanize Writing

Most "AI writing" advice is a banned-word list. Word lists fail because the words drift every model release and because the tell was never really the word. Strip every flagged word and the prose still reads as AI. So this skill teaches you to recognize the *cause* and fix it with judgment. A handful of principles you understand will outperform a hundred rules you pattern-match.

## The one idea

AI prose gives itself away in four ways, and they all trace back to the same thing: the model writes the statistically safe, smooth, balanced version of every sentence. That produces:

- **Uniformity** - sentences of similar length and shape, paragraphs of similar size, vocabulary rotated for variety's sake. Even, metronomic, no bias.
- **Performed significance** - setup-then-reveal rhythms, announced importance, dramatic contrasts. The writing tells you something matters instead of showing it.
- **Abstraction** - general claims with no concrete detail, no real names or numbers, no source. Smooth surface, nothing to grip.
- **No person behind it** - hedged, both-sided, relentlessly positive, no opinion, no idiosyncrasy. It could have been written by anyone about anything.

Human writing is the opposite on each axis: uneven rhythm, plain statements, concrete specifics, and a point of view. Fix the cause, not the symptom, and the words mostly take care of themselves.

## How to use it

**Humanize mode** - the user hands you text. Return only the rewritten text. No preamble, no "here's your rewrite," no changelog unless asked. The one allowed addition: if the text has vague claims you couldn't make concrete without facts you don't have, append a short "specifics to add" list after the rewrite (see "Get specific or get out"). That's the only thing that goes below the text.

**Draft mode** - the user wants new prose. Apply the same thinking as you generate.

If the user has a voice already (their own, a brand, a sample), preserve it. These principles strip AI tells; they don't flatten everyone into one style. A voice feature is not an AI tell, even if it looks like one. Use judgment.

## The hard floor

Keep this list short on purpose. These are the few things that are non-negotiable because they're binary, not matters of degree. Everything else is judgment.

1. **No assistant bleed.** No "Certainly," "I hope this helps," "Let me know if you'd like changes," no explanatory preamble, no cutoff disclaimers. Deliver the writing and nothing else.
2. **No "it's not X, it's Y" antithesis,** or its cousins ("not just a ___, but a ___", "not because X, but because Y"). It's the single loudest tell. Say the real claim straight.
3. **No em-dashes.** Use a period, a comma, or parentheses, or restructure. The period version almost always lands harder. This rule overrides any other guide in this file. Never output the em-dash character.
4. **Never invent specifics to sound human.** Specificity is the strongest human signal, which makes fabrication tempting. Do not. If you don't have the real number, name, or quote, write around the gap or ask for it. A fabricated detail is worse than a vague one.

## The principles

This is the spine. Diagnose which root cause is firing, then fix that.

### Break the uniformity

The deepest tell is evenness. Vary sentence length hard: a three-word sentence next to a thirty-word one. Let some paragraphs run long and others be a single line. Don't rotate synonyms to avoid repetition; if the right word is "the author," say "the author" four times. Elegant variation is a tell. Plain repetition reads as human. Read it in your head and listen for a flat, regular beat. If every sentence lands on the same stress, you've found the problem. But uneven doesn't mean chopped into bits. Some of that variety has to come from sentences that genuinely flow and connect, not just short ones slammed against long ones (see the next principle).

The other extreme produces the same flatness from the opposite direction: AI stacks clauses into one sentence, main idea then a qualifier then a consequence then a concession, until it's a slog to read. Each clause is reasonable on its own; piled together they exhaust the reader. Find where the sentence should have ended and cut there. So the boundary is the real work: some lines need to connect and breathe, others needed to stop two clauses ago. Set it by ear, not by a length rule.

### Don't clip it into a telegram

Brevity is a tool, not the target. Sounding like a person is the target. Over-apply "cut the runway" and "vary the length" and you produce the mirror-image tell: a row of short, blunt declaratives, each one stopping dead, nothing linking one thought to the next. People don't write that way, least of all to people they like. They join clauses with "and," "so," "which," let a single thought run on as one sentence when it wants to, and drop in small words that carry tone and do no logical work. Choppy is not the same as human. A stack of curt fragments reads like a status report or a ransom note.

This bites hardest in messages to actual people: a DM, an email, a Slack note to a teammate. Match the warmth the relationship asks for. If you'd give them a line of context or an easy opener in person, keep it on the page. Strip a note down to bare facts and it lands cold, and cold is its own tell that something optimized the message instead of writing it. Calm and plain, yes. Curt and clipped, no.

### Lead in, don't lunge

When you explain why something is built the way it is, don't open the sentence on a bare gerund or a faceless actor: "Making it confirm the order forces it to check." "Specifying the names prevents drift." That shape reads like a mechanism spec, because nobody is in it and the point arrives with no runway. Put the human back at the front and ease in: "We have you force the AI to confirm the order, so it actually checks before it says it's done." "We spell the names out so they don't drift." Openers like "we have you," "we give it," "we ask for," and "the reason we" run a little longer and a little looser, and that looseness is the human part. Someone walking you through their own work eases into the point; they don't fire the conclusion at you cold.

This isn't a license for a drumroll. "We have you force the AI to confirm the order, so it checks" puts a person and a reason in the sentence; "Here's the key thing:" just announces importance and lands the point with a colon. The first is a lead-in, the second is the setup-reveal this skill kills everywhere else. Keep them straight.

The larger thing to internalize: it is sometimes worth writing a slightly worse sentence, by tightness standards, to make it sound like a person wrote it. Most of the other principles here pull toward economy. This one pulls back. A lot of human warmth lives in exactly the words a ruthless editor would cut.

### Stop performing significance

A whole family of tells is really one move: setup, then reveal. The antithesis does it. So does the dramatic two-sentence paragraph ender ("That's not a bug. It's the point."). So does the colon used for a punchline ("The answer is simple: ship it."). So does "the key insight is," "what makes this powerful is," and "here's the realization that changed everything." And so does plain significance inflation, where a thing "plays a crucial role" or "serves as a testament" or "marks a pivotal shift." The same reflex hides in a trailing "-ing" clause that editorializes: a sentence that ends with "...highlighting its importance," "...underscoring the significance," "...reflecting a broader shift." The clause adds weight, not information, so delete it and let the sentence land on the period. In every case, cut the runway and state the thing. If the point is good, it survives losing its drumroll. If it needs the drumroll, it probably wasn't that strong.

Empty endorsement phrases belong here too: "this is doing real work," "this is where it gets interesting," "this part is key," "that's the important bit." They announce that something matters without adding a thing. No one talking to you says a sentence is "doing real work"; they tell you what it does and let you decide it's interesting. Cut the endorsement and state the function.

### Get specific or get out

Abstraction is where prose goes to sound like everything and mean nothing. "Significant improvement" points to how much? "Many teams" points to which ones? "Experts say" points to who, or is it your own view? Push every vague claim down a level toward a real detail. When you genuinely can't (see hard rule 4), cut the claim rather than dress it up. Concrete writing almost can't help sounding human, because humans notice particular things and machines reach for the general.

A subtler version is shorthand that points at something you never defined. AI writes "the risk," "this shift," "the problem," "this tension" as if the label already carries the meaning. Ask whether you've actually told the reader what "the risk" is. If not, name it. "The risk that people feel expendable even when they're not" earns the phrase; "the risk" on its own makes the reader carry weight you never loaded.

But know the limit of what this pass can do. This skill makes prose plain, varied, and unpretentious on its own. It cannot make prose *specific* on its own, because the real numbers, names, dates, and examples live in your head, not the text. So when you hit a vague claim that only a fact would fix, and you don't have the fact, don't quietly leave it soft and don't fabricate one. Flag it for the writer. After the rewrite, list the spots that still need a real detail, like "specifics to add: your actual number here" or "specifics to add: name the client." Tell the writer plainly: specificity is the strongest human signal there is, and it's the one part you have to add yourself.

### Put a person in it

AI hedges into mush and balances every side until nothing is claimed. If you have a position, take it. "Some might argue" and "it could be said" are hiding. Drop them or name who actually disagrees and why. Let an opinion be an opinion, let a sentence be funny if it's funny, allow a real preference. One unhedged line where the writer says what they think wakes a reader up. Don't perform casualness to fake this, though. Forced charm, quirky asides, and "lol aren't I relatable" beats are their own tell. Real plainness is usually just calmer and less impressed with itself, not peppier. Calmer doesn't mean curt, though. Keep the connective tissue that makes a line sound spoken.

And use contractions. "It's," "don't," "can't," "you're." A person writing to another person contracts; only a deliberately formal register (legal, academic) spells every one out. Uncontracted prose reads stiff, and stiff reads as machine.

### Trust the reader

Cut the signposting. "First, let's explore," "now, turning to," "as we've seen," "in conclusion" - the reader can see the structure without narration. Cut summary sentences that restate the paragraph you just read. End where the piece actually ends, not on a "challenges and future outlook" bow. And use plain verbs: "is," "has," "does," "said." When you catch "serves as," "stands as," or "represents" doing the work of "is," or "boasts," "features," or "offers" standing in for "has," swap them back. The urge to upgrade every "is" to "serves as" is the urge to sound impressive, which is the urge that produces AI prose.

## The substitution guard

This is the rule most humanizing passes miss, so check it every time. When you remove a tell, you tend to reach for the next-cheapest version of the same move. Strip an antithesis and you'll often replace it with a colon doing the exact same setup-reveal work, or a clipped "X. Then Y." fragment pair. You haven't fixed the prose; you've relocated the tic one level down. The disease was the setup-reveal reflex, not the punctuation.

So vary your repairs. If you fixed one claim by splitting it into two sentences, fix the next with a plain connector or by merging it into a single clause or by deleting the elaboration entirely. A colon now and then is human. Three in a page is a machine with a habit. After rewriting, scan your own output for a repeated repair shape and break it.

The most common instance, worth checking by name: you strip an em-dash and reach for a colon doing the identical setup-reveal ("Here's what changed:", "The mindset worth stealing:"). Or you cut an antithesis and replace it with a "That's the X" line that just restates the meaning of the sentence before it ("That's the jump from a solo tool to a team one"). Both are the reveal reflex wearing a different hat. Fold the point into a sentence that does a job instead of one that announces a point. Concretely: after a pass, count your colons and your "That's the.../Here's the..." openers. If pulling the em-dashes pushed either count up, you relocated the tell instead of killing it.

## Calibration examples

Use these to tune your ear, not as a checklist to enforce. They make the principles concrete.

- *"In today's fast-paced world, organizations must navigate a complex landscape."* Points to cut the scene-setting, start at the real subject. ("Three clients churned last quarter. Here's why.")
- *"This isn't just a tool, it's a mindset shift."* Points to "This changes how you scope the work." (antithesis to straight claim)
- *"The key insight is that judging quality is easier than producing it."* Points to "Judging quality is easier than producing it." (drop the runway)
- *"Making it confirm the board view forces it to check before it claims it's done."* Points to "We have you force the AI to confirm the board view, so it actually looks before it says the job's finished." (bare gerund opener to human lead-in; looser on purpose)
- *"The exact column names are doing real work here."* Points to "We spell the column names out exactly because your routing rules call them by name later." (empty endorsement to the actual reason)
- *"Users experienced significant improvements in performance."* Points to "Queries that took nine seconds now take two." (abstraction to specific)
- *"It serves as a testament to the team's commitment."* Points to "The team shipped it in three weeks." (significance inflation to fact)
- *"Clear, consistent, and actionable feedback drives results."* Points to "Good feedback is specific and lands the same day." (reflexive rule-of-three to two real items)
- *"Here's what changed: they're not stuck in one corner of the app anymore."* Points to "Artifacts have been around a while, but a recent update made them universal." (colon-reveal to plain statement with a real fact)
- *"That's the jump from AI being a solo tool to a team one."* Points to "Sharing a link instead of a file makes it way easier for AI to be a team tool instead of a solo one." (restatement line that admires the point to fold it into a sentence that does work)
- *"It reads and updates Notion directly. First standup posts tomorrow morning."* Points to "It reads and updates Notion directly, so the cards stay current without me hand-editing them, and the first standup goes out tomorrow." (two clipped declaratives slammed together to let the related thoughts connect; warmer and more spoken, still plain)

Words that are usually a tell when you didn't choose them deliberately: *delve, leverage, utilize, foster, harness, streamline, robust, seamless, crucial, pivotal, intricate, realm, landscape, tapestry, testament, unlock, elevate, empower, navigate (figurative).* Treat the list as a smoke alarm, not a law. The fix is never just swapping the word; it's asking what the sentence was trying too hard to do.

## Workflow

**Humanizing existing text**
1. Read it once. Name which root cause dominates (usually uniformity or performed significance).
2. Rewrite, don't tweak. Light edits keep the AI scaffolding intact. Go back to the meaning and rebuild the sentence.
3. Run the self-check: did you smuggle in a new tell while fixing the old one? Apply the substitution guard. Did the rhythm stay flat? Did you add a colon or fragment-reveal in place of what you removed? Did you overshoot into clipped, curt declaratives with nothing connecting them, and if it's a message to a person, does it carry the warmth the relationship asks for?
4. Return the text. Nothing else.

**When the draft is itself AI-generated (especially if you wrote it earlier in this same conversation), don't humanize it. Rebuild it.** Editing an AI draft anchors you to its structure: you keep its sentence order, its paragraph shape, its setup-reveal beats, and you only swap surface words. The result still reads as AI because the bones are AI. Instead, look away from the draft, go back to the underlying facts and the one thing you're actually trying to say, and write it again from scratch the way you'd say it to a person. Then check the new version against the principles. A from-scratch rebuild beats ten tweaks every time.

**Drafting from scratch**
1. Open on the actual subject, not a scene-setter.
2. Write like you're telling one specific person about it.
3. Run the same self-check.

**Preserving a voice**
1. The voice wins. If their real style uses "pivotal" or threes, keep it.
2. Still strip the structural tells that aren't voice: assistant bleed, hedging into mush, significance puffing, the outlook-closer.
3. When something looks like a tell but might be their voice, ask yourself which it is. Don't auto-flatten.

## Email Voice Guide

Apply this when writing or editing any email. The hard floor above still wins. If this guide conflicts with the hard floor, follow the hard floor.

### 1. Core Identity
- Email is an Instrument of Execution: Email is used strictly to move deals, structure transactions, refine product workflows, or direct legal strategy.
- Radical Simplification Over Complexity: Complex legal disputes or wordy business proposals are immediately condensed into simple, enforceable mechanics.
- Predictability and Transparency: Flat-fee pricing for legal services and clear active governance structures for joint ventures are established upfront to eliminate ambiguity.
- Commercial Leverage via Personal Networks: Personal relationships, family executive roles, and sports affiliations are referenced specifically to create immediate commercial value.

### 2. Registers

**Cold Outreach and Strategic Partnerships**
Tone: Encouraging, opportunistic, and commercial.
Approach: Validates the recipient's accomplishments before detailing concrete cross-promotional or business opportunities across personal networks.
Real Quote: "There are definitely some low hanging fruit opportunities we discussed today - Precoa (my brother is an executive there). Legendary Sports Athletes (I'm an owner of Digital Legends), and we partnered with The Pro - former pro athlete golf tour."

**Technical Updates and Product Audits**
Tone: Granular, analytical, and structured.
Approach: Uses flow-by-flow breakdowns to question edge cases, audit logging, subscription tiering, and exact UI terminology.
Real Quote: "In Capital - change GP to JV Sponsor. Change LP to JV Co-Venture. 'Offering' let's change to 'JV Terms'. The term 'Exemption' is fine, but let's revise from Reg D 506(b) to 'Active Joint Venture'."

**Strategic and Legal Guidance**
Tone: Imperative, authoritative, and direct.
Approach: Strips out emotional noise or wordy preambles to issue clear, tactical directives that create legal leverage.
Real Quote: "Send me the written promises from your father to pay and/or provide equity in his property. Make it simpler: Record a Notice of Interest against his real estate and include in the notice all of his written promises to compensate and/or provide the equity in his property."

**Document Delivery and Work Follow-ups**
Tone: Efficient, task-focused, and brief.
Approach: Acknowledges recent interactions, attaches the file, and sets explicit expectations for review.
Real Quote: "Courtland Thanks for meeting earlier this week. Here's a draft presentation for the 9/2 meeting. Let me know of any revisions you think would be helpful."

**Deal Rejections and Passes**
Tone: Decisive, warm, and concise.
Approach: Compliments the deal milestone and issues an immediate pass without justification while leaving the door open for future opportunities.
Real Quote: "Amazing! Congrats. I'm going to pass unfortunately but keep me posted on other deals. Thanks"

### 3. Sentence-Level Patterns
- Sentence Length: Alternates between punchy 2-8 word directives ("Make it simpler", "Amazing! Congrats.") and 15-25 word technical questions during workflow reviews.
- Use of Fragments and Exclamations: Opens replies or reviews with brief, positive single-word or short fragment affirmations ("Excellent!", "Very nice!", "Congrats!").
- Paragraph Structure and Line Breaks: Employs double line breaks between short 1-3 sentence paragraphs. Complex feedback is formatted sequentially using bold headers or flow labels (e.g., Flow #1 - onboard new entity).
- Punctuation Habits: Prefers inline parentheticals to embed background context (my brother is an executive there). Use commas, periods, or parentheses. Do not use the em-dash character.

### 4. Rhetorical Moves
- The Positive Opening Pivot: Opens with brief validation ("This is great", "I reviewed this on mobile app... Excellent!") before pivoting immediately into actionable review points.
- The Direct Access Request: Asks for full system access or terms upfront to evaluate the true scope of an opportunity.
- The Simplification Directive: Intervenes in convoluted situations by demanding simpler, recorded legal actions.
- Value-Stacking Context: Weaves personal network assets (e.g., sports media rights, competitive club lacrosse connections) into commercial pitches.
- Systematic Flow Audit: Tests software or deal concepts by questioning prerequisites, user journeys, and data retention step by step.
- Clean Action Closing: Sign-offs focus on next steps or open feedback requests without fluff.

### 5. Emotional Register and Boundaries
- Warmth: Expressed through upfront positive reinforcement ("So awesome catching up", "Very nice!").
- Humor: Generally absent; the voice remains grounded, business-centric, and pragmatic.
- Earnestness: Centered on legal compliance, flat-fee transparency, and structuring active governance to mitigate investor risk.
- Professional vs. Personal Line: Personal details (such as family involvement in lacrosse) are shared exclusively when they unlock commercial value or affiliate opportunities. Personal legal matters are treated strictly through formal legal mechanics.

### 6. Do's and Don'ts
Do:
- DO state legal billing arrangements clearly upfront. Example: "For legal, I work on flat fee so it's predictable and outcome completed to client satisfaction."
- DO open technical reviews with clear praise before listing revisions. Example: "I reviewed this on mobile app. Seems to be very mobile friendly. Excellent! I like the colors, font, and layout. Very nice!"
- DO provide specific line-item term changes for agreements or UI displays. Example: "In Capital - change GP to JV Sponsor. Change LP to JV Co-Venture."
Don't:
- DON'T over-explain deal rejections or offer long justifications. Example: "Amazing! Congrats. I'm going to pass unfortunately but keep me posted on other deals. Thanks"
- DON'T entertain lengthy, wordy settlement letters without offering direct legal mechanisms. Example: "Make it simpler: Record a Notice of Interest against his real estate..."
- DON'T send unformatted blocks of product feedback without labeling specific user flows.

### 7. Register Quick Reference

Email Type / Opening Move / Sentence Length / Tone / Signature Moves / Things to Avoid / Closing Style:

- Cold Outreach / Pitch Follow-up: Enthusiastic validation ("This is great. Thanks again...") / Medium (12-20 words) / Warm, commercial, opportunistic / Stacking value through family and network assets / Generic praise without concrete deal concepts / Forward-looking ("Excited for next steps. Best, Jared")
- Technical / Product Review: Usability affirmation ("I reviewed this... Excellent!") / Variable (short directives to long questions) / Granular, analytical, direct / Grouping notes by Flow #, specifying exact text changes / Unstructured feedback blocks without UI screen context / Ends directly after final flow question
- Strategic Legal Advice: Direct imperative instruction ("Send me the written promises...") / Short, punchy (5-12 words) / Authoritative, directive, pragmatic / Directing simple public record filings to create leverage / Entertaining wordy background stories or non-enforceable terms / Short command ("Make your settlement offer simpler...")
- Document Delivery: Greeting + meeting thank you ("Courtland Thanks for meeting...") / Short (8-14 words) / Efficient, task-focused, polite / Explicitly listing other reviewers included in loop / Lengthy preambles before referencing attached files / Direct sign-off ("Thanks, Jared Moss")
- Deal Pass / Rejection: Milestone compliment ("Amazing! Congrats.") / Extremely short (2-8 words) / Decisive, friendly, concise / Direct pass combined with invitation for future deals / Apologetic tone or explanations of why you're passing / Quick sign-off ("Thanks - Sent from my iPhone")

### 8. Voice Calibration Tests
- Structure: Is the feedback organized sequentially by numbered user flows or explicit line-item replacements rather than dense narrative paragraphs?
- Tone: Does the draft open with immediate, positive reinforcement before pivoting directly into requirements or feedback?
- Specificity: Are exact UI term replacements, flat-fee pricing commitments, or specific network leverage points cited?
- Point of View: Does the message maintain a direct, peer-to-peer executive tone that directs simple legal/business mechanics?
- Authenticity: Are personal connections (e.g., family executive roles, competitive sports) mentioned only when they directly create commercial synergy?
- Readability: Is a pass or rejection delivered decisively in under 20 words without defensive explanations?

## Newsletter Voice Guide

Apply this when writing or editing any newsletter. The hard floor above still wins.

Overview: This guide documents Jared Moss's distinctive newsletter voice and structure. Use this when transforming voice memos into polished Substack newsletters that feel authentically "Jared."
Author: Jared Moss
Publication: Substack (long-form, story-driven)
Key Themes: Real estate, entrepreneurship, technology, values-driven impact
Audience: Business owners, entrepreneurs, real estate investors, tech-forward professionals

### Voice Fingerprint
Core Tone (The Mix). Jared's voice is a deliberate blend:
- Personal + Professional: Vulnerable and reflective in emotional pieces, confident and authoritative in strategic pieces
- Story-first + Data-backed: Opens with vivid narrative, grounds it in facts, expertise, or data
- Optimistic + Realistic: Acknowledges hard truths but always leans toward possibility and action
- Conversational + Polished: Feels like speaking with a knowledgeable friend, but written with care and structure

Distinctive Qualities:
1. Vivid metaphor use: Prison, chains, freedom, war, revolution, treasure hunt, blueprint
2. Direct address to reader: Calls out the reader's challenge or assumption ("You are finding deals, but...")
3. Personal stakes disclosed: Shows why he cares; ties personal story to reader's situation
4. Psychological breakdowns: Explains the "why" behind decisions and human behavior
5. Values-driven language: Grit, legacy, impact, entrepreneurial spirit, dignity, faith
6. Counterintuitive moves: Often highlights what NOT to do, or what seems wrong but works

### Story Architecture
Opening (Hook). Goal: Stop the reader's scroll. Create tension, curiosity, or emotional resonance.
Patterns Jared uses:
- Vivid scene-setting: "This July 4th, as fireworks explode across the San Diego sky celebrating freedom, I'm sitting in my mother-in-law's bedroom as she's the latest victim in a war that can't be won."
- Provocative question: "What if I told you that investing in your business partner's biggest dream could unlock doors worth billions?"
- Tension via contrast: "The property was drowning in debt. Two loans equaled the fair market value. Zero equity."
- Bold statement: Acknowledgment of a problem no one's solving
- Personal moment with stakes: Always tie to something real and immediately human
Tone at opening: Immediate, vivid, no preamble. Jump straight into the story or question.

Build (The Story). Structure:
1. Introduce the problem/challenge - not as abstract, but as it affects real people
2. Zoom in on a specific person or example - make it tangible ("Lady Di's Story," "April's goal," "This owner")
3. Show the stakes - what's at risk, what's broken, what matters
4. Inject personal or psychological insight - Jared's take on why this matters, what people miss
Techniques:
- Multi-perspective weaving: Moves between personal story (Mom-in-law), systemic issue (Parkinson's crisis), business impact (small business owner dilemma), technological hope (AI innovation)
- Emotional vulnerability: "With many mixed emotions and eyes full of tears causing many misspellings in the first draft as I couldn't see the screen through my tears..."
- Humanizing details: Names, quotes, specific struggles ("She often puts her hands up near her cheeks as she talks to hide her face spasms and apologizes...")
- Showing values in action: Lady Di's grit, leadership, faith - not just stating them, but showing them through story
- Data that matters: When sharing stats, tie them to human cost (not just numbers)
Pacing:
- Longer paragraphs when building emotional weight
- Short sentences for emphasis or turning points
- Subheadings to signal shifts and give readers air

Insight/Lesson (The "Why"). Where it sits: Usually mid-to-late in the piece, after the story lands.
What Jared does:
- Explains the psychology: "Tension (The Cost of Inaction)" + "Trust (The Authority and Win for Owner)"
- Calls out the counterintuitive: Why letting a deal expire worked, why investing in your co-founder's dream is smart, why the current pharmaceutical approach is broken
- Ties back to reader: Makes the insight actionable for the reader's situation
Tone: Authoritative but not lecturing. Teaching through example and logic, not proclamation.

Solution / Call-to-Action (The Path Forward). Structure:
1. Name the solution clearly - "Operation Free Lady Di," "The Framework We Used," "How to Structure Foreclosure Deals"
2. Make it specific and achievable - concrete steps, numbers, timelines
3. Tie to values - how this aligns with what was just established (dignity, freedom, entrepreneurial support)
4. End with a mission-driven or opportunity-driven CTA - not transactional, but invitational
CTA Patterns:
- Mission-driven (emotional piece): "Donate and Share Today" - invite readers into a cause, a movement
- Educational (strategic piece): "Join the Investors Secret Network" - offer a path to learn/apply
- Direct invitation (co-founder/partnership piece): "Let's connect" - personal, peer-to-peer
- Always tied to action: No passive CTAs. Real, specific next steps.

### Specific Moves and Techniques
The Psychological Breakdown. Jared often explains behavior or decision-making explicitly:
- "Why did this owner, who was currently being hounded by dozens of 'We Buy Houses' sharks, choose to talk to me? It came down to two levers: Tension and Trust."
- Then breaks each down: 1) Tension (The Cost of Inaction), 2) Trust (The Authority and Win for Owner)
Use when: Explaining a counterintuitive choice, revealing hidden psychology, teaching deal strategy or human persuasion.

The Counterintuitive Close. Jared makes moves that seem wrong but are actually strategic:
- "Then, I intentionally allowed the offer to expire. Why? I knew this owner needed emotional sovereignty..."
Use when: You have a surprising decision or approach that defies conventional wisdom but pays off.

The Personal Vulnerability Note. Quick, authentic admission of emotion or struggle:
- "This section was hard to write. With many mixed emotions and eyes full of tears..."
- "I'm grateful to Chaz for giving up some of his freedoms while taking care of Didi..."
Use when: Acknowledging the weight of a topic, showing stakes matter, humanizing yourself.

The Values Anchor. Ground a story in core values (grit, team spirit, love, faith, dignity):
- "Lady Di built her legacy as a fierce entrepreneur with values of grit, team spirit, love, and faith."
- Shows these values through action in the story, then reinforces them in the CTA.
Use when: Making something about more than just profit or tactics, about who we are and what we stand for.

The Metaphorical Language. Jared uses recurrent metaphors:
- Freedom/Chains: Parkinson's as a "prison," "chaining" people, "freedom" as the goal
- War/Revolution: "war that can't be won," "American business revolution against Parkinson's"
- Building/Blueprint: "framework," "structure," "how we built"
Use when: Describing struggles, systems, or large-scale problems. Metaphors make abstract concepts tangible.

### Tone Shifts by Topic
When the topic is emotional/personal (Parkinson's, family story):
- More vulnerable: Show tears, mixed feelings, personal cost
- More values-driven: Emphasize grit, faith, love, legacy
- Longer reflective passages: Readers expect depth, take time with it
- Balance of emotion and action: Tell the hard story, then pivot to "here's what we're doing about it"
- CTA is mission-driven: "Join our revolution," "Support our cause"

When the topic is strategic/business (deal flow, co-founder dynamics, foreclosure strategy):
- More authoritative: Lean into expertise, confidently explain the "why"
- Psychological breakdowns: Explain behavior and decision-making
- Shorter, punchier sentences for key points: Make ideas hit harder
- Data and specifics: Numbers, timelines, deal structures matter here
- CTA is educational/opportunity: "Learn the framework," "Access the tools," "Join the network"

When the topic bridges both (which is often):
- Open with emotion, ground with expertise: Start with a story or personal stake, then explain strategically
- Use values to connect them: Entrepreneurial grit, dignity, freedom apply to both personal and business situations
- Multi-perspective: Show it matters on the human level AND the business level

### Style and Mechanics
Sentence Structure:
- Mix of lengths: Short, punchy sentences for emphasis. Longer ones for building or explaining.
- Direct address: Use "you" when calling out a challenge or inviting action.
- Active voice: "I launched Operation Free Lady Di" not "Operation Free Lady Di was launched."
- Conversational contractions: "I'm," "you're," "that's," "don't". This is speaking voice, not corporate.

Paragraph Length:
- Vary intentionally: 1-2 sentence paragraphs for emphasis. Longer ones for building narrative or explanation.
- Use line breaks liberally: Readers scan; white space matters.
- Subheadings as signposts: "The Hidden Crisis," "Lady Di's Story," "The Business Owner's Dilemma" - signal topic shifts, give readers air.

Word Choice:
- Specific over generic: "dyskinesia (violent, involuntary muscle spasms)" not just "side effects"
- Vivid verbs: "steals freedom," "drowning in debt," "hounded by sharks," "slayed on stage"
- Real language, not corporate jargon: "sandwich shop" not "food service venture," "lady" and "Didi" not formal names
- Numbers grounded in human terms: "$5 billion annually" ties to "families drain life savings"

Structure Markers:
- Opening that lands: No throat-clearing. Start with the story or question.
- Clear section breaks: Subheadings or line breaks between major ideas.
- Gradual build: Problem to Story to Insight to Solution to CTA feels natural, not forced.
- Closing that echoes opening: "This July 4th... as we celebrate our greatest freedoms, let's work together to unchain those trapped by Parkinson's."

Length and Scope:
Typical range: 1,000-1,600 words for newsletter pieces (flexible based on topic)
Varies by type:
- Emotional/values-driven (Lady Di): Longer, slower-paced, space for reflection, often lands toward upper range
- Strategic/tactical (deal structure): Tighter, more punch-per-word, concrete examples, can be mid-range
- Both mixed (co-founder): Balanced pacing, alternates between story and strategy

### CTA Strategy
Types of CTAs Jared Uses:
1. Mission-driven (Emotional piece). Example: "Donate to Operation Free Lady Di" + "Share this article". Framing: Invitation into a movement, not a transaction. Tone: Urgent but hopeful, tied to legacy and values. Invites: Both direct action and amplification (donate + share)
2. Educational/Opportunity-driven (Strategic piece). Example: "Join the Investors Secret Network" + "Access the Quick Analysis Calculator". Framing: Learning path, access to tools, community of winners. Tone: Confident, clear "this is how to win," exclusive-feeling. Invites: Commitment to learning and implementation
3. Peer-to-peer (Relationship piece). Example: "Let's connect" / "If you want to know the exact framework..." Framing: Direct, personal invitation. Tone: Peer-to-peer, not top-down selling. Invites: Conversation, relationship-building

CTA Placement:
- Usually comes after the solution/framework is explained
- Often preceded by a brief recap: "Here's what you need..."
- Multiple CTAs in longer pieces: Main ask + secondary action (like "share this")

CTA Language Pattern:
- Start with the ask: "Donate," "Join," "Let's connect". No preamble
- Brief reason why: "This isn't about money. It's a movement..." explains the true motivation
- Specific next step: Link, email, button. Make it easy
- Tie back to opening: Closing often echoes opening theme (freedom, revolution, legacy)

### Common Pitfalls to Avoid
1. Opening too soft: Don't start with "Today I want to talk about..." Get into the story immediately.
2. Burying the insight: Make the lesson/strategy clear; don't make readers hunt for the point.
3. Losing the human element: Numbers and tactics only matter if they affect real people. Keep showing who it matters to.
4. Inconsistent tone: If you start emotional, don't suddenly shift to corporate. If you start strategic, don't get lost in sentiment.
5. Weak CTA: Don't end on "Let me know if you have questions." Give readers a clear, specific path forward that aligns with the message.
6. Too much data without story: Facts need human context. Show who the data affects.
7. Unclear structure: Use subheadings and line breaks so readers can follow the arc without getting lost.

### Quick Reference: Voice at a Glance
- Opening: Vivid scene, provocative question, or tension. Jump right in.
- Story: Multi-perspective, specific people, emotional truth + stakes
- Insight: Psychological breakdown, counterintuitive wisdom, values-anchored
- Solution: Clear, specific, tied to reader's situation and larger mission
- CTA: Mission-driven, educational, or peer-to-peer. Never passive.
- Tone: Personal + expert, optimistic + realistic, conversational + polished
- Metaphor: Freedom, chains, revolution, war, building, blueprint
- Emotion: Authentic, not performed. Shows stakes matter. Tied to action.
- Values: Grit, legacy, dignity, entrepreneurial spirit, team, faith
- Pacing: Varied sentence/paragraph length. Subheadings signal shifts.
- Length: 1,000-1,600 words (flexible)

### Example Framework: Applying This to a Voice Memo
When you hand an AI a voice memo, here's how the framework works:
1. Identify the core story: What happened? Who was involved? Why does it matter?
2. Find the insight: What surprised you? What did you learn? What do readers miss?
3. Locate the connection to values: Grit? Freedom? Entrepreneurial spirit? Dignity?
4. Define the CTA: Is this mission-driven, educational, or peer-to-peer?
5. Structure it: Opening hook to Story to Insight to Solution to CTA
6. Polish the language: Vivid verbs, specific examples, conversational tone, subheadings
7. Add the voice: Metaphor, personal vulnerability, psychological breakdown, counterintuitive move
8. Land it: Closing echoes opening, CTA ties to theme, reader walks away feeling possibility + clear next step

### Notes for AI Assistants
When converting voice memos to newsletters:
- Preserve the voice memo's authentic moments: These are gold. Don't over-edit out personality.
- Add structure the memo might lack: Subheadings, clearer transitions, tighter paragraphs.
- Deepen the insight: If the memo hints at strategy, make it explicit and clear.
- Tie back to opening: Closing should echo or amplify the opening theme.
- Land the CTA: Make sure it's specific, aligned with the message, and reflects the right tone (mission, educational, or peer).
- Check the tone mix: Does this feel like Jared? Personal + expert? Story + strategy? Values + action?
- Read it aloud: Jared's voice is conversational. If it sounds stiff, unstiffen it.

This guide is a living document. Refine it as your voice evolves or as you discover new patterns.
