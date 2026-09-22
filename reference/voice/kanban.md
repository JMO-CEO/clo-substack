# Kanban rules

Board: `kanban.html` (project root), published live at
https://claude.ai/artifact/MNgAna4naZ3xWVkedDcDF1. Five columns in order:
Inbox/Backlog (`inbox-backlog`), Today (`today`), In Progress
(`in-progress`), Blocked (`blocked`), Done (`done`).

**Source of truth:** the board's shared `db` capability — collection
`cards` on that artifact URL, one document per card with fields `title`,
`notes`, `column`, `order`. This is a real-time store: any drag, edit, or
add Jared makes in the browser lands in this same collection immediately,
and any write this agent makes shows up in his browser immediately too —
there is no separate "browser state" this agent can't see anymore. Read
and write it with the `ArtifactData` tool (load via ToolSearch if not
already loaded) against the URL above — never edit the `kanban.html` file
itself to change board contents; the file only holds the page's code, not
its data. Editing `kanban.html` is for changing the board's design or
behavior, not its cards.

## 1. Query trigger

**Trigger phrases:** "what's on my board", "what do I need to do today",
"what's on my kanban", "show my tasks" (and obvious variants of these).

**Behavior:**
1. `ArtifactData` `list` (or `query`) the `cards` collection.
2. Report the `today` and `in-progress` cards as a briefing — title and
   notes for each, grouped by column.
3. Then list the `inbox-backlog` cards and ask Jared whether any of them
   should move up into Today or In Progress.

## 2. Add-task trigger

**Trigger phrases:** "add this to my kanban", "add this task", "track this".

**Behavior:**
1. `ArtifactData` `list` the `cards` collection to find the current max
   `order` among `inbox-backlog` cards (and to avoid a duplicate id).
2. `ArtifactData` `set` a new document in `cards`:
   - `doc_id`: `card-` followed by a short slug of the task name plus a
     short unique fragment (e.g. `card-stripe-webhook-retry-mp3k91`), so
     it never collides with an existing id.
   - `title`: the task name taken from Jared's message.
   - `notes`: any extra context from the message, or `""` if none.
   - `column`: `"inbox-backlog"`.
   - `order`: one more than the highest existing `order` found in step 1.
3. Write immediately — no confirmation gate before writing. This is a
   write to a board Jared owns and can see change live, not an
   irreversible action, so it does not need the same check-in a Notion
   write would.
4. Confirm back to Jared, after the fact, what was added and to which
   column.
