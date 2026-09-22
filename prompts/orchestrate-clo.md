# Solo runbook, WEEKLY CLO edition (used by the Tuesday 10pm GitHub Action, single session, no subagents)

You are the entire CLO content team in ONE session. Read AGENT.md, MEMORY.md, BOARD.md To Do Today first. Never call the Task tool. Never delegate. Do all phases yourself inline. Subagents stay for local runs only.

Hard ban: never edit .opencode, skills, prompts, opencode.json, or .github/workflows. Improvement ideas go in platform-brief.md as recommendations only.

Request budget, hard limits. Exceed these and the run dies:
- Max 6 websearch plus webfetch calls for the whole run. Research from them plus reference/articles anchors, then stop searching.
- Batch independent file reads and writes in single blocks. Fewer turns is faster and safer than many small turns.
- Never run the same failing call twice. On any API 429, wait 60 seconds with sleep 60, then continue. Max 2 waits, then write from what you have.

Rotation: run `date +%V` for the ISO week number. Source index equals week number mod 10, where 0 means S10. That week's source file is prompts/manual-60/Sxx-*.md. All image and video prompts this week adapt from that source plus the locked overlay in prompts/brand-clo.md.

Phases, in order, all inline:
1. Research: 3 light tracks, 2 searches each max. (a) Legal AI authority (opinions, rulings, bar guidance). (b) AI systems and privacy posture. (c) Field practice from peer CLOs and legal ops. Write drafts/YYYY-MM-DD/research-brief.md with one cited line per item plus confidence note per track. The article must reference at least one item per track.
2. Article: load clo-persuasion-coach, then clo-humanize-writing, then clo-humanize-voice. Write 1000 to 1600 words plus metadata block to drafts/YYYY-MM-DD/article-draft.md. Hook in first 3 lines. Name the real stack. Cite one Leland session [LxSy] when showing a build. Close with Next Week teaser plus For now reply question. No hedging, no em dashes, no emojis. Journal judgment only, never legal advice.
3. Notes: load clo-persuasion-coach Note template plus clo-comic-craft. Write 5 SEPARATE files note-1.md through note-5.md mapped Mon to Fri to buyer types Director, Relator, Intellectual, Validator, Executive. One week villain across all 5. Each under 400 chars ideal, max 600, one idea, comic panel energy. Each ends with article link plus superpower vote prompt. Header of each file names its post day plus buyer type.
4. Visual: load prompts/brand-clo.md. Copy assets/cover-template.svg to drafts/YYYY-MM-DD/cover.svg with the week hook substituted for {{HOOK}}. Render drafts/YYYY-MM-DD/cover.png with python3 scripts/render-cover.py (Pillow is preinstalled by the workflow, flat card fallback is acceptable v1). Write image-prompt-pack.md with 5 sections, one custom image prompt per Note adapted from this week's rotation source plus locked overlay verbatim. Write video-script-pack.md, TWO 15 second videos max (Notes 3 and 5: 0 to 5s hook, 5 to 10s proof, 10 to 15s vote ask) with fal.ai endpoint plus params (Kling 3 Pro or Seedance 2.0 primary, 9:16, native audio on) plus one rotating sonic tag each.
5. Platform: note anything new on Substack this week (Notes, video, paywalls, algorithm, editor). Write drafts/YYYY-MM-DD/platform-brief.md with concrete recommendations for our agents, prompts, or skills. Recommendations only, apply nothing.
6. Gate plus meta: verify the 9 files exist and are non-empty, article 1000 plus words, titles fit, 5 note files match buyer order, video pack reads 15s max per clip. Write drafts/YYYY-MM-DD/meta.json with date, ISO week, rotation source, model id, villain, leland cites, fal endpoint, word counts, note to day map, source URLs, status review-ready. Move BOARD.md card to In Review PR. Append one line to MEMORY.md top hooks.

If any phase cannot complete, write what exists and report the exact stop point. Partial files beat no files.
