---
name: clo-research-sources
description: Deep-dive sourced research on a law plus AI topic, output as linked bullet points with confidence tiers, without drafting a post. Use when Jared just wants sources, not copy.
---

Dispatch the `clo-researcher` subagent (Task tool) on the requested topic.
Return its sourced bullet points directly to Jared — don't turn them into
prose unless he asks for a draft (route to `clo-new-post` instead in that case).
