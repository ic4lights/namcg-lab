import os
import numpy as np
import pandas as pd
from scipy.optimize import minimize

# --- PHYSICAL CONSTANTS ---
G = 4.3009e-3  # pc M_sun^-1 (km/s)^2[cite: 7, 8]
g_s_si = 1.20e-10  # m/s^2[cite: 7, 8]
g_s_kms2_pc = g_s_si * 3.08567758e10  # converted to pc (km/s)^2[cite: 7, 8]

def g_newton(M_total, r):
    return G * M_total / (r**2)  #[cite: 7, 8]

def nu_namcg(g_n, g_scale):
    return 1 / (1 - np.exp(-np.sqrt(g_n / g_scale)))  #[cite: 7, 8]

def predict_v3D(M_total, r_3D, g_scale=g_s_kms2_pc, model='NAMCG'):
    g_n = g_newton(M_total, r_3D)  #[cite: 7, 8]
    if model == 'Newton':
        v2 = g_n * r_3D  #[cite: 7, 8]
    elif model == 'NAMCG':
        v2 = g_n * nu_namcg(g_n, g_scale) * r_3D  #[cite: 7, 8]
    elif model == 'MOND':
        # Simple MOND interpolator for comparison[cite: 7, 8]
        nu_mond = 0.5 * (1 + np.sqrt(1 + 4 * g_scale / g_n))  #[cite: 7, 8]
        v2 = g_n * nu_mond * r_3D  #[cite: 7, 8]
    return np.sqrt(v2)

def gmm_negative_log_likelihood(params, df_gaia, model='NAMCG'):
    """
    Two-component Gaussian Mixture Model (GMM) log-likelihood.
    Separates bound wide binaries from unresolved hierarchical triples and optical chance alignments.
    """
    sigma_sys = params[0]   # Core wide binary systematic dispersion (~0.3-0.5 km/s)
    sigma_trip = params[1]  # Contaminant tail dispersion (~1.5-10.0 km/s)
    f_trip = params[2]      # Fraction of contaminated systems (0.0 to 0.5)
    
    v_pred = predict_v3D(df_gaia['M_total'], df_gaia['r_3D'], g_s_kms2_pc, model=model)  #[cite: 7, 8]
    
    var_obs = df_gaia['v_3D_err']**2  #[cite: 7, 8]
    var_core = var_obs + sigma_sys**2
    var_tail = var_obs + sigma_trip**2
    
    # Core bound binary signal likelihood
    like_core = (1.0 - f_trip) * (1.0 / np.sqrt(2 * np.pi * var_core)) * \
                np.exp(-0.5 * (df_gaia['v_3D_obs'] - v_pred)**2 / var_core)
                
    # Contaminant tail likelihood (unresolved triples, optical pairs)
    like_tail = f_trip * (1.0 / np.sqrt(2 * np.pi * var_tail)) * \
                np.exp(-0.5 * (df_gaia['v_3D_obs'] - v_pred)**2 / var_tail)
                
    total_likelihood = like_core + like_tail
    return -np.sum(np.log(total_likelihood + 1e-12))

def run_monte_carlo_deprojection():
    print("=" * 82)
    print("Running Monte Carlo Isotropic 3D Deprojection (Gaussian Mixture Model)")
    print("=" * 82)
    
    data_file = "gaia_dr3_wide_binaries.csv"  #[cite: 7, 8]
    if not os.path.exists(data_file):
        print("Error: Processed binary file not found.")  #[cite: 7, 8]
        return
        
    df_raw = pd.read_csv(data_file)  #[cite: 7, 8]
    
    # Monte Carlo Resampling (N_iter realizations per system to average out projection noise)[cite: 7, 8]
    np.random.seed(42)  #[cite: 7, 8]
    n_realizations = 50  #[cite: 7, 8]
    
    deprojected_records = []
    
    for idx, row in df_raw.iterrows():  #[cite: 7, 8]
        r_2d = row['r_2D']  #[cite: 7, 8]
        v_2d_obs = row['v_2D_obs']  #[cite: 7, 8]
        v_err = row['v_2D_err']  #[cite: 7, 8]
        mass = row['M_total']  #[cite: 7, 8]
        
        for _ in range(n_realizations):  #[cite: 7, 8]
            u = np.random.uniform(0.0, 1.0)  #[cite: 7, 8]
            sin_alpha = np.sin(np.arccos(u))  #[cite: 7, 8]
            if sin_alpha < 0.05:  # Avoid division by zero singularities at edge-on extremes[cite: 7, 8]
                continue
                
            r_3d = r_2d / sin_alpha  #[cite: 7, 8]
            v_3d_obs = v_2d_obs * np.sqrt(1.5)   #[cite: 7, 8]
            
            deprojected_records.append({
                'M_total': mass,
                'r_3D': r_3d,
                'v_3D_obs': v_3d_obs,
                'v_3D_err': v_err * np.sqrt(1.5)
            })  #[cite: 7, 8]
            
    df_mc = pd.DataFrame(deprojected_records)  #[cite: 7, 8]
    print(f"Generated {len(df_mc)} Monte Carlo deprojected phase-space realizations.\n")  #[cite: 7, 8]
    
    # --- MODEL COMPARISON ON DEPROJECTED DATA WITH GMM ---
    models = ['Newton', 'MOND', 'NAMCG']  #[cite: 7, 8]
    results = {}
    
    print(f"{'Model':<10} | {'AIC':<12} | {'NLL':<12} | {'Sig_sys (km/s)':<15} | {'Sig_trip (km/s)':<16} | {'F_trip':<8}")
    print("-" * 82)
    
    for mod in models:
        # Initial guesses: [sigma_sys, sigma_trip, f_trip]
        initial_guess = [0.4, 3.0, 0.15]
        bounds = [(0.01, 1.5), (1.5, 10.0), (0.0, 0.5)]
        
        res = minimize(gmm_negative_log_likelihood, x0=initial_guess, args=(df_mc, mod), bounds=bounds)
        
        # k = 3 parameters in GMM
        k = 3
        aic = 2 * k + 2 * res.fun
        
        results[mod] = {
            'AIC': aic, 
            'NLL': res.fun, 
            'Sigma_sys': res.x[0],
            'Sigma_trip': res.x[1],
            'F_trip': res.x[2]
        }
        
    sorted_results = sorted(results.items(), key=lambda item: item[1]['AIC'])  #[cite: 7, 8]
    for mod, metrics in sorted_results:
        print(f"{mod:<10} | {metrics['AIC']:<12.2f} | {metrics['NLL']:<12.2f} | {metrics['Sigma_sys']:<15.4f} | {metrics['Sigma_trip']:<16.4f} | {metrics['F_trip']:<8.4f}")
        
    print("\n")
    
    # --- DEPROJECTED RADIAL BIN PROFILE ---
    print("=" * 82)
    print("Deprojected Radial Bin Profile ($r_{3D}$-dependence)")  #[cite: 7, 8]
    print("=" * 82)
    
    bins = [(0.01, 0.02), (0.02, 0.035), (0.035, 0.05)]  # in parsecs (~2000-4000, 4000-7000, 7000-10000 AU)[cite: 7, 8]
    bin_labels = ["2000-4000 AU", "4000-7000 AU", "7000-10000 AU"]  #[cite: 7, 8]
    
    print(f"{'Bin Range (3D)':<18} | {'Mean v_obs / v_Newton':<22} | {'Trend Status'}")  #[cite: 7, 8]
    print("-" * 65)
    
    for (r_min, r_max), label in zip(bins, bin_labels):  #[cite: 7, 8]
        df_bin = df_mc[(df_mc['r_3D'] >= r_min) & (df_mc['r_3D'] < r_max)]  #[cite: 7, 8]
        if len(df_bin) < 50:  #[cite: 7, 8]
            continue
            
        v_newton = np.sqrt(g_newton(df_bin['M_total'], df_bin['r_3D']) * df_bin['r_3D'])  #[cite: 7, 8]
        ratio = np.mean(df_bin['v_3D_obs'] / v_newton)  #[cite: 7, 8]
        
        status = "Rising (Anomaly Active)" if ratio > 1.0 else "Flat / Newtonian"  #[cite: 7, 8]
        print(f"{label:<18} | {ratio:<22.4f} | {status}")  #[cite: 7, 8]
    print("\n")

if __name__ == "__main__":
    run_monte_carlo_deprojection()  #[cite: 7, 8]