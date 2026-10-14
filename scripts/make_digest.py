#!/usr/bin/env python3
"""Build scratch/digest.md, a compact index of the manuscript chapters."""

import hashlib
import re
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
chap = root / "chapters"
out = root / "scratch" / "digest.md"
files = sorted(chap.rglob("*.tex"), key=lambda path: path.as_posix())


def content_hash():
    digest = hashlib.sha256()
    for path in files:
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()[:16]


def git(*args):
    return subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()


chapter_hash = content_hash()
head = git("rev-parse", "HEAD")
dirty_chapters = "yes" if git("status", "--porcelain", "--", "chapters") else "no"
if "--check" in sys.argv:
    expected_header = (
        "head: " + head,
        "chapters-hash: " + chapter_hash,
        "files: %d" % len(files),
        "dirty-chapters: " + dirty_chapters,
    )
    header = out.read_text(encoding="utf-8", errors="replace")[:600] if out.exists() else ""
    current = all(line in header for line in expected_header)
    print("DIGEST CURRENT" if current else "DIGEST STALE")
    sys.exit(0 if current else 1)

section = re.compile(r"\\(chapter|section|subsection|paragraph)\*?\{([^}]*)\}")
label = re.compile(r"\\label\{([^}]+)\}")
lines = [
    "# Manuscript digest (generated; do not edit)",
    "",
    "head: " + head,
    "chapters-hash: " + chapter_hash,
    "files: %d" % len(files),
    "dirty-chapters: " + dirty_chapters,
    "",
    "Read in full every passage you cite, edit or rely on. This digest does not replace that.",
    "",
]
labels = {}

for path in files:
    relative_path = path.relative_to(root).as_posix()
    source_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    lines.append("## %s (%d lines)" % (relative_path, len(source_lines)))
    for number, source_line in enumerate(source_lines, 1):
        match = section.search(source_line)
        if match:
            lines.append(
                "  L%d %s: %s"
                % (number, match.group(1), match.group(2)[:90])
            )
        for found_label in label.findall(source_line):
            labels.setdefault(found_label, []).append("%s:%d" % (path.name, number))
    lines.append("")

duplicates = {name: locations for name, locations in labels.items() if len(locations) > 1}
lines += ["## Duplicate labels"] + (
    ["  %s -> %s" % (name, ", ".join(locations)) for name, locations in duplicates.items()]
    or ["  none"]
)
lines += ["", "## Label index"] + [
    "  %s %s" % (name, locations[0]) for name, locations in sorted(labels.items())
]

for name in ("appH-microscopic-proofs.tex", "ch17-agenda.tex"):
    path = chap / name
    if not path.exists():
        continue
    lines += ["", "## Status lines in " + name]
    for number, source_line in enumerate(
        path.read_text(encoding="utf-8", errors="replace").splitlines(), 1
    ):
        if re.search(r"Status:|PROGRAMME-CONDITIONAL|CRITICAL PATH", source_line):
            lines.append("  L%d %s" % (number, source_line.strip()[:160]))

out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("wrote", out, "hash", chapter_hash)
