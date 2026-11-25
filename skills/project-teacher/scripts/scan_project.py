"""Read-only scan of a project folder: tree, stack, entry points, README head.

Usage: python -I scan_project.py "<project path>"

Standard library only. Never writes or changes files.
"""
import os
import sys

SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv", "env",
    "dist", "build", "target", ".next", ".idea", ".vscode", "graphify-out",
}

STACK_MARKERS = {
    "package.json": "Node.js (JavaScript/TypeScript)",
    "requirements.txt": "Python (pip)",
    "pyproject.toml": "Python (pyproject)",
    "Pipfile": "Python (pipenv)",
    "Cargo.toml": "Rust",
    "go.mod": "Go",
    "pom.xml": "Java (Maven)",
    "build.gradle": "Java/Kotlin (Gradle)",
    "pubspec.yaml": "Dart/Flutter",
    "Gemfile": "Ruby",
    "composer.json": "PHP",
    "Dockerfile": "Docker container",
    "docker-compose.yml": "Docker Compose",
    "Makefile": "Make",
    ".github/workflows": "GitHub Actions (CI)",
}

ENTRY_NAMES = {
    "main.py", "app.py", "manage.py", "server.py", "index.js", "index.ts",
    "main.js", "main.ts", "main.go", "main.rs", "App.jsx", "App.tsx",
    "Main.java", "index.html", "cli.py", "__main__.py",
}

MAX_TREE_LINES = 80
MAX_DEPTH = 3
README_LINES = 30


def walk(root):
    """Yield (relative_path, is_dir) for entries, skipping noise folders."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        rel_dir = os.path.relpath(dirpath, root)
        depth = 0 if rel_dir == "." else rel_dir.count(os.sep) + 1
        if depth > MAX_DEPTH:
            dirnames[:] = []
            continue
        yield rel_dir, True, depth
        for name in sorted(filenames):
            yield os.path.join(rel_dir, name), False, depth + 1


def main():
    # Windows consoles default to cp1252; READMEs may contain other characters.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) != 2:
        print("Usage: python -I scan_project.py \"<project path>\"")
        return 1
    root = os.path.abspath(sys.argv[1])
    if not os.path.isdir(root):
        print(f"Not a folder: {root}")
        return 1

    print(f"Project: {root}")
    print()

    stack = []
    for marker, label in STACK_MARKERS.items():
        if os.path.exists(os.path.join(root, marker)):
            stack.append(label)
    print("Detected stack:")
    print("  " + ("\n  ".join(stack) if stack else "none recognised (ask the user)"))
    print()

    entries = []
    file_count = 0
    ext_counts = {}
    tree_lines = []
    for rel, is_dir, depth in walk(root):
        if is_dir:
            if rel != ".":
                tree_lines.append("  " * (depth - 1) + os.path.basename(rel) + "/")
            continue
        file_count += 1
        name = os.path.basename(rel)
        ext = os.path.splitext(name)[1].lower() or "(no extension)"
        ext_counts[ext] = ext_counts.get(ext, 0) + 1
        if name in ENTRY_NAMES:
            entries.append(rel)
        if len(tree_lines) < MAX_TREE_LINES:
            tree_lines.append("  " * max(depth - 1, 0) + name)

    print(f"Files: {file_count}")
    top_exts = sorted(ext_counts.items(), key=lambda kv: -kv[1])[:8]
    print("Most common file types: " + ", ".join(f"{e} ({n})" for e, n in top_exts))
    print()

    print("Likely entry points:")
    print("  " + ("\n  ".join(entries) if entries else "none found by name (check the README)"))
    print()

    print(f"Tree (first {MAX_TREE_LINES} lines, depth {MAX_DEPTH}):")
    for line in tree_lines[:MAX_TREE_LINES]:
        print("  " + line)
    if len(tree_lines) > MAX_TREE_LINES:
        print("  ... more files not shown")
    print()

    for readme in ("README.md", "README.txt", "README", "readme.md"):
        path = os.path.join(root, readme)
        if os.path.isfile(path):
            print(f"README head ({readme}, first {README_LINES} lines):")
            with open(path, encoding="utf-8", errors="replace") as fh:
                for i, line in enumerate(fh):
                    if i >= README_LINES:
                        print("  ...")
                        break
                    print("  " + line.rstrip())
            break
    else:
        print("No README found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
