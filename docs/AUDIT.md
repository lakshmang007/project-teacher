# Audit: project-teacher 0.1.0

This audit covers the skill files and the Python scanner. It was run by hand, with the commands listed below, on Windows 11 with Python 3.13.

## Summary

| Area | Result |
|---|---|
| Security | No network calls, no subprocesses, no writes. Passed. |
| Correctness (encoding) | One real bug found and fixed (see finding 1). |
| Correctness (symlinks) | Symlink loop does not hang. Passed. |
| Documentation | Install, usage, licence and contribution docs added. |
| Automated tests | None yet. Checks below were manual. |

## Findings

### 1. Scanner crashed on non-ASCII README text (fixed)

- **Severity:** Must fix. The scanner stopped with an error on a common project type.
- **Cause:** Windows consoles default to cp1252. A README containing characters such as `→` made `print()` raise `UnicodeEncodeError`.
- **Fix:** `scripts/scan_project.py` now sets stdout to UTF-8 with `errors="replace"` before printing.
- **Verified:** A README containing `Café → test` now prints correctly, both with the default console and with `PYTHONIOENCODING=cp1252`.

### 2. Ambiguous scanner path in SKILL.md (fixed)

- **Severity:** Should fix.
- **Cause:** The skill said `scripts/scan_project.py`, a path that only works from inside the skill folder. Claude runs it from the user's project folder.
- **Fix:** SKILL.md now gives the full invocation pattern: `python -I <this skill's folder>/scripts/scan_project.py "<project path>"`.

### 3. README stored in the wrong folder during build (fixed)

- **Severity:** Repository hygiene.
- **Cause:** The README was written inside the skill folder.
- **Fix:** Moved to the repository root. The installed copy was also cleaned up.

## Security checks

| Check | Method | Result |
|---|---|---|
| Network access | Search for `urllib`, `requests`, `socket` | None found |
| Command execution | Search for `subprocess`, `os.system`, `eval`, `exec` | None found |
| File writes | Search for write-mode `open()` | None found |
| Reads outside the target folder | Code review: paths come from `os.walk` of the argument | Only reads inside the target folder |
| Symlink loops | Ran the scanner on a folder containing a symlink to itself | Completed, no hang |
| Large output | Caps: 80 tree lines, 30 README lines, depth 3 | Bounded |

## Tests run

```
python -I scan_project.py <folder with Unicode README>           -> prints README, exit 0
PYTHONIOENCODING=cp1252 python -I scan_project.py <same folder>  -> prints README, exit 0
python -I scan_project.py <folder containing a symlink loop>     -> completes, exit 0
python -I scan_project.py /nonexistent                           -> "Not a folder", exit 1
```

## Not checked

- The plugin install path (`/plugin marketplace add`) was not tested in Claude Code. It needs a live GitHub push first.
- Whether Claude picks the skill for the trigger phrases in its description was not measured. The skill-creator evaluation loop has not been run.
- The scanner was tested only on Windows. macOS and Linux paths are expected to work but are unverified.
- The skill's advice on teaching and checklists was reviewed by reading, not by running real projects through it.

## Recommended next steps

1. Add an automated test script for the scanner, covering the cases above.
2. Run the skill-creator evaluation loop to check trigger accuracy.
3. Test the plugin install on macOS and Linux.
