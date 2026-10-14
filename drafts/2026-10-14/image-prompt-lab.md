# Image and Video Prompt Lab - 2026-10-14 (Rotation Week 2)

## Tips and Recommendations

1. Tip: Utilizing precise focal length descriptions (e.g. 85mm f/1.4) enhances character subject separation in comic-noir hybrid art styles.
   - Recommendation: Add standard focal length directives to prompt templates in prompts/brand-clo.md to ensure consistent depth of field across all comic issues.
   - Target File: prompts/brand-clo.md
   - Expected Effect: Sharper visual hierarchy between foreground heroes and ink-black backgrounds.

2. Tip: Specifying lighting direction (e.g. single overhead softbox with Fresnel reflections) prevents plastic-looking renders in AI-generated product and hardware stills.
   - Recommendation: Update prompts/visual-clo.md rendering guidelines to mandate explicit studio lighting terms.
   - Target File: prompts/visual-clo.md
   - Expected Effect: Higher fidelity metallic and glass surfaces in tech-themed comic panels.

3. Tip: Native audio synchronization tags in fal.ai Kling 3 Pro prompts improve rhythm alignment between motion bursts and sound cues.
   - Recommendation: Standardize the three sonic tags in prompts/brand-clo.md motion verbs list with explicit timecodes (0-5s, 5-10s).
   - Target File: prompts/brand-clo.md
   - Expected Effect: Tighter multi-sensory cohesion in 15-second video clips.

4. Tip: Maintaining uniform aspect ratio tags (9:16) at the exact end of every prompt string prevents cropping errors in vertical video platforms.
   - Recommendation: Enforce 9:16 safe and aspect ratio trailing parameters in clo-visual-builder agent specifications.
   - Target File: .opencode/agents/clo-visual-builder.md
   - Expected Effect: Zero manual reframing required when moving stills to fal.ai image-to-video pipelines.
