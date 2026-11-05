#!/usr/bin/env python3
"""Extract detailed paragraphs from appH-microscopic-proofs.tex into appH-detailed.tex.

This script:
1. Identifies detailed paragraphs (conditional results, no-gos, bounded results with derivations)
2. Extracts them to a new file with proper labels
3. Replaces each in appH with a compact reference (one line with label)
4. Preserves CRLF line endings
"""

import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
appH_path = root / "chapters" / "appH-microscopic-proofs.tex"
detailed_path = root / "chapters" / "appH-detailed.tex"


def read_lines(path):
    """Read file and return lines (preserving content, not line endings)."""
    text = path.read_text(encoding="utf-8")
    return text.splitlines()


def write_lines(path, lines):
    """Write lines to file with CRLF line endings."""
    text = "\r\n".join(lines)
    path.write_text(text, encoding="utf-8")


def extract_blocks(lines):
    """Extract paragraph blocks from appH lines."""
    blocks = []
    current_section = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("\\paragraph{"):
            para_title = line.strip()
            para_start = i
            para_section = current_section
            i += 1
            while i < len(lines):
                if lines[i].startswith("\\paragraph{") or lines[i].startswith("\\section{"):
                    break
                i += 1
            para_end = i - 1
            current_section = current_section or para_section
            blocks.append({
                "start": para_start,
                "end": para_end,
                "title": para_title,
                "section": current_section,
                "lines": lines[para_start:para_end + 1],
            })
        elif line.startswith("\\section{Problem"):
            current_section = line.strip()
        i += 1
    return blocks


def categorize_blocks(blocks):
    """Categorize blocks as detailed (to move) or main (to stay)."""
    detailed = []
    main = []
    for b in blocks:
        content = b["lines"][1:]  # skip the \\paragraph line
        content_text = "\n".join(content)
        has_conditional = (
            "conditional" in b["title"].lower()
            or "bounded" in b["title"].lower()
            or "not closure" in b["title"].lower()
            or "no-ghost" in b["title"].lower()
        )
        has_equation = "\\[" in content_text or "tabular" in content_text
        is_long = len(content) > 6

        if has_conditional or has_equation or is_long:
            detailed.append(b)
        else:
            main.append(b)
    return detailed, main


def make_label(section, title, idx):
    """Create a unique label for a detailed paragraph."""
    # Extract problem letter from section
    problem = ""
    if section:
        m = re.search(r"Problem\s+([A-Z])", section)
        if m:
            problem = m.group(1)
    # Clean title for label
    clean = re.sub(r"[^\w]", "", title.lower())
    return f"detail:sec-{problem}-{clean[:30]}-{idx}"


def clean_section_name(section):
    """Clean section name for use in labels."""
    if not section:
        return "uncategorized"
    # Remove \section{...} wrapper if present
    if section.startswith("\\section{") and section.endswith("}"):
        section = section[9:-1]
    return section.replace("\\", "")


def build_detailed_file(detailed_blocks):
    """Build the detailed file content."""
    lines = [
        "\\chapter{Status of the Open Problems -- Detailed Derivations}",
        "\\label{app:status-detailed}",
        "",
        "This file contains the detailed derivations, conditional results,",
        "no-gos, and bounded results that were previously interleaved in",
        "appH-microscopic-proofs.tex. Each block is labeled for cross-reference.",
        "",
    ]

    current_section = None
    current_section_label = None
    idx = 0
    for b in detailed_blocks:
        clean_sec = clean_section_name(b["section"])
        if clean_sec != current_section:
            current_section = clean_sec
            sec_label = f"sec:detailed-{clean_sec}"
            lines.append("")
            lines.append(f"\\section{{{current_section}}}")
            lines.append(f"\\label{{{sec_label}}}")
            lines.append("")
            current_section_label = sec_label

        label = make_label(b["section"], b["title"], idx)
        # The title already has \\paragraph{...}, so just use it
        title_content = b["title"]
        if title_content.startswith("\\paragraph{"):
            title_content = title_content[11:-1]  # strip \\paragraph{}
        lines.append(f"\\paragraph{{{title_content}}} \\label{{{label}}}")

        # Add content lines, removing empty lines within math blocks
        content_lines = b["lines"][1:]  # skip the \\paragraph line
        in_math = False
        for cl in content_lines:
            stripped = cl.strip()
            if stripped == "\\[" or stripped == "\\]":
                in_math = not in_math
                lines.append(cl)
            elif stripped == "":
                if not in_math:
                    lines.append(cl)
                # else: skip empty lines within math
            else:
                lines.append(cl)

        lines.append("")
        idx += 1

    return lines


def build_compact_appH(lines, detailed_ranges):
    """Build the compact appH with detailed paragraphs replaced by references."""
    detailed_ranges = sorted(detailed_ranges, key=lambda x: x[0])

    # First, collect all detailed blocks with their problem letters
    detailed_with_problem = []
    for start, end in detailed_ranges:
        problem = ""
        for j in range(max(0, start - 20), start):
            if lines[j].startswith("\\section{Problem"):
                m = re.search(r"Problem\s+([A-Z])", lines[j])
                if m:
                    problem = m.group(1)
                break
        detailed_with_problem.append((start, end, problem))

    # Build result by iterating through lines
    result = []
    detail_idx = 0
    i = 0

    while i < len(lines):
        # Check if this line starts a detailed block
        if detail_idx < len(detailed_ranges):
            start, end = detailed_ranges[detail_idx]
            if i == start:
                # Replace this block with a compact reference
                _, _, problem = detailed_with_problem[detail_idx]
                compact_ref = (
                    f"\\paragraph{{Detailed derivation {detail_idx + 1} "
                    f"(Problem {problem}; conditional result).}} \\label{{ref:detail-{detail_idx}}} % [see appH-detailed.tex]"
                )
                result.append(compact_ref)
                result.append("")
                i = end + 1
                detail_idx += 1
                continue

        result.append(lines[i])
        i += 1

    return result


def main():
    """Run the extraction."""
    lines = read_lines(appH_path)
    blocks = extract_blocks(lines)
    detailed, main = categorize_blocks(blocks)

    print(f"appH-microscopic-proofs.tex: {len(lines)} lines, {len(lines) * 100} bytes (est)")
    print(f"  Detailed blocks to extract: {len(detailed)}")
    print(f"  Main blocks to stay: {len(main)}")

    # Build detailed file
    detailed_lines = build_detailed_file(detailed)
    write_lines(detailed_path, detailed_lines)
    print(f"\nWrote {detailed_path}: {len(detailed_lines)} lines")

    # Build compact appH
    # Find the ranges of detailed blocks in the original lines
    detailed_ranges = []
    for b in detailed:
        detailed_ranges.append((b["start"], b["end"]))

    # Build compact appH by replacing detailed blocks
    compact_lines = list(lines)
    # Process in reverse order to preserve indices
    for start, end in reversed(detailed_ranges):
        # Replace the block with a compact reference
        problem = ""
        for j in range(max(0, start - 20), start):
            if compact_lines[j].startswith("\\section{Problem"):
                m = re.search(r"Problem\s+([A-Z])", compact_lines[j])
                if m:
                    problem = m.group(1)
                break

        idx = detailed_ranges.index((start, end))
        compact_ref = (
            f"\\paragraph{{Detailed derivation {idx + 1} "
            f"(Problem {problem}; conditional result).}} \\label{{ref:detail-{idx}}} % [see appH-detailed.tex]"
        )
        # Replace lines[start:end+1] with compact_ref
        compact_lines[start : end + 1] = [compact_ref, ""]

    compact_path = root / "chapters" / "appH-microscopic-proofs-compact.tex"
    write_lines(compact_path, compact_lines)
    print(f"Wrote {compact_path}: {len(compact_lines)} lines")

    # Show savings
    savings = len(lines) - len(compact_lines)
    print(f"Savings: {savings} lines ({100 * savings / len(lines):.0f}%)")


if __name__ == "__main__":
    main()
