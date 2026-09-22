---
description: Wednesday ship gate for the weekly CLO folder. Runs the editor gate and publish checklist, then marks BOARD ready.
agent: clo-editor
subtask: true
---

Ship gate for week $ARGUMENTS (default today). Load the week drafts folder, run @clo-editor gate plus clo-publish-check, verify all 10 files plus meta.json present and non-empty.

If the gate passes: move the BOARD.md card to Done Published, append one line to MEMORY.md top hooks, and tell Jared the article is ready to paste to Substack plus blog with the 5 Notes scheduled Mon to Fri. If anything fails, report the failing line and hold. Never push live or post anywhere from this command.
