#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the NAMCG attack plan (reports/graph/attack-plan.yaml) to a PNG.

Layout: one card per OPEN problem, placed in the column of its attack WAVE
(wave = 1 + max(dep waves) - i.e. the first wave at which every prerequisite
is already attacked), and one card per blocked GR goal in a far-right column.
Each problem card lists the manuscript's own stated missing steps as
obligations, each with its source citation. Wires run problem -> problem
(unlock edges) and problem -> goal. A per-card impact count ("-> n prob / m
goals") is the transitive closure over the unlock graph, computed by this
renderer. Everything strategy-related (waves, order, impact) is advice
derived from the manifest; statuses are mirrored verbatim and never changed.

Geometry self-check after drawing: TEXT-TEXT, TEXT-OWNERSHIP, WIRE-TEXT are
hard; WIRE-BEHIND-CARD is soft (wire hidden behind a foreign card).
Usage: python scripts/render_attack_graph.py [yaml] [png]
"""
import sys
import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow

SURFACE = "#fcfcfb"; INK = "#0b0b0b"; SEC = "#52514e"; MUTED = "#898781"
GRID = "#c3c2b7"; CRIT = "#d03b3b"; OPT = "#ec835a"; BLUE = "#2a78d6"; DPI = 200
STATE_COL = {"open-critical": CRIT, "open-optional": OPT}
TAG = {"open-critical": "CRITICAL", "open-optional": "OPTIONAL"}

CARD_W = 4.7; GOAL_W = 4.4; GAP = 1.7; LH = 0.30


def load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def compute_waves(problems):
    wave = {}
    def w(pid):
        if pid in wave:
            return wave[pid]
        p = next(q for q in problems if q["id"] == pid)
        deps = p.get("depends_on") or []
        wave[pid] = 1 if not deps else 1 + max(w(d) for d in deps)
        return wave[pid]
    for p in problems:
        w(p["id"])
    return wave


def downstream(pid, problems):
    seen, stack = set(), [pid]
    while stack:
        cur = stack.pop()
        for q in problems:
            if cur in (q.get("depends_on") or []) and q["id"] not in seen:
                seen.add(q["id"]); stack.append(q["id"])
    return seen


def main():
    ypath = sys.argv[1] if len(sys.argv) > 1 else "reports/graph/attack-plan.yaml"
    ppath = sys.argv[2] if len(sys.argv) > 2 else "reports/graph/attack-plan.png"
    plan = load(ypath)
    problems = plan["problems"]; goals = plan["goals"]
    wave = compute_waves(problems)
    nw = max(wave.values())
    imp = {}
    for p in problems:
        ds = downstream(p["id"], problems)
        gi = sum(1 for g in goals if set(g["needs"]) & (ds | {p["id"]}))
        imp[p["id"]] = (len(ds), gi)
    goal_wave = {g["id"]: 1 + max(wave[q] for q in g["needs"]) for g in goals}

    # ---------------- layout ----------------
    col_x = [c * (CARD_W + GAP) for c in range(nw)]
    goal_x = nw * (CARD_W + GAP)
    Y_TOP = 0.0

    cards = []  # each: dict(kind,id,x0,x1,yt,yb,col,owner texts appended later)
    by_wave = {}
    for p in problems:
        by_wave.setdefault(wave[p["id"]], []).append(p)
    order_crit = 0  # manifest order preserved, critical before optional
    for c in range(1, nw + 1):
        grp = sorted(by_wave[c], key=lambda p: (0 if p["state"] == "open-critical" else 1,))
        y = Y_TOP
        for p in grp:
            n = len(p["obligations"])
            h = 0.92 + n * LH
            cards.append(dict(kind="prob", id=p["id"], x0=col_x[c - 1], x1=col_x[c - 1] + CARD_W,
                              yt=y, yb=y - h, col=c, p=p, h=h))
            y -= h + 0.8
    y = Y_TOP
    for g in goals:
        h = 0.92 + 2 * LH
        cards.append(dict(kind="goal", id=g["id"], x0=goal_x, x1=goal_x + GOAL_W,
                          yt=y, yb=y - h, col=nw + 1, g=g, h=h))
        y -= h + 0.8
    depth = max(-(c["yb"]) for c in cards)

    # ---------------- canvas ----------------
    xr = (-0.5, goal_x + GOAL_W + 0.5)
    yr = (-depth - 2.6, Y_TOP + 2.9)
    fig_w = 22.0
    fig_h = fig_w * (yr[1] - yr[0]) / (xr[1] - xr[0])
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=DPI)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.patch.set_facecolor(SURFACE); ax.set_facecolor(SURFACE)
    ax.set_xlim(*xr); ax.set_ylim(*yr); ax.axis("off")
    texts = []  # (text_obj, owner_card_id)

    def T(x, y, s, fs, col, ha="left", wt="normal", owner=None):
        t = ax.text(x, y, s, fontsize=fs, color=col, ha=ha, va="center",
                    fontweight=wt, zorder=4)
        texts.append((t, owner))
        return t

    # header
    T(xr[0] + 0.35, Y_TOP + 2.35, plan["title"], 10.5, INK, wt="bold")
    T(xr[0] + 0.35, Y_TOP + 1.85,
      "open problems decomposed into the manuscript's own stated missing steps; wave = first wave at which all "
      "prerequisites are attacked;  impact = transitive downstream problems / blocked goals",
      6.6, SEC)
    for c in range(1, nw + 1):
        lbl = u"WAVE %d — %s" % (c, "start now, run in parallel" if c == 1 else
                                 "unlocked by waves < %d" % c)
        T(col_x[c - 1], Y_TOP + 1.25, lbl, 7.6, SEC, wt="bold")
    T(goal_x, Y_TOP + 1.25, u"GR GOALS — still blocked; each clears once its listed problems fall",
      7.6, CRIT, wt="bold")
    # legend (header right)
    lx = goal_x - 6.6
    ax.add_patch(Rectangle((lx, Y_TOP + 2.22), 0.14, 0.30, color=CRIT, zorder=3))
    T(lx + 0.24, Y_TOP + 2.37, "open, critical path", 5.6, SEC, owner="#legend")
    ax.add_patch(Rectangle((lx + 2.5, Y_TOP + 2.22), 0.14, 0.30, color=OPT, zorder=3))
    T(lx + 2.74, Y_TOP + 2.37, "open, optional", 5.6, SEC, owner="#legend")

    # cards
    for c in cards:
        if c["kind"] == "prob":
            p = c["p"]
            ax.add_patch(Rectangle((c["x0"], c["yb"]), c["x1"] - c["x0"], c["h"],
                                   facecolor=SURFACE, edgecolor=INK, lw=0.8, zorder=3))
            ax.add_patch(Rectangle((c["x0"], c["yb"]), 0.10, c["h"],
                                   facecolor=STATE_COL[p["state"]], edgecolor="none", zorder=4))
            np_, ng = imp[p["id"]]
            T(c["x0"] + 0.24, c["yt"] - 0.26, p["id"], 6.6, INK, wt="bold", owner=c["id"])
            T(c["x1"] - 0.16, c["yt"] - 0.26, TAG[p["state"]] + u"  ·  → %d prob / %d goals" % (np_, ng),
              5.0, STATE_COL[p["state"]], ha="right", owner=c["id"])
            yy = c["yt"] - 0.56
            for ob in p["obligations"]:
                T(c["x0"] + 0.24, yy, u"%s  %s" % (ob["id"], ob["task"]), 5.4, INK, owner=c["id"])
                yy -= LH
            srcs = sorted(set(ob["src"] for ob in p["obligations"]))
            T(c["x0"] + 0.24, c["yb"] + 0.14, u"obligations sourced: " + u"; ".join(srcs),
              4.6, MUTED, owner=c["id"])
        else:
            g = c["g"]
            ax.add_patch(Rectangle((c["x0"], c["yb"]), c["x1"] - c["x0"], c["h"],
                                   facecolor=SURFACE, edgecolor=CRIT, lw=1.2,
                                   linestyle=(0, (4, 2)), zorder=3))
            T(c["x0"] + 0.22, c["yt"] - 0.26, g["id"], 6.4, CRIT, wt="bold", owner=c["id"])
            T(c["x1"] - 0.18, c["yt"] - 0.26, u"opens after wave %d" % goal_wave[g["id"]],
              5.0, SEC, ha="right", owner=c["id"])
            T(c["x0"] + 0.22, c["yt"] - 0.56, g["title"], 5.4, INK, owner=c["id"])
            T(c["x0"] + 0.22, c["yb"] + 0.20, u"needs: " + u", ".join(g["needs"]), 4.8, MUTED, owner=c["id"])

    # ---------------- wires ----------------
    card_by_id = {c["id"]: c for c in cards}
    wires = []  # (polyline, src_id, tgt_id, kind)

    def route(sc, tc):
        cs, ct = sc["col"], tc["col"]
        mids = [c for c in cards if cs < c["col"] < ct and c["kind"] == "prob"]
        x_lo = sc["x1"] + 0.55; x_hi = tc["x0"] - 0.55
        ys = [Y_TOP - 0.15 * i for i in range(int((depth + 0.4) / 0.15) + 1)]
        y_exit = (sc["yt"] + sc["yb"]) / 2.0; y_entry = (tc["yt"] + tc["yb"]) / 2.0
        def blocked_at(y):
            return [c for c in mids if c["yb"] - 0.09 < y < c["yt"] + 0.09]
        cands = [(len(blocked_at(y)), abs(y - y_exit) + abs(y - y_entry), y) for y in ys]
        _, _, y_mid = min(cands)
        xg1 = sc["x1"] + 0.55 + 0.22 * (len(wires) % 4)
        xg2 = tc["x0"] - 0.62
        pts = [(sc["x1"], y_exit), (xg1, y_exit), (xg1, y_mid), (xg2, y_mid), (xg2, y_entry), (tc["x0"], y_entry)]
        return pts

    edges = []
    for p in problems:
        for d in (p.get("depends_on") or []):
            edges.append((d, p["id"], "unlock"))
    for g in goals:
        for q in g["needs"]:
            edges.append((q, g["id"], "goal"))
    behind = 0
    for s, t, kind in edges:
        sc, tc = card_by_id[s], card_by_id[t]
        pts = route(sc, tc)
        wires.append((pts, s, t, kind))
        col = INK if kind == "unlock" else MUTED
        lw = 1.15 if kind == "unlock" else 0.75
        al = 1.0 if kind == "unlock" else 0.8
        from matplotlib.lines import Line2D
        ax.add_line(Line2D([p[0] for p in pts], [p[1] for p in pts],
                           linewidth=lw, color=col, alpha=al, zorder=2,
                           solid_joinstyle="round"))
        ax.add_patch(FancyArrow(pts[-2][0], pts[-2][1], pts[-1][0] - pts[-2][0] - 0.02, 0.0,
                                width=0.0, head_width=0.10 if kind == "unlock" else 0.08,
                                head_length=0.10 if kind == "unlock" else 0.08,
                                length_includes_head=True, facecolor=col, edgecolor="none",
                                alpha=al, zorder=2))

    # ---------------- footer ----------------
    fy = -depth - 1.0
    wlists = []
    for c in range(1, nw + 1):
        ids = ", ".join(sorted([p["id"] for p in by_wave[c]]))
        wlists.append(u"W%d: %s" % (c, ids))
    order = sorted([p["id"] for p in problems],
                   key=lambda pid: (wave[pid], -imp[pid][1], -imp[pid][0], pid))
    T(xr[0] + 0.35, fy, u"waves — " + u"   |   ".join(wlists), 6.2, SEC, owner="#foot")
    T(xr[0] + 0.35, fy - 0.42, u"advisory attack order (wave, then impact): " + u", ".join(order),
      6.2, INK, wt="bold", owner="#foot")
    T(xr[0] + 0.35, fy - 0.84,
      u"strategy computed from reports/graph/mission-graph.yaml - ordering is advice, not manuscript content; "
      u"statuses mirrored verbatim from Appendix H, none changed; conditional items already in the book "
      u"(usable as inputs, still conditional): " + u", ".join(plan["conditional_suppliers"]),
      5.4, MUTED, owner="#foot")

    fig.canvas.draw()
    R = fig.canvas.get_renderer()

    # ---------------- self-check ----------------
    hard, soft = [], []
    tb = [(t, owner, t.get_window_extent(R)) for t, owner in texts]
    for i in range(len(tb)):
        for j in range(i + 1, len(tb)):
            if tb[i][1] is not None and tb[j][1] is not None and tb[i][1] != tb[j][1]:
                continue
            a, b = tb[i][2], tb[j][2]
            ix = max(0, min(a.x1, b.x1) - max(a.x0, b.x0))
            iy = max(0, min(a.y1, b.y1) - max(a.y0, b.y0))
            if ix * iy > 0.30 * min(a.width * a.height, b.width * b.height):
                hard.append(u"TEXT-TEXT %r / %r" % (tb[i][0].get_text()[:26], tb[j][0].get_text()[:26]))
    ppu = fig_w * DPI / (xr[1] - xr[0])
    for t, owner, bb in tb:
        if owner in card_by_id:
            c = card_by_id[owner]
            cx, cy = (bb.x0 + bb.x1) / 2.0, (bb.y0 + bb.y1) / 2.0
            # convert card box to px
            def px(x, y):
                fx = (x - xr[0]) / (xr[1] - xr[0]) * fig_w * DPI
                fy2 = (y - yr[0]) / (yr[1] - yr[0]) * fig_h * DPI
                return fx, fy2
            x0p, ybp = px(c["x0"], c["yb"]); x1p, ytp = px(c["x1"], c["yt"])
            if not (x0p <= cx <= x1p and ybp <= cy <= ytp):
                hard.append(u"TEXT-OUTSIDE %r escapes card %s" % (t.get_text()[:26], owner))
            if (bb.x1 - bb.x0) > (c["x1"] - c["x0"] - 0.30) * ppu + 1:
                hard.append(u"TEXT-WIDE %r wider than card %s" % (t.get_text()[:26], owner))
    for pts, s, t, kind in wires:
        for k in range(len(pts) - 1):
            (x1_, y1_), (x2_, y2_) = pts[k], pts[k + 1]
            for m in range(26):
                f = m / 25.0
                wx = x1_ + (x2_ - x1_) * f; wy = y1_ + (y2_ - y1_) * f
                fx, fy2 = (wx - xr[0]) / (xr[1] - xr[0]) * fig_w * DPI, \
                          (wy - yr[0]) / (yr[1] - yr[0]) * fig_h * DPI
                for tt, owner, bb in tb:
                    if bb.x0 + 1 < fx < bb.x1 - 1 and bb.y0 + 1 < fy2 < bb.y1 - 1:
                        hard.append(u"WIRE-TEXT wire %s->%s hits %r" % (s, t, tt.get_text()[:22]))
                        break
                for c in cards:
                    if c["id"] in (s, t) or c["kind"] != "prob":
                        continue
                    x0p, ybp = ((c["x0"] - xr[0]) / (xr[1] - xr[0]) * fig_w * DPI,
                                (c["yb"] - yr[0]) / (yr[1] - yr[0]) * fig_h * DPI)
                    x1p, ytp = ((c["x1"] - xr[0]) / (xr[1] - xr[0]) * fig_w * DPI,
                                (c["yt"] - yr[0]) / (yr[1] - yr[0]) * fig_h * DPI)
                    if x0p + 2 < fx < x1p - 2 and ybp + 2 < fy2 < ytp - 2:
                        soft.append(u"WIRE-BEHIND wire %s->%s behind card %s" % (s, t, c["id"]))
                        break
    # dedupe soft (samples along one wire hit the same card many times)
    seen = set(); softd = []
    for m in soft:
        if m not in seen:
            seen.add(m); softd.append(m)
    for m in hard[:20]:
        sys.stderr.write(m + "\n")
    fig.savefig(ppath, facecolor=SURFACE)
    print("RENDERED %s | CARDS %d (prob %d, goal %d) | WIRES %d | WAVES %d | WARNINGS %d | "
          "COLLISIONS %d (hard %d, wire-behind %d)" %
          (ppath, len(cards), len(problems), len(goals), len(wires), nw,
           0, len(hard) + len(softd), len(hard), len(softd)))
    for m in softd:
        sys.stderr.write(m + "\n")


if __name__ == "__main__":
    main()
