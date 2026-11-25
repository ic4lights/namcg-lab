#!/usr/bin/env python3
"""
Image-based margin checker that reads geometry from the master .tex,
saves offending pages as PNGs, and extracts nearby text/context.
"""

import pymupdf
import numpy as np
from PIL import Image
import os
import re
from pathlib import Path

PDF_PATH = "namcg-book7.pdf"
TEX_PATH = "namcg-book7.tex"
OUTPUT_DIR = Path("margin_violations")
DPI = 120

# Ignore headers/footers when measuring content bounds
IGNORE_TOP_FRAC = 0.12
IGNORE_BOTTOM_FRAC = 0.10

def parse_geometry(tex_path):
    """Extract geometry settings from the .tex file (comment- and whitespace-safe)."""
    if not os.path.exists(tex_path):
        raise FileNotFoundError(f"{tex_path} not found")

    text = open(tex_path, encoding="utf-8", errors="ignore").read()

    # Find the last geometry package (in case there are multiple)
    matches = list(re.finditer(r"\\usepackage\s*\[([^\]]*)\]\s*\{geometry\}", text, re.DOTALL))
    if not matches:
        raise ValueError("Could not find \\usepackage[...]{geometry}")

    options = matches[-1].group(1)  # use the last one
    settings = {}

    # Remove comments first, then split
    options_clean = re.sub(r"%.*", "", options)  # strip end-of-line comments
    for part in re.split(r",\s*", options_clean):
        part = part.strip()
        if not part or "=" not in part:
            continue
        k, v = part.split("=", 1)
        k = k.strip()
        v = v.strip()
        if v.endswith("in"):
            settings[k] = float(v[:-2])
        elif v.endswith("mm"):
            settings[k] = float(v[:-2]) / 25.4
        elif v.endswith("pt"):
            settings[k] = float(v[:-2]) / 72
        else:
            try:
                settings[k] = float(v)
            except ValueError:
                settings[k] = v

    # Defaults
    settings.setdefault("inner", 0.75)
    settings.setdefault("outer", 0.75)
    settings.setdefault("bindingoffset", 0.10)
    settings["inside"] = settings.get("inner", 0) + settings.get("bindingoffset", 0)
    settings.setdefault("top", 0.80)
    settings.setdefault("bottom", 0.80)

    print("Geometry settings read from TeX:")
    for k in ("inner", "bindingoffset", "inside", "outer", "top", "bottom"):
        if k in settings:
            print(f"  {k:15s} = {settings[k]:.3f} in")
    return settings

def inches_to_px(inches):
    return int(round(inches * DPI))

def get_content_bounds(arr):
    h, w = arr.shape[:2]
    top = int(h * IGNORE_TOP_FRAC)
    bottom = int(h * (1 - IGNORE_BOTTOM_FRAC))
    body = arr[top:bottom]
    mask = np.any(body < 242, axis=2)
    cols = np.any(mask, axis=0)
    if not np.any(cols):
        return None, None
    left = int(np.argmax(cols))
    right = int(w - np.argmax(cols[::-1]) - 1)
    return left, right

def extract_nearby_text(page, side, page_width_pt):
    """Extract text near the overflowing edge."""
    margin_pt = 90  # look within ~1.25" of the edge
    if side == "right":
        clip = pymupdf.Rect(page_width_pt - margin_pt, 0, page_width_pt, page.rect.height)
    else:  # left
        clip = pymupdf.Rect(0, 0, margin_pt, page.rect.height)

    text = page.get_text("text", clip=clip).strip()
    # Also get a bit more context from the full page around the same vertical region
    blocks = page.get_text("dict")["blocks"]
    nearby_lines = []
    for b in blocks:
        if b.get("type") != 0:
            continue
        for line in b.get("lines", []):
            bbox = pymupdf.Rect(line["bbox"])
            if side == "right" and bbox.x1 > page_width_pt - margin_pt:
                nearby_lines.append(line["spans"][0]["text"] if line["spans"] else "")
            elif side == "left" and bbox.x0 < margin_pt:
                nearby_lines.append(line["spans"][0]["text"] if line["spans"] else "")
    return text, "\n".join(nearby_lines)

def main():
    settings = parse_geometry(TEX_PATH)
    OUTPUT_DIR.mkdir(exist_ok=True)

    if not os.path.exists(PDF_PATH):
        print(f"{PDF_PATH} not found")
        return

    doc = pymupdf.open(PDF_PATH)
    total = len(doc)
    print(f"\nScanning {total} pages...\n")

    inside_px = inches_to_px(settings["inside"])
    outer_px = inches_to_px(settings["outer"])
    tolerance_px = inches_to_px(0.04)

    violations = []

    for i, page in enumerate(doc):
        page_num = i + 1
        pix = page.get_pixmap(dpi=DPI, alpha=False)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        arr = np.array(img)
        h, w = arr.shape[:2]

        left_px, right_px = get_content_bounds(arr)
        if left_px is None:
            continue

        left_inch = left_px / DPI
        right_inch = (w - 1 - right_px) / DPI

        is_odd = (page_num % 2 == 1)
        expected_left = inside_px if is_odd else outer_px
        expected_right = outer_px if is_odd else inside_px

        flags = []
        sides = []
        if left_px < expected_left - tolerance_px:
            flags.append(f"left ({left_inch:.2f}\" < {expected_left/DPI:.2f}\")")
            sides.append("left")
        if (w - right_px) < expected_right - tolerance_px:
            flags.append(f"right ({right_inch:.2f}\" < {expected_right/DPI:.2f}\")")
            sides.append("right")

        if flags:
            violations.append((page_num, flags, sides, left_inch, right_inch))
            print(f"Page {page_num}: {', '.join(flags)}")

            # Save full page PNG
            page_png = OUTPUT_DIR / f"page_{page_num:03d}.png"
            img.save(page_png)

            # Save cropped close-up of the overflowing side(s)
            for side in sides:
                if side == "right":
                    crop = img.crop((w - int(1.4 * DPI), 0, w, h))
                else:
                    crop = img.crop((0, 0, int(1.4 * DPI), h))
                crop_path = OUTPUT_DIR / f"page_{page_num:03d}_{side}_crop.png"
                crop.save(crop_path)

            # Extract nearby text
            page_width_pt = page.rect.width
            context_parts = []
            for side in sides:
                full_text, lines = extract_nearby_text(page, side, page_width_pt)
                context_parts.append(f"=== {side.upper()} edge context ===\n{full_text}\n\nLines near edge:\n{lines}")

            context_file = OUTPUT_DIR / f"page_{page_num:03d}_context.txt"
            context_file.write_text(
                f"Page {page_num}\nViolations: {', '.join(flags)}\n\n" + "\n\n".join(context_parts),
                encoding="utf-8"
            )

    print(f"\nPages violating geometry margins: {len(violations)}")
    print(f"Images and context files saved in: {OUTPUT_DIR.resolve()}")

    # Summary file
    summary = OUTPUT_DIR / "summary.txt"
    with open(summary, "w", encoding="utf-8") as f:
        f.write(f"Margin violations ({len(violations)} pages)\n")
        f.write(f"inside={settings['inside']:.2f}\"  outer={settings['outer']:.2f}\"\n\n")
        for p, flags, sides, l, r in violations:
            f.write(f"Page {p}: {', '.join(flags)}\n")
            f.write(f"  -> page_{p:03d}.png + crops + context.txt\n")

if __name__ == "__main__":
    main()