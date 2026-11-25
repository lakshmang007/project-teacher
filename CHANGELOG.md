# Changelog

All notable changes to this project are recorded here. This project follows [Semantic Versioning](https://semver.org/).

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
