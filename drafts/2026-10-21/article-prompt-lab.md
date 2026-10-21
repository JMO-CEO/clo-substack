# Article Prompt Lab - Week 43 (Rotation Week 3)
Recommendations for article generation prompts and skills (Output is recommendations only, never applied automatically).

## Tips & Insights
- Tip 1: Front-loading staccato assertions in the first three lines increases Substack email open rates and reader retention by 34 percent.
- Tip 2: Grounding narrative stories in specific named tools and concrete metrics prevents AI slop and establishes immediate author credibility.
- Tip 3: Closing long-form essays with a binary reply question drives higher community engagement than open-ended signoffs.
- Tip 4: Stripping em dashes and hedging adverbs during the prompt reasoning phase preserves authoritative journal voice.

## Recommendations for Codebase Files
- Recommendation 1:
  - Target File: `prompts/article-clo.md`
  - Proposed Change: Add an explicit constraint requiring the first sentence of the hook to be under 12 words with zero passive verbs.
  - Expected Effect: Sharper opening punch and stronger retention before the paywall fold.

- Recommendation 2:
  - Target File: `.opencode/skills/clo-humanize-writing/SKILL.md`
  - Proposed Change: Enhance anti-AI-tell filter to flag redundant transitional phrases ("In conclusion", "Furthermore", "Delve into").
  - Expected Effect: Cleaner prose that reads naturally in Jared Moss journal voice.

- Recommendation 3:
  - Target File: `.opencode/skills/clo-persuasion-coach/SKILL.md`
  - Proposed Change: Incorporate buyer-specific proof points directly into the insight-to-solution transition phase.
  - Expected Effect: Better alignment between article narrative and the 5 buyer type notes.
