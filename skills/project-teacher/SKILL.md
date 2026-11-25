---
name: project-teacher
description: Teach and plan software projects for learners. Use this skill whenever someone wants to understand or learn from a whole project (their own, a friend's, a GitHub repo, or a folder) - walking through how it fits together, explaining the concepts or terms it uses, how it was made, or the simplest way it could have been built. Also use it whenever someone asks for a build checklist, a step-by-step plan, or a sequence of prompts to build or rebuild an app, and whenever a beginner or non-coder has an app idea and asks where to start. Phrases like "walk me through this repo", "teach me how this was made", "I've never coded", "where do I start", "which concepts does it use" or "prompts to rebuild it" all mean this skill, even without the words "skill", "tutorial" or "checklist". Not for fixing one bug, writing one function, a general concept question unrelated to a project, or checklists that are not about building software.
---

# Project Teacher

Help someone learn by building. Given a project, or an idea for one, produce four things:
1. **Concepts**: the few technical ideas the project depends on, explained plainly.
2. **Simplest path**: how it could have been built with the least code, and what that gives up.
3. **Prompt chain**: the short, ordered prompts that build it step by step.
4. **Checklist**: a file of checkboxes, one per step, each with a "done when" test.

Keep the work moving. Explain only what the current project needs.

## Step 0: Choose the mode

- **Explain (existing project):** a folder, repo or app already exists. Go to Step 2.
- **Plan (new idea):** the user has an idea but no code yet. Skip to Step 1.
- **Both:** explain what exists, then plan the next feature.

If unclear, ask one question: "Do you have a project folder, or are we starting from an idea?"

## Step 1: Intake (ask only what is missing)

Ask all missing items in one message, at most six questions:
- What should the project do, in one sentence, and who uses it?
- Experience level: never coded, some code, or experienced? (It sets how much to explain.)
- Preferred language or platform, or "you choose"?
- The project folder path, if one exists.
- How much time per session?
- What does "finished" look like for the first version?

If the user already answered these, do not ask again. A vague request gets the smallest version that does the core job, and you say which parts were left out.

## Step 2: Scan the project (existing projects)

1. Run the scanner that ships with this skill, pointing it at the project folder: `python -I <this skill's folder>/scripts/scan_project.py "<project path>"`. It is read-only and prints the folder tree, detected stack, entry points and the start of the README.
2. Read only the files the scan points to: README, the entry point, the config file, and the one module the user asked about. Use search for a symbol before opening a large file.
3. Note what the project does, which libraries it uses, and where data comes in and goes out.
4. If the scan finds nothing useful (empty folder, binary files only), say so and ask what the project is.

## Step 3: Teach the concepts

List at most **8 concepts**, in dependency order (a concept comes after the ones it needs). For each one:
- **Term:** the correct technical name.
- **Meaning:** one plain sentence.
- **Analogy:** one everyday comparison, worked out fully.
- **Where it is:** the file and line, or the prompt step where it appears.

Match depth to the experience level:
- Never coded: explain every concept. Use short sentences and no unexplained acronyms.
- Some code: skip terms the user already uses. Ask in one line if unsure.
- Experienced: name the concept and give the trade-off, not the basics.

Never invent a concept the project does not use. If a name is ambiguous, say which reading the code supports.

## Step 4: Show the simplest path

Use `references/design-patterns.md` as the pattern to follow.

**Existing project:** compare how it was built with the simplest way that still works.

| | How it was built | Simplest way that still works |
|---|---|---|
| Structure | ... | ... |
| Libraries | ... | ... |
| What you lose | ... | ... |

**New idea:** nothing is built yet, so compare two or three real options and recommend one. For example, for a small website: one HTML file, separate HTML/CSS/JS files, or a framework.

| | Option A (recommended) | Option B |
|---|---|---|
| Files and setup | ... | ... |
| Libraries | ... | ... |
| Good for | ... | ... |
| What you lose | ... | ... |

Rules:
- Only suggest a simpler way that still does the job. If the simplest version drops a requirement, name the dropped requirement.
- Prefer what the language or platform already does, and existing project code, over new dependencies.
- Do not claim time, cost or token savings unless measured. Say "fewer files" or "fewer libraries", which you can check.

## Step 5: Write the prompt chain

Give 5 to 12 prompts, in order. Each prompt does one thing, names the file it changes, and ends with a check. Use the templates in `references/prompt-patterns.md`.

For each step, show:
- The prompt to paste.
- What the result should look like.
- How the user checks it works (run it, click it, read the output).

## Step 6: Create the checklist

Use `references/checklist-template.md`. Each item has a goal, the prompt to use, a "done when" test, and the one concept it teaches.

If the project has a user interface (web page, app, form), the step that adds the interface must also make it usable by everyone: every input and checkbox has a label, every button has a name that says what it does, and it works with the keyboard alone. Put this in that step's prompt and its "done when" test. Fixing it at the end is harder, and beginners never learn it otherwise.

- Show the checklist in chat by default.
- Write it to a file (for example `BUILD-CHECKLIST.md`) only after the user says yes, and only in the folder they name. Writing into their project is an edit they should approve.

## Step 7: Teach while building

When the user works through the checklist, mark an item done only after its "done when" check passes. Teach a new term only when that step needs it. Keep each teaching note under 100 words, and at most three terms per step.

## Rules

- Language: a 10-year-old should follow it. Do not talk down.
- Length: short unless the user asks for depth. Use a table only to compare two or more options.
- Read only the files you need. Do not dump the whole project into the chat.
- Never invent tools, libraries, or numbers. If unknown, say so.
- Do not run commands that change the user's project without asking first.
- Adapt to any language or stack. Do not assume the project is a web app.
