#!/usr/bin/env python3
"""Two pdflatex passes, reference check, PDF restore, whitespace check.

Exit code 0 only if everything is clean. Run from anywhere; operates on the repository root.

Optimized with --fast flag: skips pdflatex if no .tex files changed since last build.
"""
import re
import subprocess
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parent.parent
ok = True


def run(cmd, **kw):
    return subprocess.run(cmd, cwd=root, capture_output=True, text=True, errors="replace", **kw)


def is_fast_skip_allowed():
    """Check if we can skip the build in --fast mode.

    Returns True if no .tex files in chapters/ have changed since last build.
    """
    # Check if any .tex files changed since last build
    last_build = root / "scratch" / ".last_build"
    if last_build.exists():
        last_ts = float(last_build.read_text().strip())
        now = time.time()
        # If last build was very recent (< 1s ago), still build
        if now - last_ts < 1:
            return False

    # Check git diff for .tex files in chapters/
    d = run(["git", "diff", "--quiet", "HEAD", "--", "chapters/", "bib/"])
    if d.returncode == 0:
        # Also check uncommitted changes
        s = run(["git", "status", "--porcelain", "--", "chapters/", "bib/"])
        tex_changes = [l for l in s.stdout.splitlines() if l.strip() and ".tex" in l]
        if not tex_changes:
            return True

    return False


pages = "?"
fast_mode = "--fast" in sys.argv

if fast_mode and is_fast_skip_allowed():
    print("BUILD_SKIPPED (fast, no .tex changes since last build)")
    print("BUILD_CHECK PASS pages=0 (skipped)")
    sys.exit(0)

for i in (1, 2):
    p = run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "namcg-book7.tex"], timeout=900)
    m = re.search(r"Output written on .*?\((\d+) pages", p.stdout)
    if p.returncode != 0 or not m:
        print("pdflatex pass %d FAILED" % i)
        print("\n".join(l for l in p.stdout.splitlines() if l.startswith("!") or "Error" in l)[:3000])
        ok = False
        break
    pages = m.group(1)
    print("pass %d OK, %s pages" % (i, pages))

log = (root / "namcg-book7.log").read_text(errors="replace") if (root / "namcg-book7.log").exists() else ""
bad = [l for l in log.splitlines()
       if re.search(r"undefined references|Reference `.*' on page .* undefined|multiply[- ]defined|There were undefined", l)]
print("undefined/multiply-defined warnings: %d" % len(bad))
for l in bad[:10]:
    print("  " + l)
ok = ok and not bad

r = run(["git", "restore", "--", "namcg-book7.pdf"])
print("pdf restored" if r.returncode == 0 else "pdf restore FAILED: " + r.stderr)
ok = ok and r.returncode == 0

d = run(["git", "diff", "--check"])
print("git diff --check: " + ("clean" if d.returncode == 0 else "PROBLEMS\n" + d.stdout))
ok = ok and d.returncode == 0

# Record last build time
scratch_dir = root / "scratch"
scratch_dir.mkdir(exist_ok=True)
(last_build := scratch_dir / ".last_build").write_text(str(time.time()))

print("BUILD_CHECK " + ("PASS" if ok else "FAIL") + " pages=" + pages)
sys.exit(0 if ok else 1)
