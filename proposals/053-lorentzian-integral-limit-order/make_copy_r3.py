#!/usr/bin/env python3
"""Proposal 053, round 3: copy the tracked files of the working tree, except proposals/,
reports/, .claude/ and agents/, to a directory OUTSIDE the repository, for the build check.

usage: python make_copy_r3.py <dst>        (dst must lie outside the repository)
Read-only git (git ls-files). Writes only inside <dst>.
"""
import subprocess, pathlib, shutil, sys

ROOT = pathlib.Path(r"C:/Users/redgi/Projects/namcg-lab@gpu")
EXCL = ("proposals/", "reports/", ".claude/", "agents/")

def main():
    dst = pathlib.Path(sys.argv[1]).resolve()
    if dst == ROOT or ROOT in dst.parents:
        sys.exit("refusing: destination is the repository or lies inside it")
    files = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True).stdout
    names = [f.decode() for f in files.split(b"\0") if f]
    n = 0
    for s in names:
        if s.startswith(EXCL):
            continue
        src = ROOT / s
        if not src.is_file():
            continue
        out = dst / s
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, out)
        n += 1
    print("copied", n, "tracked files to", dst, "of", len(names), "tracked")

main()
