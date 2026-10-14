#!/usr/bin/env python3
"""PreToolUse guard for the autonomous NAMCG-Lab workflow.

Reads the hook JSON on stdin and exits 2 (block, message on stderr) for forbidden actions.
"""
import json
import os
import re
import subprocess
import sys

root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

tool = data.get("tool_name", "")
inp = data.get("tool_input", {}) or {}


def deny(msg):
    print("BLOCKED by .claude/hooks/guard.py: " + msg, file=sys.stderr)
    sys.exit(2)


def rel(path):
    p = os.path.abspath(path if os.path.isabs(path) else os.path.join(root, path))
    try:
        return os.path.relpath(p, root).replace("\\", "/")
    except ValueError:
        return p.replace("\\", "/")


def branch():
    try:
        return subprocess.run(
            ["git", "-C", root, "branch", "--show-current"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
    except Exception:
        return ""


ALLOWED_ALWAYS = ("proposals/", "scratch/", "reports/", ".claude/state/")
CHAPTERS_FLAG = os.path.join(root, ".claude", "state", "allow_chapters")
PROTECTED = ("agents/", ".claude/agents/", ".claude/hooks/", ".claude/commands/", ".claude/settings",
             "CLAUDE.md", "MILESTONE.md", "bib/", "code/", "figs/", "frontmatter/", "namcg-book7.tex")

if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
    path = inp.get("file_path") or inp.get("notebook_path") or ""
    r = rel(path)
    if r.startswith("../") or os.path.isabs(r):
        deny("write outside the repository: " + r)
    if r.startswith("chapters/"):
        if not os.path.exists(CHAPTERS_FLAG):
            deny("chapters/ may only be edited by the integrator step (flag .claude/state/allow_chapters absent)")
        if not branch().startswith("auto/"):
            deny("chapters/ edits are only allowed on an auto/* branch")
        old = inp.get("old_string", "") or ""
        new = inp.get("new_string", "") or ""
        for edit in inp.get("edits", []) or []:
            old += edit.get("old_string", "") or ""
            new += edit.get("new_string", "") or ""
        for token in ("CRITICAL PATH", "PROGRAMME-CONDITIONAL"):
            if old.count(token) > new.count(token):
                deny("edit would remove the status marker '%s'" % token)
        if re.search(r"Problem[s]?~?\s*[BCDFG]\b[^.]{0,40}\b(is|are)\s+(now\s+)?(closed|solved|derived)", new, re.I):
            deny("edit appears to declare a critical-path problem closed/solved")
    elif r.startswith(PROTECTED):
        deny("protected path: " + r)
    elif not r.startswith(ALLOWED_ALWAYS):
        deny("path not in the allowed write set (proposals/, scratch/, reports/): " + r)

elif tool == "Bash":
    cmd = inp.get("command", "") or ""
    low = cmd.lower()
    patterns = [
        (r"\bgit\s+push\b", "git push"),
        (r"\bgit\s+reset\s+--hard\b", "git reset --hard"),
        (r"\bgit\s+(clean)\b", "git clean"),
        (r"\bgit\s+(checkout|switch)\s+(-f\s+)?(main|master)\b", "switching to main/master"),
        (r"\bgit\s+merge\b", "git merge"),
        (r"\bgit\s+rebase\b", "git rebase"),
        (r"\bgit\s+branch\s+-[dD]\b", "branch deletion"),
        (r"\bgit\s+commit\b.*--amend", "git commit --amend"),
        (r"--no-verify", "--no-verify"),
        (r"\bgit\s+stash\b", "git stash"),
        (r"\bgit\s+restore\b(?!\s+--\s+namcg-book7\.pdf)(?!\s+--\s+chapters)", "git restore of other paths"),
        (r"remove-item[^;|&]*chapters|\brm\b[^;|&]*chapters|\bdel\b[^;|&]*chapters", "deleting chapters/"),
        (r"(>|>>|set-content|out-file|add-content|tee(-object)?)\s*['\"]?\.?[\\/]?chapters[\\/]", "shell write into chapters/"),
    ]
    for pat, name in patterns:
        if re.search(pat, low):
            deny("forbidden command: " + name)
    if re.search(r"\bgit\s+commit\b", low) and branch() in ("main", "master", ""):
        deny("commits are only allowed on an auto/* branch")
    if re.search(r"\bgit\s+(add|commit)\b", low) and branch() not in ("",) and not branch().startswith("auto/"):
        deny("git add/commit only on an auto/* branch")

sys.exit(0)
