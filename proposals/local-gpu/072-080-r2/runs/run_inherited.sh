#!/bin/sh
# Re-runs the inherited gpu scripts (072-080) with python -I; outputs into runs/.
cd "$(dirname "$0")/../.."
OUT=072-080-r2/runs
for s in 072-g-edge-resum-dominant-rep/s1_moment_decomposition.py 072-g-edge-resum-dominant-rep/s2_hook_content.py 072-g-edge-resum-dominant-rep/s3_saddle_residual.py \
 073-g-edge-rowshift/s4_uniform_rowshift.py 073-g-edge-rowshift/s5_scaling_and_breakdown.py \
 074-g-edge-uqstack/s1_uq_closedform.py 074-g-edge-uqstack/s2_uq_scaling.py 074-g-edge-uqstack/s3_uq_boxmin.py \
 075-g-edge-frameavg/s1_frame_edge_data.py 075-g-edge-frameavg/s2_frame_two_row.py 075-g-edge-frameavg/s3_frame_stacked.py \
 076-g-edge-uqstack-selrule/s1_coincident_qlift.py 076-g-edge-uqstack-selrule/s2_band_sep_two_caps.py 076-g-edge-uqstack-selrule/s3_moment_mismatch.py 076-g-edge-uqstack-selrule/s4_product_qcopies.py \
 077-g-selrule-copyinv/s1_typicality_exact.py 077-g-selrule-copyinv/s3_criterion_blockdiag.py 077-g-selrule-copyinv/s4b_gram_mixture_fixed.py 077-g-selrule-copyinv/s5_gram_and_q2_exact.py 077-g-selrule-copyinv/s6_imalpha.py \
 078-g-selrule-imalpha/s1_structure_general_q.py 078-g-selrule-imalpha/s2b_imalpha_exact_fixed.py 078-g-selrule-imalpha/s3_scalarK_general_q.py \
 079-g-frameavg-residual/s1_exact_lemma.py 079-g-frameavg-residual/s2_frame_uniform_check.py \
 080-g-selrule-mixedmult/s1_spectrum_mixed.py 080-g-selrule-mixedmult/s2_q2_criterion.py 080-g-selrule-mixedmult/s3_mixed_moments.py ; do
  n=$(echo $s | sed 's#/#__#')
  t0=$(date +%s)
  python -I $s > $OUT/$n.out 2> $OUT/$n.err
  rc=$?
  t1=$(date +%s)
  echo "$s rc=$rc secs=$((t1-t0)) last=$(tail -1 $OUT/$n.out)" >> $OUT/summary.txt
done
echo DONE >> $OUT/summary.txt
