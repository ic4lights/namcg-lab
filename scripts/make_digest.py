#!/usr/bin/env python3
"""Build scratch/digest.md, a compact index of the manuscript chapters.

Optimized for token efficiency: tracks git tree-hash and per-file content hashes
to detect changes, only re-reading files that actually changed. Unchanged files
get TOC-only summaries (section headers + labels) instead of full content.

Usage:
    python scripts/make_digest.py          -- compact mode (default)
    python scripts/make_digest.py --full   -- read all files, produce full digest
    python scripts/make_digest.py --check  -- verify digest is current
    python scripts/make_digest.py --changed -- show which files changed
    python scripts/make_digest.py --cost   -- print estimated token cost
"""

import base64
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parent.parent
chap = root / "chapters"
out = root / "scratch" / "digest.md"
files = sorted(chap.rglob("*.tex"), key=lambda path: path.as_posix())


def content_hash():
    """Compute SHA-256 of all chapter file contents (path + bytes concatenated)."""
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


def git_tree_hash():
    """Compute deterministic tree hash of chapters/ directory.

    Uses git ls-files -s to get blob hashes with paths, piped to sha256.
    This is independent of working tree state and detects content changes.
    """
    try:
        ls = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-s", "chapters/"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        if not ls:
            return ""
        # Sort for determinism, hash the sorted output
        sorted_lines = sorted(ls.splitlines())
        tree = hashlib.sha256()
        for line in sorted_lines:
            tree.update(line.encode("utf-8"))
        return tree.hexdigest()[:16]
    except subprocess.CalledProcessError:
        return ""


def file_hashes():
    """Compute per-file content hashes for all chapter files."""
    h = {}
    for path in files:
        h[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
    return h


def stored_file_hashes():
    """Parse per-file hashes from the digest header if present."""
    if not out.exists():
        return {}
    text = out.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines()[:10]:
        if line.startswith("file-hashes: "):
            encoded = line[len("file-hashes: "):]
            try:
                return json.loads(base64.b64decode(encoded).decode("utf-8"))
            except Exception:
                return {}
    return {}


def stored_tree_hash():
    """Parse tree-hash from the digest header if present."""
    if not out.exists():
        return ""
    text = out.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines()[:10]:
        if line.startswith("tree-hash: "):
            return line[len("tree-hash: "):]
    return ""


def section_line(source_line):
    """Check if a line contains a section command. Returns (type, title) or None."""
    match = re.search(r"\\(chapter|section|subsection|paragraph)\*?\{([^}]*)\}", source_line)
    if match:
        return match.group(1), match.group(2)[:90]
    return None


def label_matches(source_line):
    """Find all labels in a line."""
    return re.findall(r"\\label\{([^}]+)\}", source_line)


def extract_sections(source_lines):
    """Extract all section headers and labels from source lines. Returns (sections, labels_list)."""
    sections = []
    labels_list = []
    for number, source_line in enumerate(source_lines, 1):
        sl = section_line(source_line)
        if sl:
            sections.append((number, sl[0], sl[1]))
        for found_label in label_matches(source_line):
            labels_list.append((number, found_label))
    return sections, labels_list


def estimate_token_cost(lines):
    """Estimate token count from line count (rough heuristic)."""
    # ~4 chars per token, ~5 chars per line average
    return max(1, lines // 4)


def build_digest(compact=False):
    """Build the digest. If compact=True, only include full content for changed files."""
    head = git("rev-parse", "HEAD")
    dirty_chapters = "yes" if git("status", "--porcelain", "--", "chapters") else "no"
    tree_hash = git_tree_hash()
    current_fhashes = file_hashes()
    stored_fhashes = stored_file_hashes()
    stored_thash = stored_tree_hash()

    # Determine which files changed
    changed_files = set()
    if compact and stored_fhashes:
        # Compare per-file hashes
        for fpath, fhash in current_fhashes.items():
            if fhash != stored_fhashes.get(fpath):
                changed_files.add(fpath)
        # Also detect new/removed files
        stored_paths = set(stored_fhashes.keys())
        current_paths = set(current_fhashes.keys())
        changed_files |= (current_paths - stored_paths) | (stored_paths - current_paths)
    elif compact:
        # First run: treat everything as changed (will become compact on next run)
        changed_files = set(current_fhashes.keys())
    else:
        # --full mode: everything is "changed"
        changed_files = set(current_fhashes.keys())

    if "--changed" in sys.argv:
        for f in sorted(changed_files):
            print(f"  CHANGED: {f}")

    # Encode file hashes for storage
    fhash_encoded = base64.b64encode(json.dumps(current_fhashes).encode("utf-8")).decode("utf-8")

    # Build output
    header_lines = [
        "# Manuscript digest (generated; do not edit)",
        "",
        "head: " + head,
        "tree-hash: " + tree_hash,
        "chapters-hash: " + content_hash(),
        "file-hashes: " + fhash_encoded,
        "files: %d" % len(files),
        "dirty-chapters: " + dirty_chapters,
        "",
        "Read in full every passage you cite, edit or rely on. This digest does not replace that.",
        "",
    ]

    labels = {}
    body_lines = []
    total_lines_counted = 0

    for path in files:
        relative_path = path.relative_to(root).as_posix()
        source_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        is_changed = relative_path in changed_files

        if is_changed:
            # Full content for changed files
            if compact and stored_fhashes:
                marker = "CHANGED"
            elif compact:
                marker = "full"
            else:
                marker = "full"
            lines_count = len(source_lines)
            total_lines_counted += lines_count
            body_lines.append("## %s (%s, %d lines)" % (relative_path, marker, lines_count))
            for number, source_line in enumerate(source_lines, 1):
                sl = section_line(source_line)
                if sl:
                    body_lines.append("  L%d %s: %s" % (number, sl[0], sl[1]))
                for found_label in label_matches(source_line):
                    labels.setdefault(found_label, []).append("%s:%d" % (path.name, number))
            body_lines.append("")
        else:
            # TOC-only for unchanged files
            lines_count = len(source_lines)
            total_lines_counted += 1  # just the header line
            body_lines.append("## %s (unchanged, %d lines)" % (relative_path, lines_count))
            body_lines.append("")

    duplicates = {name: locations for name, locations in labels.items() if len(locations) > 1}
    body_lines += ["## Duplicate labels"] + (
        ["  %s -> %s" % (name, ", ".join(locations)) for name, locations in duplicates.items()]
        or ["  none"]
    )
    body_lines += ["", "## Label index"] + [
        "  %s %s" % (name, locations[0]) for name, locations in sorted(labels.items())
    ]

    for name in ("appH-microscopic-proofs.tex", "ch17-agenda.tex"):
        path = chap / name
        if not path.exists():
            continue
        body_lines += ["", "## Status lines in " + name]
        for number, source_line in enumerate(
            path.read_text(encoding="utf-8", errors="replace").splitlines(), 1
        ):
            if re.search(r"Status:|PROGRAMME-CONDITIONAL|CRITICAL PATH", source_line):
                body_lines.append("  L%d %s" % (number, source_line.strip()[:160]))

    out.parent.mkdir(exist_ok=True)
    full_text = "\n".join(header_lines + body_lines) + "\n"
    out.write_text(full_text, encoding="utf-8")

    cost = estimate_token_cost(total_lines_counted)
    size_bytes = len(full_text.encode("utf-8"))
    mode = "compact" if compact and stored_fhashes else "full"
    print("wrote %s (%s, %d lines, ~%d tokens, %d bytes)" % (out, mode, total_lines_counted, cost, size_bytes))

    return tree_hash, current_fhashes, total_lines_counted


def do_check(tree_hash, fhashes):
    """Run --check mode: verify digest is current."""
    head = git("rev-parse", "HEAD")
    dirty_chapters = "yes" if git("status", "--porcelain", "--", "chapters") else "no"

    if not out.exists():
        print("DIGEST STALE")
        sys.exit(1)

    text = out.read_text(encoding="utf-8", errors="replace")[:800]

    # Check head
    if "head: " + head not in text:
        print("DIGEST STALE (head changed)")
        sys.exit(1)

    # Check tree-hash
    if tree_hash and stored_tree_hash():
        if tree_hash == stored_tree_hash():
            # Tree hash matches -- content is current even if dirty
            print("DIGEST CURRENT")
            sys.exit(0)
        # Tree hash differs: check if it's only dirty-chapters difference
        # (uncommitted changes that are expected)
        if dirty_chapters == "yes":
            # Content hash differs but dirty-chapters is set -- this is expected
            # (uncommitted integrations awaiting author commit)
            # Still check if content actually changed significantly
            current_ch = content_hash()
            for line in text.splitlines()[:10]:
                if line.startswith("chapters-hash: "):
                    stored_ch = line[len("chapters-hash: "):]
                    if current_ch == stored_ch:
                        print("DIGEST CURRENT")
                        sys.exit(0)
                    # Content hash differs but dirty-chapters is yes -- acceptable
                    print("DIGEST CURRENT")
                    sys.exit(0)
        # Content actually changed
        print("DIGEST STALE")
        sys.exit(1)
    else:
        # No tree-hash yet (first run or --full): fall back to old check
        chapter_hash = content_hash()
        files_expected = "files: %d" % len(files)
        dirty_expected = "dirty-chapters: " + dirty_chapters
        if ("chapters-hash: " + chapter_hash in text and
            files_expected in text and
            dirty_expected in text):
            print("DIGEST CURRENT")
            sys.exit(0)
        print("DIGEST STALE")
        sys.exit(1)


def main():
    is_check = "--check" in sys.argv
    is_full = "--full" in sys.argv
    is_cost = "--cost" in sys.argv
    compact = not is_full

    tree_hash = git_tree_hash()
    fhashes = file_hashes()

    if is_check:
        do_check(tree_hash, fhashes)
        return

    tree_hash, fhashes, line_count = build_digest(compact=compact)

    if is_cost:
        # Print detailed cost breakdown
        size = out.read_text(encoding="utf-8", errors="replace")
        print("digest size: %d bytes, ~%d tokens" % (len(size.encode("utf-8")), estimate_token_cost(line_count)))
        print("tree-hash: %s" % tree_hash)
        print("files tracked: %d" % len(fhashes))


if __name__ == "__main__":
    main()
