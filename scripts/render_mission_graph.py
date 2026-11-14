#!/usr/bin/env python
"""Render reports/graph/mission-graph.yaml (schema v2) to a PNG.

Neural-network style view: QM symbols_out as circles (left), premises as diamonds,
namcg+ir nodes auto-layered by longest path, gr goals at the right. Blocked
propagation: a node is BLOCKED if named in gaps, a gap symbol is in its symbols_in,
or a required edge comes from an open/blocked node (fixed point); it is +open-input
if only conditional edges come from open/blocked nodes. supports edges never block.
Usage: render_mission_graph.py MANIFEST.yaml OUT.png
"""
import sys, textwrap
import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon
from matplotlib import textpath  # noqa: F401

OPEN_STATES = {"open-critical", "open-optional", "goal"}
COL = {"foundation": "#dfe8f5", "open-critical": "#fde2e2", "open-optional": "#fff2cc",
       "closed-conditionally": "#e2f2e2", "derived": "#b8e6b8", "goal": "#eeeeee"}
KIND = {"required": ("#222222", "-"), "conditional": ("#b36b00", "--"),
        "supports": ("#7a7a7a", ":"), "gap": ("#cc0000", "-.")}
BW, BH = 3.0, 1.55
XS, YS = 4.1, 2.05


def main(inp, out):
    m = yaml.safe_load(open(inp, encoding="utf-8"))
    nodes = {n["id"]: n for n in m["nodes"]}
    edges = m["edges"]
    gaps = m.get("gaps", [])
    gapsyms = {g["symbol"]: g for g in gaps}
    rm = m.get("render_math", {})
    disp = rm.get("displays", {})

    # ---- blocking propagation
    blocked = {}
    for g in gaps:
        for b in g["blocks"]:
            blocked.setdefault(b, []).append("gap: " + g["symbol"])
    for n in nodes.values():
        for s in n["symbols_in"]:
            if s in gapsyms:
                blocked.setdefault(n["id"], [])
                if "gap: " + s not in blocked[n["id"]]:
                    blocked[n["id"]].append("gap: " + s)
    openinput = {}
    ch = True
    while ch:
        ch = False
        for e in edges:
            if e["kind"] not in ("required", "conditional"):
                continue
            f, t = nodes[e["from"]], nodes[e["to"]]
            if t["layer"] == "qm" or f["layer"] == "qm":
                continue
            src_open = f["state"] in OPEN_STATES or f["id"] in blocked
            if not src_open or t["state"] == "foundation":
                continue
            if e["kind"] == "required":
                tag = "upstream " + f["id"]
                if tag not in blocked.setdefault(t["id"], []):
                    blocked[t["id"]].append(tag)
                    ch = True
            else:
                if t["id"] not in blocked and f["id"] not in openinput.get(t["id"], []):
                    openinput.setdefault(t["id"], []).append(f["id"])
    # ---- layering of namcg + ir
    mid = [n for n in nodes.values() if n["layer"] in ("namcg", "ir")]
    midids = {n["id"] for n in mid}
    layer = {i: 0 for i in midids}
    for _ in range(len(midids) + 2):
        for e in edges:
            if e["from"] in midids and e["to"] in midids:
                layer[e["to"]] = max(layer[e["to"]], layer[e["from"]] + 1)
    # terminal compaction: nodes with no outgoing mid-edge but not at max stay put
    gr = [n for n in nodes.values() if n["layer"] == "gr"]
    nmid = max(layer.values()) + 1
    cols = {}
    for i, l in layer.items():
        cols.setdefault(l + 2, []).append(i)
    gritems = [n["id"] for n in gr if n["id"] != "gr.complete"]
    cols[nmid + 2] = gritems
    cols[nmid + 3] = ["gr.complete"]
    # barycentre-free ordering: keep manifest order, then sort by mean predecessor row
    order = {n["id"]: k for k, n in enumerate(m["nodes"])}
    pos = {}
    for c in sorted(cols):
        ids = sorted(cols[c], key=lambda i: order[i])
        if c > 2:
            def bary(i):
                ys = [pos[e["from"]][1] for e in edges if e["to"] == i and e["from"] in pos]
                return sum(ys) / len(ys) if ys else 0
            ids.sort(key=lambda i: (bary(i), order[i]))
        for r, i in enumerate(ids):
            pos[i] = (c * XS, -r * YS)
    # centre columns vertically
    maxr = max(len(v) for v in cols.values())
    for c, ids in cols.items():
        off = -((maxr - len(ids)) // 2) * YS
        for i in ids:
            pos[i] = (pos[i][0], pos[i][1] + off)
    # qm circles
    qsyms = []
    for n in m["nodes"]:
        if n["layer"] == "qm":
            qsyms += [(s, n["id"]) for s in n["symbols_out"]]
    for k, (s, _) in enumerate(qsyms):
        pos["sym:" + s] = (0, -k * 1.6 - 1.0)
    prem = [i for i in m["inputs"]]
    for k, i in enumerate(prem):
        pos["pre:" + i["symbol"]] = (XS, -k * 1.25)

    fig_w = (nmid + 4) * XS * 0.62 + 4
    fig_h = max(maxr * YS, len(prem) * 1.25) * 0.62 + 4
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=110)
    ax.set_aspect("auto")
    warns = {"hard": 0, "soft": 0}
    rects = {}
    for i in midids | {n["id"] for n in gr}:
        x, y = pos[i]
        rects[i] = (x - BW / 2, y - BH / 2, x + BW / 2, y + BH / 2)

    def seg_hits(p, q, r):
        x0, y0, x1, y1 = r
        n = 40
        for k in range(1, n):
            t = k / n
            x = p[0] + (q[0] - p[0]) * t
            y = p[1] + (q[1] - p[1]) * t
            if x0 + .05 < x < x1 - .05 and y0 + .05 < y < y1 - .05:
                return True
        return False

    def anchor(i, other):
        x, y = pos[i]
        ox, oy = pos[other]
        if i in rects:
            return (x + BW / 2, y) if ox > x else (x - BW / 2, y)
        return (x + 0.45, y) if ox > x else (x - 0.45, y)

    lane_use = {}

    def wire(a, b, kind, label=None, lw=1.3):
        pa, pb = anchor(a, b), anchor(b, a)
        c, ls = KIND[kind]
        ca, cb = round(pos[a][0] / XS), round(pos[b][0] / XS)
        pts = [pa, pb]
        if cb - ca > 1:
            ym = (pa[1] + pb[1]) / 2
            k = round(-ym / YS - 0.5)
            lane = -(k + 0.5) * YS
            n = lane_use.get(round(lane, 2), 0)
            lane_use[round(lane, 2)] = n + 1
            lane += (n % 5 - 2) * 0.07
            gx1 = pa[0] + 0.3 + (n % 4) * 0.12
            gx2 = pb[0] - 0.3 - (n % 4) * 0.12
            pts = [pa, (gx1, pa[1]), (gx1, lane), (gx2, lane), (gx2, pb[1]), pb]
        for u, v in zip(pts[:-2], pts[1:-1]):
            ax.plot([u[0], v[0]], [u[1], v[1]], color=c, ls=ls, lw=lw, zorder=1)
        ax.annotate("", xy=pts[-1], xytext=pts[-2], zorder=1,
                    arrowprops=dict(arrowstyle="-|>", color=c, ls=ls, lw=lw, shrinkA=0, shrinkB=0))
        for u, v in zip(pts[:-1], pts[1:]):
            for j, r in rects.items():
                if j not in (a, b) and seg_hits(u, v, r):
                    warns["hard"] += 1
                    print("WARN wire-through-node", a, "->", b, "via", j)

    # wires
    for e in edges:
        f, t = e["from"], e["to"]
        if nodes[f]["layer"] == "qm":
            for s in e["symbols"]:
                wire("sym:" + s, t, e["kind"])
        else:
            wire(f, t, e["kind"])
    used = {}
    for i in prem:
        for u in i["used_by"]:
            used.setdefault(u, []).append(i["symbol"])
    for g in gaps:
        for b in g["blocks"]:
            x, y = pos[b]
            ax.text(x - BW / 2 - 0.1, y + BH / 2 + 0.12, "GAP: " + g["symbol"], color="#cc0000",
                    fontsize=6, ha="left", va="bottom", zorder=6)

    # circles
    for s, _ in qsyms:
        x, y = pos["sym:" + s]
        ax.add_patch(Circle((x, y), 0.45, fc=COL["foundation"], ec="#333", zorder=3))
        sm = rm.get("symbols", {}).get(s, {})
        ax.text(x, y, sm.get("math", s), ha="center", va="center", fontsize=11, zorder=4)
        ax.text(x, y - 0.62, "qm input", ha="center", va="top", fontsize=6, zorder=4)
    # diamonds
    for i in prem:
        x, y = pos["pre:" + i["symbol"]]
        ax.add_patch(Polygon([(x - 0.55, y), (x, y + 0.5), (x + 0.55, y), (x, y - 0.5)],
                             fc="#f3e5f5", ec="#6a1b9a", zorder=3))
        pm = rm.get("premises", {}).get(i["symbol"], {})
        ax.text(x + 0.62, y + 0.1, i["symbol"], fontsize=6, va="bottom", zorder=4)
        ax.text(x + 0.62, y - 0.08, pm.get("math", pm.get("note", i["kind"])), fontsize=6.5, va="top", zorder=4)
    # nodes
    for i in midids | {n["id"] for n in gr}:
        n = nodes[i]
        x0, y0, x1, y1 = rects[i]
        bl = i in blocked
        oi = i in openinput
        ec = "#cc0000" if bl else ("#e69500" if oi else "#333333")
        ax.add_patch(FancyBboxPatch((x0, y0), BW, BH, boxstyle="round,pad=0.02,rounding_size=0.1",
                                    fc=COL[n["state"]], ec=ec, lw=2.2 if (bl or oi) else 1.0,
                                    ls="--" if bl else "-", zorder=3))
        d = disp.get(i, {})
        tag = n["state"].upper() + (" | BLOCKED" if bl else (" | +open-input" if oi else ""))
        ax.text(x0 + 0.08, y1 - 0.06, tag, fontsize=5.8, va="top", color="#8b0000" if bl else "#333", zorder=4)
        ax.text(x0 + 0.08, y1 - 0.25, "\n".join(textwrap.wrap(n["title"], 38)[:3]), fontsize=6.3, va="top",
                weight="bold", zorder=4)
        t = ax.text((x0 + x1) / 2, y0 + BH * 0.42, d.get("math", ""), fontsize=8, ha="center", va="center", zorder=4)
        ax.text(x1 - 0.06, y0 + 0.30, d.get("label", ""), fontsize=5.5, ha="right", va="bottom", color="#1a237e", zorder=4)
        if i in used:
            ax.text(x0 + 0.08, y0 + 0.40, "uses: " + textwrap.shorten(", ".join(used[i]), 52), fontsize=5,
                    va="bottom", color="#6a1b9a", zorder=4)
        if d.get("note"):
            ax.text(x0 + 0.08, y0 + 0.2, d["note"], fontsize=5.3, va="bottom", color="#555", zorder=4)
        if bl:
            why = "; ".join(blocked[i])
            ax.text(x0 + 0.08, y0 + 0.04, "BLOCKED: " + textwrap.shorten(why, 62), fontsize=5, va="bottom",
                    color="#cc0000", zorder=4)
        fig.canvas.draw()
        bb = t.get_window_extent().transformed(ax.transData.inverted())
        if bb.width > BW - 0.1 or bb.height > BH * 0.6:
            warns["hard"] += 1
            print("WARN BOX-OVERFLOW", i)

    # column headers
    hd = {0: "QM inputs", 1: "premises (inputs)"}
    for c in range(2, nmid + 2):
        hd[c] = "derivation column %d" % (c - 1)
    hd[nmid + 2] = "GR criterion items"
    hd[nmid + 3] = "final label"
    ytop = max(p[1] for p in pos.values()) + 1.6
    for c, t in hd.items():
        ax.text(c * XS, ytop, t, ha="center", fontsize=8, weight="bold", color="#444")
    ax.set_xlim(-1.5, (nmid + 3) * XS + BW / 2 + 0.5)
    ax.set_ylim(min(p[1] for p in pos.values()) - 2.0, ytop + 0.6)
    ax.axis("off")
    nopen = sum(1 for n in m["nodes"] if n["state"].startswith("open"))
    ax.set_title("%s  (label: %s; %d nodes, %d open, %d gaps, %d blocked)" %
                 (m["title"], m["active_label"], len(nodes), nopen, len(gaps), len(blocked)), fontsize=11)
    leg = ("Legend: red dashed border = BLOCKED (gap or required open/blocked upstream); amber = +open-input; "
           "solid = required, dashed amber = conditional, dotted = supports (never blocks), diamonds = premises, listed in each node as 'uses:'. "
           "No numerical values are drawn (manuscript states none for these symbols).")
    fig.text(0.01, 0.005, leg, fontsize=6.5)
    fig.savefig(out, bbox_inches="tight")
    print("RENDERED %s NODES %d EDGES %d BLOCKED %d WARNINGS %d (hard %d, soft %d)" %
          (out, len(nodes), len(edges), len(blocked), warns["hard"] + warns["soft"], warns["hard"], warns["soft"]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
