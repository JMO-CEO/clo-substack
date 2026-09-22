# CLO brand lock v1 (interim, approved 2026-09-22)

Comic book journal system mirroring Studio Dumbar method: motion and sound show
personality, design shows appearance. Simple ideas that scale. Play as the method.
Underline palette cross-check pending. When Underline hex values land, adjust
this file first, then frames.md, then the cover template.

## Palette (locked)

- Ink Black #0B0B10: canvas, comic page at night. Distinct from JV OS pure black.
- Signal Yellow #FFD21F: hero accents, headline text, CTA highlight.
- Hazard Magenta #FF2E7E: villain accents only. Never hero, never CTA.
- Paper White #F5F1E6: caption boxes, body text on dark.

## Type (locked, zero spend)

- Display: bold condensed shout for headlines and cover hook. Code built covers
  use Arial Narrow / Liberation Sans Narrow (system stack, no font spend).
- Body: plain grotesk. Substack native stack, never embedded.

## Comic overlay (append verbatim to every adapted image and video prompt)

ink black canvas #0B0B10, halftone dot shading, signal yellow #FFD21F hero accents,
hazard magenta #FF2E7E villain accents only, bold condensed caption box top third
left clear for headline, paper white #F5F1E6 caption text, no watermark, 9:16 safe

## Motion verbs (one per Note, rotation)

slam, stretch, snap, unfold, surge. The cover and clips move the way the story reads.

## Sonic tags (one per video, rotation, fal.ai native audio on)

1. paper snap plus bass hit (hero entrance)
2. ink scratch riser (villain reveal)
3. crowd gasp plus resolve chord (vote ask close)

## Cover system (zero image spend)

assets/cover-template.svg holds the template with {{HOOK}} placeholder. The run
copies it to drafts/YYYY-MM-DD/cover.svg with the week hook, then renders
cover.png via scripts/render-cover.py (cairosvg, rsvg-convert, or Pillow flat
card fallback in CLO palette).

## Video spec (fal.ai, manual v1)

Image to video from the approved still. Primary: Kling 3 Pro or Seedance 2.0,
15s single pass, 9:16, native audio on. Fallback: 2x Veo 3.1 8s stitched.
video-script-pack.md carries endpoint plus params plus sonic tag per clip.
Generation stays manual in the fal playground. The Action never spends.

## Text model (locked)

google/gemini-3.5-flash-lite via GEMINI_API_KEY repo secret, exported in the
workflow as GOOGLE_GENERATIVE_AI_API_KEY (the exact name the Google provider
reads). The model writes prompt packs. Humans run fal.ai by hand.
