---
name: clo-publish-check
description: Pre-publish checklist for a CLO Substack draft — voice, legalese, source links, tone. Use when Jared asks if a draft is ready to publish.
---

Run this checklist against the draft in question and report pass/fail on
each line, not just an overall verdict:

1. Voice: checked against `clo-humanize-voice`
   (banned words, no legal advice framing, journal judgment-call framing).
2. No archaic legalese (therefore, thereto, therein, whereas, etc.).
3. Every factual/legal claim has a working, verified link.
4. Reads like Jared, not an AI — run past `clo-humanize-writing` first,
   then `clo-humanize-voice`
   calibration checks to confirm it's not just
   human-sounding but specifically his voice.
5. Title and preview text are accurate to the body (no bait).

If anything fails, fix it directly (or dispatch the `clo-editor` subagent) and
re-check before telling Jared it's ready.
