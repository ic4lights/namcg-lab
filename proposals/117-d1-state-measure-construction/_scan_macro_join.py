# _scan_macro_join.py -- temporary audit: find absorbed/suspect macro tokens in payload
import re
line = open("insert-d1-state-measure.tex", encoding="ascii").read()
tokens = sorted(set(re.findall(r"\\([A-Za-z]+)", line)))
known = {
    "emph", "eqref", "ref", "label", "cite", "mathrm", "mathcal", "mathbb",
    "mathbf", "operatorname", "propto", "le", "ge", "in", "to", "infty",
    "det", "min", "sup", "int", "prod", "sum", "lvert", "rvert", "lVert",
    "rVert", "phi", "Phi", "mu", "beta", "lambda", "sigma", "alpha", "eta",
    "omega", "Omega", "epsilon", "varepsilon", "rho", "nu", "xi", "pi",
    "hat", "bar", "tilde", "vec", "mathit", "boldsymbol", "bigl", "bigr",
    "Bigl", "Bigr", "left", "right", "frac", "tfrac", "text", "textrm",
    "substack", "displaystyle", "ldots", "cdots", "dots", "colon", "mid",
    "coloncolon", "setminus", "subset", "subseteq", "supset", "cup", "cap",
    "vee", "wedge", "lnot", "partial", "nabla", "times", "cdot", "circ",
    "langle", "rangle", "lbrack", "rbrack", "lbrace", "rbrace", "langle",
    "rangle", "Re", "Im", "arg", "ker", "tr", "rank", "supp", "Vol",
}
bad = [t for t in tokens if t not in known]
print("distinct macro tokens:", len(tokens))
print("UNKNOWN (suspect absorb/typo):", bad)
