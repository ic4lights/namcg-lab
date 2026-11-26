cd "$(git rev-parse --show-toplevel)"
f=chapters/appH-microscopic-proofs.tex
echo "replace-sentence count:"; grep -cF "The gluing selected by the matrix state is not determined here." $f
echo "insert anchor count:"; grep -cF "or the Kaluza--Klein sector. Problems~B, C, D, F and~G remain open." $f
echo "next section after anchor:"; grep -nF '\section{Problem C: conformal mode and Cassini}' $f
echo "bib keys present:"; for k in MantaSteinackerTran2024 Solodukhin2011 IKKT1997 CasiniHuerta2009 FursaevMiele1997; do printf '%s ' $k; grep -c "{$k," bib/namcg.bib; done
echo "macros in insert:"; grep -o '\[A-Za-z]*' proposals/019-fermion-replica-gluing/appH_insert.tex | sort -u | tr '\n' ' '
