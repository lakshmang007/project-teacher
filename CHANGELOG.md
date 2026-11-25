# Changelog

All notable changes to this project are recorded here. This project follows [Semantic Versioning](https://semver.org/).

## [0.3.1] - 2026-11-25

### Added
- `examples/`: real, unedited outputs (planning a new idea; explaining an existing project) and the to-do site built by following the skill's checklist.
- README: quick install at the top and a "See it in action" section.

### Fixed
- Checklist steps are now ordered so each "from day one" safeguard arrives no later than the step that needs it (for example, database access rules in the same step as sign-up). Found while reviewing the new-idea example.

## [0.3.0] - 2026-11-25

### Added
- **Domain expert role**: the skill names the project's field and briefs the user like an expert in it (where to start, what never to skip, common beginner mistakes). New `references/domains.md` covers websites, web apps with data, mobile, APIs, data and ML, automation, games, and hardware.
- **Idea shaping**: a one-sentence restatement, a small Version 1, "later" ideas, and one stretch question that invites the user's own twist.
- **Recommendations before the user asks**: new `references/recommendations.md` lists verified Claude skills (Ponytail, Superpowers, Anthropic example skills, Graphify) with install commands taken from their own READMEs, and free tools with their main limits.
- **Prompt coaching**: while building, the skill checks the user's own prompts for goal, file, exclusions and check, and shows an improved version.

## [0.2.0] - 2026-11-25

### Changed
- Skill description rewritten to trigger more reliably: names common phrasings ("walk me through this repo", "where do I start", "prompts to rebuild it") and lists what the skill is not for. Trigger test: 27/40 → 35/40 correct, with no false triggers (see docs/AUDIT.md).
- Step 4 ("simplest path") now has a separate comparison for new ideas, comparing real options instead of "how it was built".

### Added
- Accessibility is now part of the build: labels, clear button names and keyboard use go in the interface step of the design pattern, the skill's checklist rules, and the checklist template.
- Scanner recognises plain HTML/CSS/JavaScript websites (an `index.html` with no package or build file).

## [0.1.0] - 2026-11-25

### Added
- `project-teacher` skill: explains a project's concepts, shows the simplest build path, gives step-by-step prompts, and creates a build checklist.
- Reference files: the 8-step build pattern, copy-ready prompt templates, and the checklist format.
- `scan_project.py`: a read-only, standard-library scanner for a project's stack, entry points, file tree and README.
- Claude Code plugin manifest and marketplace file.
- Documentation: README, licence (MIT), contributing guide and audit report.

### Fixed (before release)
- Scanner no longer crashes on non-ASCII README text on Windows.
- SKILL.md now gives the full scanner path.
