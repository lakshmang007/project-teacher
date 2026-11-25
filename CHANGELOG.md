# Changelog

All notable changes to this project are recorded here. This project follows [Semantic Versioning](https://semver.org/).

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
