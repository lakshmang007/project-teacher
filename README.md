# project-teacher

A Claude skill that turns any project into a learning guide and build plan.

Give it a project folder, or just an idea, and it will:

1. **Explain the concepts** the project uses, in plain words, with one everyday analogy each.
2. **Show the simplest way** it could have been built, and what that simpler way gives up.
3. **Give a prompt chain**: short, ordered prompts that build the project one step at a time.
4. **Create a checklist** with a "done when" test for every step.

It works for any language or stack. It is written for beginners who learn by building, and for experienced developers who want a fast walkthrough of an unfamiliar codebase.

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
│       │   ├── design-patterns.md     the 8-step pattern for building any project
│       │   ├── prompt-patterns.md     copy-ready prompts for each step
│       │   └── checklist-template.md  format for the build checklist
│       └── scripts/
│           └── scan_project.py   read-only project scanner (Python 3, standard library only)
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
