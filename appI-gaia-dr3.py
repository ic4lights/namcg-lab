import numpy as np
import pandas as pd
from scipy.optimize import minimize
import os

# --- PHYSICAL CONSTANTS ---
G = 4.3009e-3  # pc M_sun^-1 (km/s)^2
g_s_si = 1.20e-10 
g_s_kms2_pc = g_s_si * 3.08567758e10 

def g_newton(M_total, r):
    return G * M_total / (r**2)

def nu_namcg(g_n, g_scale):
    return 1 / (1 - np.exp(-np.sqrt(g_n / g_scale)))

def predict_v3D(M_total, r_3D, g_scale=g_s_kms2_pc, model='NAMCG'):
    g_n = g_newton(M_total, r_3D)
    if model == 'Newton':
        v2 = g_n * r_3D
    elif model == 'NAMCG':
        v2 = g_n * nu_namcg(g_n, g_scale) * r_3D
    elif model == 'MOND':
        # Simple MOND interpolator for comparison
        nu_mond = 0.5 * (1 + np.sqrt(1 + 4 * g_scale / g_n))
        v2 = g_n * nu_mond * r_3D
    return np.sqrt(v2)

def negative_log_likelihood(params, df_gaia, model='NAMCG'):
    sigma_sys = params[0]
    v_pred = predict_v3D(df_gaia['M_total'], df_gaia['r_3D'], g_s_kms2_pc, model=model)
    total_var = df_gaia['v_3D_err']**2 + sigma_sys**2
    return 0.5 * np.sum(np.log(2 * np.pi * total_var) + ((df_gaia['v_3D_obs'] - v_pred)**2 / total_var))

def run_monte_carlo_deprojection():
    print("=" * 70)
    print("Running Monte Carlo Isotropic 3D Deprojection on Pristine Binaries")
    print("=" * 70)
    
    data_file = "gaia_dr3_wide_binaries.csv"
    if not os.path.exists(data_file):
        print("Error: Processed binary file not found.")
        return
        
    df_raw = pd.read_csv(data_file)
    
    # Monte Carlo Resampling (N_iter realizations per system to average out projection noise)
    np.random.seed(42)
    n_realizations = 50
    
    deprojected_records = []
    
    for idx, row in df_raw.iterrows():
        r_2d = row['r_2D']
        v_2d_obs = row['v_2D_obs']
        v_err = row['v_2D_err']
        mass = row['M_total']
        
        for _ in range(n_realizations):
            # Draw random projection angle for isotropic orbit on the sky
            u = np.random.uniform(0.0, 1.0)
            sin_alpha = np.sin(np.arccos(u))
            if sin_alpha < 0.05:  # Avoid division by zero singularities at edge-on extremes
                continue
                
            # True 3D separation
            r_3d = r_2d / sin_alpha
            
            # Statistical 3D velocity correction from transverse 2D velocity component
            # v_3d approx v_2d / sqrt(2/3) isotropic velocity dispersion mapping
            v_3d_obs = v_2d_obs * np.sqrt(1.5) 
            
            deprojected_records.append({
                'M_total': mass,
                'r_3D': r_3d,
                'v_3D_obs': v_3d_obs,
                'v_3D_err': v_err * np.sqrt(1.5)
            })
            
    df_mc = pd.DataFrame(deprojected_records)
    print(f"Generated {len(df_mc)} Monte Carlo deprojected phase-space realizations.\n")
    
    # --- MODEL COMPARISON ON DEPROJECTED DATA ---
    models = ['Newton', 'MOND', 'NAMCG']
    results = {}
    
    print(f"{'Model':<10} | {'AIC':<12} | {'NLL':<12} | {'Sigma_sys (km/s)'}")
    print("-" * 55)
    
    for mod in models:
        res = minimize(negative_log_likelihood, x0=[0.4], args=(df_mc, mod), bounds=[(0.01, 3.0)])
        aic = 2 * 1 + 2 * res.fun
        results[mod] = {'AIC': aic, 'NLL': res.fun, 'Sigma_sys': res.x[0]}
        
    sorted_results = sorted(results.items(), key=lambda item: item[1]['AIC'])
    for mod, metrics in sorted_results:
        print(f"{mod:<10} | {metrics['AIC']:<12.2f} | {metrics['NLL']:<12.2f} | {metrics['Sigma_sys']:<15.4f}")
        
    print("\n")
    
    # --- DEPROJECTED RADIAL BIN PROFILE ---
    print("=" * 70)
    print("Deprojected Radial Bin Profile ($r_{3D}$-dependence)")
    print("=" * 70)
    
    bins = [(0.01, 0.02), (0.02, 0.035), (0.035, 0.05)] # in parsecs (~2000-4000, 4000-7000, 7000-10000 AU)
    bin_labels = ["2000-4000 AU", "4000-7000 AU", "7000-10000 AU"]
    
    print(f"{'Bin Range (3D)':<18} | {'Mean v_obs / v_Newton':<22} | {'Trend Status'}")
    print("-" * 65)
    
    for (r_min, r_max), label in zip(bins, bin_labels):
        df_bin = df_mc[(df_mc['r_3D'] >= r_min) & (df_mc['r_3D'] < r_max)]
        if len(df_bin) < 50:
            continue
            
        v_newton = np.sqrt(g_newton(df_bin['M_total'], df_bin['r_3D']) * df_bin['r_3D'])
        ratio = np.mean(df_bin['v_3D_obs'] / v_newton)
        
        status = "Rising (Anomaly Active)" if ratio > 1.0 else "Flat / Newtonian"
        print(f"{label:<18} | {ratio:<22.4f} | {status}")
    print("\n")

if __name__ == "__main__":
    run_monte_carlo_deprojection()