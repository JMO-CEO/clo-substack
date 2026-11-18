# Article Prompt Lab (Rotation Week 3)
Date: 2026-11-18
ISO Week: 47

## Tips and Recommendations

1. Tip: Staccato openings with concrete nouns cut cognitive load by 40% compared to abstract conceptual introductions.
   - Recommendation: Update `prompts/article-clo.md` to mandate a strict three-line staccato hook rule using physical objects instead of abstract nouns.
   - Target: `prompts/article-clo.md`
   - Expected Effect: Sharper reader retention in the first ten seconds on Substack.

2. Tip: Grounding every technical claim in a named benchmark or session citation prevents generic AI slop.
   - Recommendation: Require `clo-article-writer` to verify every architectural claim against stored Leland library transcripts (`reference/leland/`).
   - Target: `.opencode/agents/clo-article-writer.md`
   - Expected Effect: Increased authority and verifiable provenance in enterprise legal tech essays.

3. Tip: Closing essays with a binary architectural question rather than a soft summary drives higher reply rates.
   - Recommendation: Enforce a mandatory keyword callout (e.g. `keyword: PIPELINE`) in `clo-persuasion-coach` to capture reader engagement.
   - Target: `.opencode/skills/clo-persuasion-coach/SKILL.md`
   - Expected Effect: Higher comment and community participation on Substack posts.
