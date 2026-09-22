---
name: clo-new-post
description: Draft a new CLO Substack issue end to end — outline, research handoff, draft, save to drafts/. Use when Jared asks to write a post or draft an issue on a topic.
---

1. Confirm the topic and angle in one line back to Jared if it's ambiguous;
   otherwise proceed.
2. Dispatch the `clo-researcher` subagent (Task tool) to gather sourced facts
   and links on the topic.
3. Draft the post in Jared's voice: direct, plain English, no legalese.
   Load `clo-humanize-voice` first. Close with a Next Week teaser plus a
   For now reply question, per reference/articles voice anchors.
4. Dispatch the `clo-editor` subagent to tighten the draft and verify sources.
5. Save the final draft to `drafts/YYYY-MM-DD-slug/article-draft.md`
   (week date, a short slug of the title). Include the sourced research
   inline or as research-brief.md so the folder is a complete record.
6. Tell Jared it's ready and where it landed — don't publish anywhere
   without him saying so.
