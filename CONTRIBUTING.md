# Contributing

Thank you for helping. This skill is for beginners learning by building, so plain language matters as much as correct code.

## Ground rules

- Keep the skill in plain English: short sentences, no unexplained jargon.
- Keep the scanner standard-library only, read-only, and free of network calls.
- Never invent tools, libraries, or numbers in the skill's advice. If a claim cannot be checked, remove it or label it as unverified.

## Making a change

1. Fork the repository and create a branch.
2. Edit the files under `skills/project-teacher/`.
3. Test the scanner on at least two folders: one with a README containing non-ASCII text, and one with no README.
4. Update `CHANGELOG.md` under an "Unreleased" heading.
5. If the change affects security or behaviour, add a line to `docs/AUDIT.md`.
6. Open a pull request that says what changed and how you tested it.

## Running the scanner

```powershell
python -I skills\project-teacher\scripts\scan_project.py "C:\path\to\a\project"
python -I skills\project-teacher\scripts\scan_project.py "C:\does\not\exist"
```

The second command should print "Not a folder" and exit with an error.

## Adding a reference file

Put it in `skills/project-teacher/references/`, and link to it from `SKILL.md` with a note on when to read it. Keep each file short enough to read in one sitting.
