# project-teacher

A Claude skill that acts like a domain expert and mentor for "vibe coders": people who build by describing what they want to an AI.

Give it a project folder, or just an idea, and it will:

1. **Shape the idea**: a small first version, "later" ideas an expert would suggest, and one question that invites your own twist.
2. **Brief you like an expert** in your field (web, mobile, data, games, hardware and more): where to start, what never to skip, and the mistakes beginners make.
3. **Explain the concepts** the project uses, in plain words, with one everyday analogy each.
4. **Show the simplest way** to build it, and what that simpler way gives up.
5. **Recommend free tools and Claude skills before you ask**: real GitHub skills with their install commands, and free hosting, databases and editors with their limits.
6. **Give a prompt chain and a checklist** with a "done when" test for every step.
7. **Coach your prompting** while you build: it shows a better version of a vague prompt and says why.

It works for any language or stack. It is written for beginners who learn by building, and for experienced developers who want a fast walkthrough of an unfamiliar codebase.

**Quick install (Claude Code):**

```
/plugin marketplace add lakshmang007/project-teacher
/plugin install project-teacher@project-teacher
```

## See it in action

These are real, unedited outputs from Claude with this skill installed.

**You type one sentence:**

> "I want to make a website where students in my college can sell their old textbooks to each other. I've never coded. Where do I start?"

**It answers like an expert mentor** (excerpt):

> **Version 1 (the smallest useful thing):** sign up with your college email, post a listing, browse and search, mark your own listing as sold.
> **Left out for now:** payments, in-app chat, photos and ratings. Students can meet on campus and pay each other directly.
>
> **From day one:** turn on the database's access rules before anyone signs up. Never put secret keys in public code. Give every input a label.
>
> **Recommended for this project:** Ponytail keeps the code small (use from step 1). Supabase handles login and the database for free (step 5); inactive free projects get paused.
>
> **5. Real database.** *"Connect Supabase. Create a listings table, and save and load listings from it. Keep keys out of public code."*
> **Done when:** a listing is still there after you refresh the page.

| Example | What it shows |
|---|---|
| [Planning a new idea](examples/textbook-marketplace-plan.md) | Idea shaping, expert brief, simplest path, recommended skills and free tools, and a 9-step checklist with a prompt and a check for every step |
| [Explaining an existing project](examples/todo-site-explained.md) | 8 concepts with analogies and exact line numbers, plus an expert check that spots a real security detail |
| [The to-do site it was built from](examples/todo-site/) | A complete one-file website built by following the skill's checklist, every step checked in a browser |

## Install

### Option 1: Claude Code plugin (recommended)

In Claude Code, run:

```
/plugin marketplace add lakshmang007/project-teacher
/plugin install project-teacher@project-teacher
```

Then start a new session. The skill loads automatically.

### Option 2: Copy the skill folder manually

Copy `skills/project-teacher` into your Claude skills folder:

```powershell
Copy-Item -Recurse skills\project-teacher "$HOME\.claude\skills\"
```

On macOS or Linux, use `cp -r skills/project-teacher ~/.claude/skills/`.

Then start a new Claude Code session.

## Use

Ask Claude in plain words. Examples:

- "Explain the project in `C:\path\to\project` and teach me the concepts."
- "What is the simplest way this could have been built?"
- "I want to build a habit tracker. Give me a checklist."
- "Make a build checklist for the project in this folder."

The skill asks only for details it does not already know.

## What is inside

```
project-teacher/
├── .claude-plugin/
│   ├── plugin.json               plugin manifest
│   └── marketplace.json          lets Claude Code install it from GitHub
├── skills/
│   └── project-teacher/
│       ├── SKILL.md              the workflow Claude follows
│       ├── references/
│       │   ├── domains.md             expert notes per project type (web, mobile, data, games, hardware...)
│       │   ├── recommendations.md     verified Claude skills and free tools, with install commands
│       │   ├── design-patterns.md     the 8-step pattern for building any project
│       │   ├── prompt-patterns.md     copy-ready prompts for each step
│       │   └── checklist-template.md  format for the build checklist
│       └── scripts/
│           └── scan_project.py   read-only project scanner (Python 3, standard library only)
├── examples/                     real outputs from the skill, and the site built with it
├── docs/
│   └── AUDIT.md                  security and quality audit, with test results
├── CHANGELOG.md
├── CONTRIBUTING.md
└── LICENSE                       MIT
```

## Run the scanner yourself

The scanner prints a project's stack, entry points, file tree and README opening. It never changes files.

```powershell
python -I skills\project-teacher\scripts\scan_project.py "C:\path\to\project"
```

It needs Python 3 and nothing else.

## Quality and security

See [docs/AUDIT.md](docs/AUDIT.md) for the audit: what was checked, what was fixed, and what was not tested.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

MIT. See [LICENSE](LICENSE).
