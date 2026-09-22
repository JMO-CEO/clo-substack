# MEMORY.md - long term facts for CLO agents. No secrets here, ever.

## Voice

[FILL IN: 2-3 lines - how CLO sounds. Different from JV OS and Legends.]

## Brand

- Lock v1 (2026-09-22, interim): Dumbar method comic system. Full spec in prompts/brand-clo.md.
- Palette: Ink Black #0B0B10 canvas, Signal Yellow #FFD21F hero, Hazard Magenta #FF2E7E villain only, Paper White #F5F1E6 captions.
- Type: bold condensed shout display (system stack, zero spend), plain grotesk body.
- Underline palette cross-check pending. Adjust brand-clo.md first when hex values land.

## Style anchors

- [FILL IN as you publish: date, piece, hook]

## Top hooks that worked

- (append one line per published piece: date, hook, saves or replies)

## Pipeline facts

- Standalone OpenCode project at `CLO\`. Own git repo, own remote. Sibling of JV OS and Digital Legends, never nested.
- Agents prefixed `clo-`. Skills prefixed `clo-`.
- Zero cross-reads with JV OS or Digital Legends folders.
- WEEKLY cadence: Tue 10pm Denver auto draft (cron `0 4 * * 3`, flip to `0 5 * * 3` after Nov 1). Wed morning Jared reviews and ships to Substack plus blog. Notes drip Mon to Fri manually.
- Text model: google/gemini-3.5-flash-lite via GEMINI_API_KEY secret, exported as GOOGLE_GENERATIVE_AI_API_KEY in the workflow. The model writes prompt packs. Humans run fal.ai by hand.
- Video: fal.ai image to video, Kling 3 Pro or Seedance 2.0 primary (15s, 9:16, native audio on), 2x Veo 3.1 8s fallback. Manual v1, the Action never spends.

## Corrections log

- (append: date, what broke, rule added)
