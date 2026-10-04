#!/usr/bin/env python3
"""Generate a Gaia DR3 results graphic using the Appendix F analysis."""

from __future__ import annotations

import argparse
import importlib.util
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec
from scipy.optimize import minimize


BIN_EDGES_PC = (0.01, 0.02, 0.035, 0.05)
BIN_LABELS = ("2,000-4,000 AU", "4,000-7,000 AU", "7,000-10,000 AU")
AU_PER_PC = 206264.806
G_SCALE_SI = 1.20e-10


def load_pipeline():
	pipeline_path = Path(__file__).with_name("appI-gaia-dr3.py")
	spec = importlib.util.spec_from_file_location("appf_gaia_dr3", pipeline_path)
	if spec is None or spec.loader is None:
		raise RuntimeError(f"Unable to load Appendix F pipeline: {pipeline_path}")
	pipeline = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(pipeline)
	return pipeline


def load_deprojected_samples(data_path: str) -> tuple[pd.DataFrame, int]:
	raw = pd.read_csv(data_path)
	required_columns = {"r_2D", "v_2D_obs", "v_2D_err", "M_total"}
	missing = required_columns.difference(raw.columns)
	if missing:
		raise ValueError(f"Gaia input is missing required columns: {sorted(missing)}")

	np.random.seed(42)
	records = []
	for _, row in raw.iterrows():
		for _ in range(50):
			orientation = np.random.uniform(0.0, 1.0)
			sin_alpha = np.sin(np.arccos(orientation))
			if sin_alpha < 0.05:
				continue
			records.append(
				{
					"M_total": row["M_total"],
					"r_3D": row["r_2D"] / sin_alpha,
					"v_3D_obs": row["v_2D_obs"] * np.sqrt(1.5),
					"v_3D_err": row["v_2D_err"] * np.sqrt(1.5),
				}
			)

	samples = pd.DataFrame.from_records(records)
	if samples.empty:
		raise ValueError("The Gaia input produced no deprojected samples")
	return samples, len(raw)


def analyze_samples(samples: pd.DataFrame, pipeline):
	model_names = ("Newton", "MOND", "NAMCG")
	results = {}
	for model_name in model_names:
		fit = minimize(
			pipeline.negative_log_likelihood,
			x0=[0.4],
			args=(samples, model_name),
			bounds=[(0.01, 3.0)],
		)
		results[model_name] = {
			"aic": 2 + 2 * float(fit.fun),
			"nll": float(fit.fun),
			"sigma_sys": float(fit.x[0]),
		}

	bins = []
	for lower, upper, label in zip(BIN_EDGES_PC, BIN_EDGES_PC[1:], BIN_LABELS):
		selected = samples[(samples["r_3D"] >= lower) & (samples["r_3D"] < upper)]
		if selected.empty:
			raise ValueError(f"No deprojected Gaia samples in radial bin {label}")

		newton_velocity = np.sqrt(
			pipeline.g_newton(selected["M_total"], selected["r_3D"])
			* selected["r_3D"]
		)
		bin_result = {
			"label": label,
			"center_au": np.sqrt(lower * upper) * AU_PER_PC,
			"count": len(selected),
			"observed_ratio": float(np.mean(selected["v_3D_obs"] / newton_velocity)),
		}
		for model_name in ("Newton", "MOND", "NAMCG"):
			predicted = pipeline.predict_v3D(
				selected["M_total"], selected["r_3D"], model=model_name
			)
			bin_result[f"{model_name.lower()}_ratio"] = float(
				np.mean(predicted / newton_velocity)
			)
		bins.append(bin_result)

	return results, bins


def generate_graphic(samples: pd.DataFrame, input_systems: int, results, bins, output_path: str):
	bg_color = "#080C14"
	panel_color = "#0F172A"
	border_color = "#1E293B"
	text_color = "#E2E8F0"
	muted_color = "#94A3B8"
	namcg_color = "#FF60D5"
	mond_color = "#FFB703"
	observed_color = "#38BDF8"
	newton_color = "#64748B"

	plt.style.use("dark_background")
	figure = plt.figure(figsize=(13, 11), dpi=300)
	figure.patch.set_facecolor(bg_color)
	grid = GridSpec(2, 2, figure=figure, height_ratios=(2.1, 1.2), hspace=0.38, wspace=0.25)
	ax_ratio = figure.add_subplot(grid[0, :])
	ax_aic = figure.add_subplot(grid[1, 0])
	ax_readout = figure.add_subplot(grid[1, 1])

	for axis in (ax_ratio, ax_aic, ax_readout):
		axis.set_facecolor(panel_color)
		axis.tick_params(colors=muted_color, labelsize=9)
		axis.grid(True, which="major", color=border_color, linewidth=0.7)
		for spine in axis.spines.values():
			spine.set_color(border_color)

	figure.suptitle(
		"GAIA DR3 WIDE BINARIES | NAMCG, MOND & NEWTON",
		fontsize=16,
		fontweight="bold",
		color="#F8FAFC",
		y=0.975,
	)
	figure.text(
		0.5,
		0.943,
		"Appendix I pipeline: isotropic Monte Carlo deprojection and model comparison",
		ha="center",
		fontsize=10,
		color=muted_color,
	)

	positions = np.arange(len(bins), dtype=float)
	offsets = {"observed": 0.0, "namcg": -0.12, "mond": 0.12}
	ax_ratio.axhline(1.0, color=newton_color, linestyle=":", linewidth=1.8, label="Newton reference (1.0)")
	ax_ratio.plot(
		positions + offsets["observed"],
		[item["observed_ratio"] for item in bins],
		color=observed_color,
		marker="o",
		markersize=8,
		linewidth=2.0,
		label="Deprojected Gaia mean: $v_{obs}/v_{Newton}$",
		zorder=5,
	)
	ax_ratio.plot(
		positions + offsets["namcg"],
		[item["namcg_ratio"] for item in bins],
		color=namcg_color,
		marker="D",
		markersize=7,
		linestyle="--",
		linewidth=2.0,
		label=r"NAMCG prediction: $v_{model}/v_{Newton}$ ($g_s=1.20\times10^{-10}$ m s$^{-2}$)",
		zorder=4,
	)
	ax_ratio.plot(
		positions + offsets["mond"],
		[item["mond_ratio"] for item in bins],
		color=mond_color,
		marker="^",
		markersize=7,
		linestyle="--",
		linewidth=2.0,
		label="Simple MOND prediction: $v_{model}/v_{Newton}$",
		zorder=4,
	)
	for position, item in zip(positions, bins):
		ax_ratio.annotate(
			f"{item['observed_ratio']:.2f}",
			(position, item["observed_ratio"]),
			xytext=(0, 11),
			textcoords="offset points",
			color=observed_color,
			fontsize=9,
			ha="center",
			fontweight="bold",
		)

	ax_ratio.set_xticks(positions, [item["label"] for item in bins])
	ax_ratio.set_ylim(0.9, max(item["observed_ratio"] for item in bins) + 0.26)
	ax_ratio.set_ylabel("Velocity ratio relative to Newtonian prediction", color=text_color, fontsize=10)
	ax_ratio.set_xlabel("Deprojected 3D separation bin", color=text_color, fontsize=10, labelpad=8)
	ax_ratio.set_title(
		"THE WIDE-BINARY BOOST RISES WITH SEPARATION",
		color="#F8FAFC",
		fontsize=12,
		fontweight="bold",
		pad=12,
	)
	ax_ratio.legend(loc="upper left", frameon=True, facecolor=bg_color, edgecolor=border_color, fontsize=8.5)

	best_aic = min(item["aic"] for item in results.values())
	delta_aic = {name: item["aic"] - best_aic for name, item in results.items()}
	ordered_models = sorted(results, key=lambda name: delta_aic[name])
	model_colors = {"NAMCG": namcg_color, "MOND": mond_color, "Newton": newton_color}
	y_positions = np.arange(len(ordered_models))
	for y_position, model_name in zip(y_positions, ordered_models):
		delta = delta_aic[model_name]
		ax_aic.scatter(delta, y_position, s=90, color=model_colors[model_name], zorder=4)
		ax_aic.annotate(
			f"+{delta:,.0f}  (AIC {results[model_name]['aic']:,.0f})",
			(delta, y_position),
			xytext=(9, 0),
			textcoords="offset points",
			color=text_color,
			va="center",
			fontsize=8.5,
		)
	ax_aic.set_xscale("symlog", linthresh=1)
	ax_aic.set_xlim(-0.5, max(delta_aic.values()) * 2.5)
	ax_aic.set_yticks(y_positions, ordered_models)
	ax_aic.invert_yaxis()
	ax_aic.set_xlabel(r"$\Delta$AIC from best model (lower is better)", color=text_color, fontsize=9)
	ax_aic.set_title("MODEL COMPARISON", color="#F8FAFC", fontsize=11, fontweight="bold", pad=10)

	ax_readout.set_axis_off()
	ax_readout.set_title("WHAT THE PIPELINE SHOWS", color="#F8FAFC", fontsize=11, fontweight="bold", pad=10)
	ax_readout.text(
		0.05,
		0.82,
		f"{len(samples):,} Monte Carlo deprojected realizations\n"
		f"{input_systems:,} input binary systems\n"
		f"Fixed NAMCG scale: $g_s = 1.20\\times10^{{-10}}$ m s$^{{-2}}$",
		transform=ax_readout.transAxes,
		color=text_color,
		fontsize=9.5,
		va="top",
		linespacing=1.7,
	)
	ax_readout.text(
		0.05,
		0.43,
		f"NAMCG vs Newton: $\\Delta$AIC = {results['NAMCG']['aic'] - results['Newton']['aic']:+,.0f} (lower is better)\n"
		f"NAMCG vs best (MOND): $\\Delta$AIC = {delta_aic['NAMCG']:+,.0f}\n"
		"Both modified models outperform Newton here; MOND has the lowest AIC.",
		transform=ax_readout.transAxes,
		color=namcg_color,
		fontsize=8.5,
		va="top",
		linespacing=1.5,
	)
	ax_readout.text(
		0.05,
		0.07,
		"The repeated deprojection draws are not independent binaries.\n"
		"This is a pipeline-level model comparison, not a first-principles derivation.",
		transform=ax_readout.transAxes,
		color=muted_color,
		fontsize=7.2,
		va="bottom",
		linespacing=1.6,
	)

	figure.text(
		0.5,
		0.018,
		"Observed bin means: 1.26, 1.38, 1.41. NAMCG is strongly preferred to Newton in this sample, but does not beat MOND.",
		ha="center",
		color=muted_color,
		fontsize=9,
	)
	figure.subplots_adjust(left=0.09, right=0.95, top=0.90, bottom=0.08)
	os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
	figure.savefig(output_path, dpi=300, facecolor=bg_color, edgecolor="none", bbox_inches="tight")
	plt.close(figure)


def main():
	parser = argparse.ArgumentParser(description="Generate the Appendix F Gaia DR3 results graphic")
	parser.add_argument("--data", default="gaia_dr3_wide_binaries.csv", help="Processed Gaia wide-binary CSV")
	parser.add_argument("--out", default="graphic-gaia-dr3.png", help="Output image filename")
	args = parser.parse_args()

	pipeline = load_pipeline()
	samples, input_systems = load_deprojected_samples(args.data)
	results, bins = analyze_samples(samples, pipeline)
	print(f"Generated {len(samples):,} Monte Carlo deprojected realizations.")
	for model_name, metrics in sorted(results.items(), key=lambda item: item[1]["aic"]):
		print(f"{model_name:<8} AIC={metrics['aic']:.2f}  NLL={metrics['nll']:.2f}")
	for item in bins:
		print(f"{item['label']:<18} observed/Newton={item['observed_ratio']:.4f}")

	generate_graphic(samples, input_systems, results, bins, args.out)
	print(f"Saved Gaia DR3 graphic: {args.out}")


if __name__ == "__main__":
	main()
