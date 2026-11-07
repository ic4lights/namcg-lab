#!/usr/bin/env python3
"""Render the NAMCG mission graph manifest (YAML) to a PNG.

Usage:
    python scripts/render_mission_graph.py [manifest.yaml] [out.png]

Defaults:
    manifest: reports/graph/mission-graph.yaml
    output:   reports/graph/mission-graph.png

Layout (neural-network style, schema v2 - math everywhere):
    col 0     QM input symbols as mathtext (circles, from qm nodes' symbols_out
              + render_math.symbols; manuscript-stated values shown where they exist)
    col 1     premises as mathtext (diamonds, render_math.premises)
    middle    namcg + ir derivation stages drawn AS their central manuscript
              formula (render_math.displays), one column per dependency depth
              (longest-path layering); red dashed border + "BLOCKED" tag when a
              gap or an open required upstream starves them; amber dashed +
              "+open-input" when only conditional upgrade paths are open
    last      the GR criterion outputs as mathtext (goal circles; red dashed
              ring + "BLOCKED - <reason>" when gaps or blocked layers feed them)

Blocking is computed from the manifest: a node is blocked if it appears in a
gaps: entry, consumes a gap symbol, or receives a required edge from an open or
blocked node (fixed point). Values/units appear only where the manuscript
states a number (render_math vsrc); nothing is invented.

Edges carry no text (that is what made an earlier render unreadable); the
symbol bridge for every edge stays in the YAML. Node state is shown by fill
color AND a compact text tag, so state never rests on color alone.

This script only draws what the manifest says and reports validation warnings;
it never invents nodes, edges or statuses.
"""

import os
import re
import sys
import textwrap

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML is required: python -m pip install pyyaml\n")
    sys.exit(2)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle, RegularPolygon
from matplotlib.lines import Line2D

DEFAULT_MANIFEST = os.path.join("reports", "graph", "mission-graph.yaml")
DEFAULT_OUT = os.path.join("reports", "graph", "mission-graph.png")

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
SEC = "#52514e"
MUTED = "#898781"
GRID = "#c3c2b7"

# derivation node state -> (fill, ink, compact tag, legend label)
STATE_STYLE = {
    "foundation":           ("#e1e0d9", INK, "FOUND",     "foundation node"),
    "derived":              ("#0ca30c", "#ffffff", "DERIVED", "closed: DERIVED"),
    "closed-conditionally": ("#2a78d6", "#ffffff", "COND",  "closed conditionally"),
    "open-critical":        ("#d03b3b", "#ffffff", "OPEN CP", "open - critical path"),
    "open-optional":        ("#ec835a", INK, "OPEN OPT", "open - optional"),
    "goal":                 ("#fcfcfb", INK, "GOAL",     "GR criterion output (not yet met)"),
}
EDGE_STYLE = {
    "required":    ("solid",        SEC,    1.15),
    "conditional": ((0, (1.5, 1.8)), MUTED, 1.0),
    "supports":    ((0, (5, 3)),    MUTED,  0.9),
    "gap":         ((0, (6, 3)),    "#d03b3b", 1.7),
}

NODE_W = 3.6
NODE_H = 1.24
CIRCLE_R = 0.30
BLOCK_COLOR = "#d03b3b"
UPGRADE_COLOR = "#fab219"
DPI = 200


def label_bg(t):
    """Knock a surface-colored halo behind free-floating text so wires that
    pass near it never run through the glyphs."""
    t.set_bbox(dict(facecolor=SURFACE, edgecolor="none", pad=0.5, alpha=0.85))
    return t


def base_name(sym):
    """Display form: drop a trailing parenthetical qualifier."""
    return re.sub(r"\s*\([^()]*\)\s*$", "", str(sym)).strip()


def one_line(text, width=34):
    s = " ".join(str(text).split())
    if len(s) > width:
        s = s[: width - 1] + "…"
    return s


class Graph:
    def __init__(self, manifest):
        self.warnings = []
        self.nodes = {n["id"]: n for n in manifest.get("nodes") or []}
        self.edges = manifest.get("edges") or []
        self.inputs = manifest.get("inputs") or []
        self.gaps = manifest.get("gaps") or []
        self.manifest = manifest
        rm = manifest.get("render_math") or {}
        self.sym_math = rm.get("symbols") or {}    # symbol name -> {math,note,value,vsrc}
        self.prem_math = rm.get("premises") or {}  # premise symbol -> {math,note}
        self.disp = rm.get("displays") or {}       # node id -> {label,math,math2,note,value,vsrc}
        self.circles = {}     # input-symbol circles: id -> dict(label, full, group, math...)
        self.diamonds = {}    # premise nodes: id -> dict(label, math, note)
        self.goals = {}       # gr node id -> dict(label, math, note, label_name, blocked)
        self.blocked = set()      # node ids starved by gaps / open upstream (fixed point)
        self.reason = {}          # node id -> list of human-readable block reasons
        self.upgrade = set()      # node ids reachable only by conditional edges from open/blocked
        self.up_reason = {}
        self.deriv = [nid for nid, n in self.nodes.items()
                      if n.get("layer") in ("namcg", "ir")]
        self.links = []       # (a, b, kind) between drawn node ids
        self.back_edges = set()
        self._build()

    def _qm_circles(self):
        for nid, n in self.nodes.items():
            if n.get("layer") != "qm":
                continue
            for k, sym in enumerate(n.get("symbols_out") or []):
                cid = "%s#sym%d" % (nid, k)
                m = self.sym_math.get(str(sym))
                if m is None:
                    for key, val in self.sym_math.items():
                        if base_name(key) == base_name(sym):
                            m = val
                            break
                m = m or {}
                self.circles[cid] = {"label": base_name(sym), "full": sym, "group": nid,
                                     "math": m.get("math", ""), "note": m.get("note", ""),
                                     "value": m.get("value", ""), "vsrc": m.get("vsrc", "")}

    def _build(self):
        self._qm_circles()
        for i, inp in enumerate(self.inputs):
            sym = str(inp.get("symbol", "?"))
            m = self.prem_math.get(sym) or self.prem_math.get(base_name(sym)) or {}
            self.diamonds["inp#%d" % i] = {"label": base_name(sym),
                                           "math": m.get("math", ""), "note": m.get("note", "")}
        for nid, n in self.nodes.items():
            if n.get("layer") == "gr":
                d = self.disp.get(nid) or {}
                self.goals[nid] = {"label": one_line(n.get("title", nid), 30),
                                   "math": d.get("math", ""), "note": d.get("note", ""),
                                   "label_name": d.get("label", ""), "blocked": False}
        # links
        for e in self.edges:
            f, t, kind = e.get("from"), e.get("to"), e.get("kind", "required")
            if f not in self.nodes and t not in self.nodes:
                self.warnings.append("edge with unknown endpoints: %r->%r" % (f, t))
                continue
            if kind not in EDGE_STYLE:
                self.warnings.append("edge %s->%s has unknown kind %r" % (f, t, kind))
                kind = "required"
            if f.startswith("qm."):
                matched = self._match_qm_circles(f, e.get("symbols") or [])
                if not matched:
                    self.warnings.append("edge %s->%s: no input symbol matched its symbols list; "
                                         "attaching all symbols of %s" % (f, t, f))
                    matched = [c for c in self.circles if self.circles[c]["group"] == f]
                tgt = t if t in self.nodes else None
                for c in matched:
                    if tgt in self.goals:
                        self.links.append((c, tgt, kind))
                    elif tgt in self.deriv:
                        self.links.append((c, tgt, kind))
                    else:
                        self.warnings.append("edge target unknown: %r" % t)
            elif t.startswith("gr."):
                if f in self.deriv or f in self.circles:
                    self.links.append((f, t, kind))
                else:
                    self.warnings.append("edge %s->%s: source unknown" % (f, t))
            else:
                if f in self.deriv and t in self.deriv:
                    self.links.append((f, t, kind))
                else:
                    self.warnings.append("edge %s->%s: endpoints not derivations" % (f, t))
        # premise diamonds -> users
        for i, inp in enumerate(self.inputs):
            did = "inp#%d" % i
            for user in inp.get("used_by") or []:
                if user in self.deriv or user in self.goals:
                    self.links.append((did, user, "conditional"))
                elif user.startswith("qm."):
                    for c in [c for c in self.circles if self.circles[c]["group"] == user]:
                        self.links.append((did, c, "conditional"))
                else:
                    self.warnings.append("input used_by unknown node: %r" % user)
        # isolated qm symbols: note (drawn, labelled unused)
        used = set(b for _, b, _ in self.links)
        self.unused_symbols = [c for c in self.circles if c not in used and c not in
                               set(a for a, _, _ in self.links)]
        self._compute_blocked()
        self._layer()

    def _compute_blocked(self):
        """Blocked = the node needs something the graph does not supply.
        (1) named in gaps.blocks, or a gap symbol feeds its symbols_in;
        (2) a REQUIRED link from an open or blocked node (fixed point);
        supports/conditional links never propagate blocking - an open problem
        target is simply unsupplied. Conditional feeders instead mark the
        target 'upgrade': the only path into it runs through something still open."""
        self.open_set = set(nid for nid, n in self.nodes.items()
                            if str(n.get("state", "")).startswith("open"))
        self.reason = {nid: [] for nid in self.nodes}
        self.up_reason = {nid: [] for nid in self.nodes}
        gap_syms = [(base_name(gp.get("symbol", "?")), set(gp.get("blocks") or []))
                    for gp in self.gaps]
        for nid, n in self.nodes.items():
            for gsym, blocks in gap_syms:
                if nid in blocks:
                    self.reason[nid].append("gap: " + gsym)
                elif any(base_name(s) == gsym for s in (n.get("symbols_in") or [])):
                    self.reason[nid].append("gap input: " + gsym)
        self.blocked = set(nid for nid in self.nodes if self.reason[nid])
        changed = True
        while changed:
            changed = False
            for a, b, kind in self.links:
                if kind != "required" or b not in self.nodes or b in self.blocked:
                    continue
                if a in self.open_set or a in self.blocked:
                    self.blocked.add(b)
                    self.reason[b].append("unmet input from " + a)
                    changed = True
        for a, b, kind in self.links:
            if kind != "conditional" or b not in self.nodes or b in self.blocked:
                continue
            if a in self.open_set or a in self.blocked:
                self.upgrade.add(b)
                self.up_reason[b].append("only path runs through open " + a)
        for nid in self.goals:
            self.goals[nid]["blocked"] = nid in self.blocked

    def _match_qm_circles(self, qm_id, symbol_strings):
        out = []
        for s in symbol_strings:
            head = s.split("->")[0].strip()
            for cid, c in self.circles.items():
                if c["group"] != qm_id:
                    continue
                if head.startswith(c["label"]) or c["label"] in s:
                    out.append(cid)
        seen, ded = set(), []
        for cid in out:
            if cid not in seen:
                seen.add(cid)
                ded.append(cid)
        return ded

    def _layer(self):
        """Longest-path layering over derivation nodes; cycle back-edges recorded."""
        preds = {n: [] for n in self.deriv}
        succs = {n: [] for n in self.deriv}
        for a, b, k in self.links:
            if a in self.deriv and b in self.deriv:
                preds[b].append(a)
                succs[a].append(b)
        layer = {}
        state = {n: 0 for n in self.deriv}  # 0 unvisited, 1 in stack, 2 done

        def resolve(n):
            if state[n] == 2:
                return layer[n]
            if state[n] == 1:  # cycle: drop the back edge for layering
                state[n] = 2
                layer[n] = 1
                return 1
            state[n] = 1
            best = 1
            for p in preds[n]:
                pl = resolve(p)
                best = max(best, pl + 1)
            state[n] = 2
            layer[n] = best
            return best

        for n in self.deriv:
            resolve(n)
        # Depth is anchored by the nodes that actually feed the GR output
        # column ("terminal"). Optional side branches that reach no goal are
        # pulled back to the last terminal stage so they do not trail past the
        # outputs as one-node tail columns.
        succ_all = {}
        for a, b, k in self.links:
            succ_all.setdefault(a, []).append(b)
        goal_ids = set(self.goals)
        terminal = set()
        stack = [n for n in self.deriv if any(b in goal_ids for b in succ_all.get(n, []))]
        terminal.update(stack)
        while stack:
            n = stack.pop()
            for a, b, k in self.links:
                if b == n and a in self.deriv and a not in terminal:
                    terminal.add(a)
                    stack.append(a)
        maxterm = max([layer[n] for n in terminal], default=1)
        for n in self.deriv:
            if n in terminal:
                continue
            tl = max([layer[p] for p in preds[n] if p in terminal], default=0)
            layer[n] = max(min(layer[n], maxterm), tl + 1)
        self.terminal = terminal
        self.layer = layer
        self.n_hidden = max(layer.values()) if layer else 0
        self.succs = succs
        self.preds = preds

    def columns(self):
        """Ordered columns: [circles], [diamonds], hidden cols 1..n, [goals]."""
        cols = []
        cols.append(list(self.circles.keys()))
        cols.append(list(self.diamonds.keys()))
        hidden = [[] for _ in range(self.n_hidden)]
        for nid in self.deriv:
            hidden[self.layer[nid] - 1].append(nid)
        # barycenter ordering: two forward sweeps, one backward
        def index_map(col):
            return {nid: i for i, nid in enumerate(col)}
        idx = {}
        for c in cols + hidden:
            for i, nid in enumerate(c):
                idx[nid] = i
        for sweep in range(3):
            for h in hidden:
                def key(nid):
                    ps = [idx[p] for p in self.preds[nid] if p in idx]
                    return sum(ps) / len(ps) if ps else idx.get(nid, 0)
                h.sort(key=key)
                for i, nid in enumerate(h):
                    idx[nid] = i
            for h in reversed(hidden):
                def key(nid):
                    ss = [idx[s] for s in self.succs[nid] if s in idx]
                    return sum(ss) / len(ss) if ss else idx.get(nid, 0)
                h.sort(key=key)
                for i, nid in enumerate(h):
                    idx[nid] = i
        cols.extend(hidden)
        cols.append(list(self.goals.keys()))
        # order the input columns by the (weighted) position of their targets,
        # so most wires run horizontally instead of fanning across rows
        def source_key(nid):
            ts = [idx[b] for a2, b, k in self.links if a2 == nid and b in idx]
            return sum(ts) / len(ts) if ts else 0.0
        for col in (cols[0], cols[1]):
            col.sort(key=source_key)
            for i, nid in enumerate(col):
                idx[nid] = i
        return cols

    def node_label(self, nid):
        if nid in self.circles:
            return ("circle", self.circles[nid]["label"])
        if nid in self.diamonds:
            return ("diamond", self.diamonds[nid])
        if nid in self.goals:
            return ("goal", self.goals[nid]["label"])
        n = self.nodes[nid]
        tag = STATE_STYLE.get(n.get("state"), ("", "", "?", ""))[2]
        return ("rect", one_line(n.get("title", nid), 30), nid, tag)


def _fit_text(t, max_w_px, renderer, min_fs=4.5):
    """Shrink a text artist until it fits a width budget (display px)."""
    fs = t.get_fontsize()
    start = fs
    while fs > min_fs:
        e = t.get_window_extent(renderer)
        if e.width <= max_w_px:
            break
        fs = max(min_fs, fs * max_w_px / max(1.0, e.width) - 0.1)
        t.set_fontsize(fs)
    if fs < start - 0.05 and fs < 5.8:
        sys.stderr.write("FITWARN: %r shrunk %.1f -> %.1f pt\n"
                         % (t.get_text()[:30], start, fs))
    return t


def _overflow(texts, patches, rect_nodes, renderer):
    """Hard check: every text of a boxed node must sit >= 80% inside its box."""
    out = []
    pmap = {o: _bb(p, renderer) for o, p in patches}
    for owner, t in texts:
        if owner not in rect_nodes:
            continue
        bb, pbb = _bb(t, renderer), pmap.get(owner)
        if pbb is None or _area(bb) == 0:
            continue
        if _inter(bb, pbb) < 0.80 * _area(bb):
            out.append("BOX-OVERFLOW  text %r of %s escapes its box"
                       % (t.get_text()[:24], owner))
    return out


def _bb(o, renderer):
    e = o.get_window_extent(renderer)
    return (e.x0, e.y0, e.x1, e.y1)


def _area(b):
    return max(0.0, b[2] - b[0]) * max(0.0, b[3] - b[1])


def _inter(a, b):
    x0, x1 = max(a[0], b[0]), min(a[2], b[2])
    y0, y1 = max(a[1], b[1]), min(a[3], b[3])
    if x1 <= x0 or y1 <= y0:
        return 0.0
    return (x1 - x0) * (y1 - y0)


def _collisions(texts, patches, arrows, renderer):
    """Geometric overlap check on the drawn canvas (display coordinates)."""
    out = []
    tb = [(owner, t.get_text(), _bb(t, renderer)) for owner, t in texts]
    pb = [(owner, _bb(p, renderer)) for owner, p in patches]
    for i in range(len(tb)):
        for j in range(i + 1, len(tb)):
            if tb[i][0] == tb[j][0] or (tb[i][0] == "chrome" and tb[j][0] == "chrome"):
                continue
            ia = _inter(tb[i][2], tb[j][2])
            amin = min(_area(tb[i][2]), _area(tb[j][2]))
            if amin > 0 and ia > 0.30 * amin:
                out.append("TEXT-TEXT  %r x %r  (%r / %r)"
                           % (tb[i][0], tb[j][0], tb[i][1][:24], tb[j][1][:24]))
    for owner, txt, bb in tb:
        for powner, pbb in pb:
            if powner == owner:
                continue
            if _inter(bb, pbb) > 0.30 * _area(bb):
                out.append("TEXT-NODE  label %r of %s overlaps node %s"
                           % (txt[:24], owner, powner))
    for i in range(len(pb)):
        for j in range(i + 1, len(pb)):
            if pb[i][0] == pb[j][0]:
                continue
            ia = _inter(pb[i][1], pb[j][1])
            if ia > 0.10 * min(_area(pb[i][1]), _area(pb[j][1])):
                out.append("NODE-NODE  %s x %s" % (pb[i][0], pb[j][0]))
    # arrows through foreign labels / node interiors: sample the actual curve
    for a, b, p in arrows:
        try:
            verts = p.get_path().transformed(p.get_transform()).vertices
        except Exception:
            continue
        for powner, pbb in pb:
            if powner in (a, b):
                continue
            hits = sum(1 for vx, vy in verts
                       if pbb[0] + 2 <= vx <= pbb[2] - 2 and pbb[1] + 2 <= vy <= pbb[3] - 2)
            if hits >= 2:
                out.append("ARROW-NODE  link %s->%s passes through node %s" % (a, b, powner))
        for owner, txt, bb in tb:
            if owner in ("chrome", a, b):
                continue
            m = 2.0
            hit = any(bb[0] - m <= vx <= bb[2] + m and bb[1] - m <= vy <= bb[3] + m
                      for vx, vy in verts)
            if hit:
                out.append("ARROW-LABEL  link %s->%s crosses label of %s (%s)"
                           % (a, b, owner, txt[:24]))
    return out


def draw(manifest, out_path):
    g = Graph(manifest)
    cols = g.columns()
    col_kind = (["sym"] + ["premise"] + ["hidden"] * g.n_hidden + ["goal"])
    col_w = []
    for k in col_kind:
        col_w.append({"sym": 3.4, "premise": 3.6, "hidden": NODE_W + 0.9, "goal": 6.2}[k])

    # layout: y slots per column; circles hug their column edge so the mathtext
    # label has the whole column width to sit in
    SLOT = {"sym": 0.9, "premise": 1.15, "hidden": NODE_H + 0.65, "goal": 1.5}
    pos = {}
    x = 0.0
    col_x = []
    maxh = 0.0
    for col, kind, w in zip(cols, col_kind, col_w):
        span = len(col) * SLOT[kind]
        maxh = max(maxh, span)
        col_x.append(x + w / 2.0)
        if kind == "sym":
            cx = x + CIRCLE_R + 0.18
        elif kind == "goal":
            cx = x + w - (CIRCLE_R + 0.10) - 0.10
        else:
            cx = x + w / 2.0
        y = span / 2.0
        for nid in col:
            pos[nid] = (cx, y)
            y -= SLOT[kind]
        x += w
    # every column is centered about y = 0 (span/2 down to -span/2)
    top = maxh / 2.0 + 1.6
    bottom = -maxh / 2.0 - 2.3
    x_hi = x + 0.8
    y_hi = top + 1.5

    # figure size follows the data aspect exactly, so set_aspect("equal")
    # fills the figure instead of letterboxing it
    xr = x_hi + 0.8
    yr = (y_hi + 0.8) - bottom
    fig_w = min(20.0, max(14.0, yr * 1.05))
    fig_h = fig_w * yr / xr
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    ppu = fig_w * DPI / xr          # display pixels per layout unit

    texts, patches, arrows, fit = [], [], [], []
    rect_nodes = set()             # nodes whose own texts must stay inside their box

    # column headers
    names = [u"QM input symbols (ℏ=c=1)", "assumed premises"] + \
            ["derivation stage %d" % (i + 1) for i in range(g.n_hidden)] + \
            ["GR outputs"]
    for cx, name in zip(col_x, names):
        texts.append(("chrome", label_bg(ax.text(cx, top - 0.35, name, ha="center", va="top",
                                                 fontsize=9, fontweight="bold", color=INK))))

    # edges
    colidx = {nid: i for i, c in enumerate(cols) for nid in c}
    kinds_seen = set()
    for i, (a, b, kind) in enumerate(g.links):
        if a not in pos or b not in pos:
            continue
        ls, color, lw = EDGE_STYLE[kind]
        kinds_seen.add(kind)
        ax_, ay = pos[a]
        bx, by = pos[b]
        same_col = colidx.get(a) == colidx.get(b)
        if same_col:
            # side chain inside one stage: route on the left of the column
            ax_ = ax_ - (NODE_W / 2.0 - 0.15 if a in g.nodes else CIRCLE_R + 0.02)
            bx = bx - (NODE_W / 2.0 + 0.05 if b in g.nodes else CIRCLE_R + 0.02)
        else:
            # trim to node boundaries
            if a in g.circles or a in g.diamonds:
                ax_ += CIRCLE_R + 0.02
            elif a in g.goals:
                ax_ -= CIRCLE_R + 0.20
            else:
                ax_ += NODE_W / 2.0 - 0.15
            if b in g.circles or b in g.diamonds:
                bx -= CIRCLE_R + 0.02
            elif b in g.goals:
                bx -= CIRCLE_R + 0.20
            else:
                bx -= NODE_W / 2.0 + 0.05
        span = colidx.get(b, 0) - colidx.get(a, 0)
        spread = ((i % 5) - 2) * 0.05
        if same_col:
            rad = -0.5 if ay >= by else 0.5
        elif bx > ax_:
            # adjacent columns: gentle arc; skipping columns: arc harder so the
            # wire bends around the intermediate stage instead of through it
            rad = (0.07 + 0.12 * max(0, span - 1)) + spread
        else:
            rad = 0.35
        arrow = FancyArrowPatch((ax_, ay), (bx, by), arrowstyle="-|>",
                                mutation_scale=8, linestyle=ls, color=color,
                                linewidth=lw, alpha=0.75,
                                connectionstyle="arc3,rad=%.3f" % rad,
                                shrinkA=1, shrinkB=1)
        ax.add_patch(arrow)
        arrows.append((a, b, arrow))

    # nodes - every label is the node's own mathtext where the manifest has one
    states_seen = set()
    for nid, (cx, cy) in pos.items():
        spec = g.node_label(nid)
        if spec[0] == "circle":
            c = g.circles[nid]
            p = Circle((cx, cy), CIRCLE_R, facecolor="#e1e0d9", edgecolor=SEC, linewidth=0.9)
            ax.add_patch(p)
            patches.append((nid, p))
            extra = c["value"] or c["note"]
            t = label_bg(ax.text(cx + CIRCLE_R + 0.12, cy + (0.13 if extra else 0.0),
                                 c["math"] or c["label"], ha="left", va="center",
                                 fontsize=7.8, color=INK))
            texts.append((nid, t)); fit.append((t, 2.6 * ppu))
            if extra:
                t2 = label_bg(ax.text(cx + CIRCLE_R + 0.12, cy - 0.19, extra, ha="left",
                                      va="center", fontsize=5.2, color=MUTED))
                texts.append((nid, t2)); fit.append((t2, 2.6 * ppu))
            if nid in g.unused_symbols:
                texts.append((nid, label_bg(ax.text(cx - CIRCLE_R - 0.12, cy, "unused",
                                                    ha="right", va="center", fontsize=5.8,
                                                    color=MUTED, style="italic"))))
        elif spec[0] == "diamond":
            d = g.diamonds[nid]
            p = RegularPolygon((cx, cy), numVertices=4, radius=CIRCLE_R,
                               orientation=0.785398, facecolor="#f0efec",
                               edgecolor=SEC, linewidth=0.8)
            ax.add_patch(p)
            patches.append((nid, p))
            t = label_bg(ax.text(cx + CIRCLE_R + 0.10, cy + (0.12 if d["note"] else 0.0),
                                 d["math"] or d["label"], ha="left", va="center",
                                 fontsize=6.8, color=SEC))
            texts.append((nid, t)); fit.append((t, 2.9 * ppu))
            if d["note"]:
                t2 = label_bg(ax.text(cx + CIRCLE_R + 0.10, cy - 0.16, d["note"], ha="left",
                                      va="center", fontsize=5.6, color=MUTED))
                texts.append((nid, t2)); fit.append((t2, 2.9 * ppu))
        elif spec[0] == "goal":
            gd = g.goals[nid]
            blocked = gd["blocked"]
            p = Circle((cx, cy), CIRCLE_R + 0.10, facecolor=SURFACE,
                       edgecolor=BLOCK_COLOR if blocked else SEC,
                       linewidth=1.6 if blocked else 1.1, linestyle=(0, (3, 2)))
            ax.add_patch(p)
            patches.append((nid, p))
            tx = cx - (CIRCLE_R + 0.10) - 0.20
            wmax = (col_w[-1] - 1.3) * ppu
            t1 = label_bg(ax.text(tx, cy + 0.46, spec[1], ha="right", va="center",
                                  fontsize=5.8, color=SEC))
            texts.append((nid, t1)); fit.append((t1, wmax))
            if gd["math"]:
                t2 = label_bg(ax.text(tx, cy + 0.06, gd["math"], ha="right", va="center",
                                      fontsize=7.0, color=INK))
                texts.append((nid, t2)); fit.append((t2, wmax))
            if gd["label_name"]:
                t3 = label_bg(ax.text(tx, cy - 0.30, gd["label_name"], ha="right", va="center",
                                      fontsize=5.2, color=MUTED))
                texts.append((nid, t3)); fit.append((t3, wmax))
            if blocked:
                why = "; ".join(g.reason.get(nid, ["?"]))
                st = "\n".join(textwrap.wrap(one_line(why, 100), 44))
                t4 = label_bg(ax.text(tx, cy - 0.60, st, ha="right", va="center",
                                      fontsize=5.6, color=BLOCK_COLOR))
                texts.append((nid, t4)); fit.append((t4, wmax))
        else:
            _, title, _, tag = spec
            n = g.nodes[nid]
            st = n.get("state", "open-critical")
            fill, ink, compact, legend = STATE_STYLE.get(st, STATE_STYLE["open-critical"])
            states_seen.add(st)
            d = g.disp.get(nid) or {}
            blocked_vis = (nid in g.blocked) and not st.startswith("open")
            upg = (nid in g.upgrade) and not st.startswith("open")
            edge, els, elw = INK, "solid", 0.8
            if upg:
                edge, els, elw = UPGRADE_COLOR, (0, (2, 2)), 1.1
            if blocked_vis:
                edge, els, elw = BLOCK_COLOR, (0, (4, 2)), 1.4
            p = FancyBboxPatch((cx - NODE_W / 2.0, cy - NODE_H / 2.0), NODE_W, NODE_H,
                               boxstyle="round,pad=0.05,rounding_size=0.10",
                               facecolor=fill, edgecolor=edge, linestyle=els, linewidth=elw)
            ax.add_patch(p)
            patches.append((nid, p))
            rect_nodes.add(nid)
            texts.append((nid, ax.text(cx - NODE_W / 2.0 + 0.12, cy + NODE_H / 2.0 - 0.10,
                                       nid, ha="left", va="top", fontsize=6.4, family="monospace",
                                       fontweight="bold", color=ink)))
            if d.get("label"):
                texts.append((nid, ax.text(cx + NODE_W / 2.0 - 0.12, cy + NODE_H / 2.0 - 0.10,
                                           d["label"], ha="right", va="top", fontsize=5.4,
                                           color=ink, alpha=0.85)))
            rows = []
            if d.get("math"):
                rows.append((d["math"], 6.4))
            if not rows:
                rows.append((one_line(title, 34), 5.8))
            if d.get("math2"):
                rows.append((d["math2"], 6.2))
            if d.get("value"):
                rows.append((d["value"], 5.9))
            elif d.get("note"):
                rows.append((d["note"], 5.4))
            k = len(rows)
            for i, (s, fsz) in enumerate(rows):
                yy = 0.0 if k == 1 else 0.24 - i * 0.48 / (k - 1)
                t = ax.text(cx, cy + yy, s, ha="center", va="center", fontsize=fsz, color=ink)
                texts.append((nid, t)); fit.append((t, (NODE_W - 0.24) * ppu))
            tagline = compact
            if blocked_vis:
                tagline += "  +BLOCKED"
            elif upg:
                tagline += "  +open-input"
            texts.append((nid, ax.text(cx, cy - NODE_H / 2.0 + 0.10, tagline, ha="center",
                                       va="bottom", fontsize=5.7, color=ink, alpha=0.92)))

    # shrink any label wider than its allotted band, before measuring collisions
    fig.canvas.draw()
    R0 = fig.canvas.get_renderer()
    for t, wpx in fit:
        _fit_text(t, wpx, R0)

    # title
    title = manifest.get("title", "NAMCG mission graph")
    gen = manifest.get("generated", "")
    active = manifest.get("active_label", "")
    bits = [title]
    if active:
        bits.append("programme: %s" % active)
    if gen:
        bits.append("generated %s" % gen)
    texts.append(("chrome", ax.text(-0.8, y_hi + 0.35, "   |   ".join(str(b) for b in bits),
                                    ha="left", va="top", fontsize=11, fontweight="bold",
                                    color=INK)))

    counts = {}
    for nid in g.deriv:
        st = g.nodes[nid].get("state", "?")
        counts[st] = counts.get(st, 0) + 1
    counts_txt = ", ".join("%s: %d" % (s, c) for s, c in sorted(counts.items()))
    lay_bl = [n for n in g.deriv if n in g.blocked and
              not str(g.nodes[n].get("state", "")).startswith("open")]
    goals_bl = [n for n in g.goals if g.goals[n]["blocked"]]
    up_l = [n for n in g.deriv if n in g.upgrade
            and not str(g.nodes[n].get("state", "")).startswith("open")]
    texts.append(("chrome", ax.text(-0.4, bottom + 2.05,
                                    "derivation nodes %d   input symbols %d   premises %d   "
                                    "edges %d   gaps %d   GR outputs %d   [%s]"
                                    % (len(g.deriv), len(g.circles), len(g.diamonds),
                                       len(g.links), len(g.gaps), len(g.goals), counts_txt),
                                    ha="left", va="top", fontsize=7.2, color=MUTED)))
    texts.append(("chrome", ax.text(-0.4, bottom + 1.84,
                                    "blocked (gap or unmet upstream): layers %d %s   outputs %d/%d"
                                    "   conditional-only: %s"
                                    % (len(lay_bl), ",".join(lay_bl) or "-", len(goals_bl),
                                       len(g.goals), ",".join(up_l) or "-"),
                                    ha="left", va="top", fontsize=7.0, color=BLOCK_COLOR)))
    for i, gp in enumerate((manifest.get("gaps") or [])[:6]):
        texts.append(("chrome", ax.text(-0.4, bottom + 1.56 - i * 0.28,
                                        "GAP  %s   blocks %s%s" % (
                                            gp.get("symbol", "?"),
                                            ",".join(gp.get("blocks", []) or ["?"]),
                                            ("   - " + gp.get("note")) if gp.get("note") else ""),
                                        ha="left", va="top", fontsize=6.4, color="#d03b3b")))
    vals = ["%s: %s  [%s]" % (nid, d["value"], d.get("vsrc", "no src"))
            for nid, d in sorted(g.disp.items()) if d.get("value")]
    if vals:
        texts.append(("chrome", ax.text(-0.4, bottom + 1.56 - 6 * 0.28 - 0.16,
                                        "stated values (manuscript): " + "   |   ".join(vals),
                                        ha="left", va="top", fontsize=6.2, color=SEC)))

    # legend
    handles = []
    for st in [s for s in STATE_STYLE if s in states_seen]:
        fill, ink, compact, legend = STATE_STYLE[st]
        handles.append(Line2D([0], [0], marker="s", linestyle="", markersize=9,
                              markerfacecolor=fill, markeredgecolor=INK, label=legend))
    handles.append(Line2D([0], [0], marker="o", linestyle="", markersize=9,
                          markerfacecolor="#e1e0d9", markeredgecolor=SEC,
                          label="QM input symbol"))
    handles.append(Line2D([0], [0], marker="D", linestyle="", markersize=7,
                          markerfacecolor="#f0efec", markeredgecolor=SEC,
                          label="assumed premise"))
    handles.append(Line2D([0], [0], marker="o", linestyle="", markersize=10,
                          markerfacecolor=SURFACE, markeredgecolor=SEC,
                          label="GR output (dashed = not met; red = gap-blocked)"))
    if lay_bl or goals_bl:
        handles.append(Line2D([0], [0], linestyle=(0, (4, 2)), color=BLOCK_COLOR,
                              linewidth=1.5, label="BLOCKED: gap symbol or unmet open input"))
    if up_l:
        handles.append(Line2D([0], [0], linestyle=(0, (2, 2)), color=UPGRADE_COLOR,
                              linewidth=1.4, label="+open-input: only path runs through an open node"))
    for kind in [k for k in EDGE_STYLE if k in kinds_seen]:
        ls, color, lw = EDGE_STYLE[kind]
        handles.append(Line2D([0], [0], linestyle=ls, color=color, linewidth=lw,
                              label="link: %s" % kind))
    ax.legend(handles=handles, loc="lower right", fontsize=6.8, framealpha=1.0,
              facecolor=SURFACE, edgecolor=GRID)

    ax.set_xlim(-0.8, x_hi)
    ax.set_ylim(bottom, y_hi + 0.8)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(out_path, dpi=DPI, facecolor=SURFACE)
    R = fig.canvas.get_renderer()
    collisions = _collisions(texts, patches, arrows, R) + _overflow(texts, patches, rect_nodes, R)
    plt.close(fig)
    return g.warnings, len(g.deriv), len(g.links), len(g.gaps), collisions


def main():
    manifest_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MANIFEST
    out_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT
    if not os.path.exists(manifest_path):
        sys.stderr.write("manifest not found: %s\n" % manifest_path)
        return 2
    with open(manifest_path, "r", encoding="utf-8") as fh:
        manifest = yaml.safe_load(fh)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    warnings, n_nodes, n_edges, n_gaps, collisions = draw(manifest, out_path)
    for w in warnings:
        sys.stderr.write("WARNING: %s\n" % w)
    hard = [c for c in collisions if not c.startswith("ARROW-LABEL")]
    soft = [c for c in collisions if c.startswith("ARROW-LABEL")]
    for c in collisions:
        sys.stderr.write("COLLISION: %s\n" % c)
    print("RENDERED %s | NODES %d | EDGES %d | GAPS %d | WARNINGS %d | COLLISIONS %d "
          "(hard %d, arrow-bbox %d)"
          % (out_path, n_nodes, n_edges, n_gaps, len(warnings), len(collisions),
             len(hard), len(soft)))
    return 0 if not warnings and not hard else 1


if __name__ == "__main__":
    sys.exit(main())
