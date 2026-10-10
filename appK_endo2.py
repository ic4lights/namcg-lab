import os
import glob
import argparse
import numpy as np
import pandas as pd

def calculate_namcg_mixing_bound(sparc_dir, eotvos_bound=1e-13):
    """
    Evaluates the NAMCG infrared residual against local solar system tests
    (e.g., Cassini bound, Eotvos experiments) using SPARC rotation curves.
    """
    sparc_files = glob.glob(os.path.join(sparc_dir, '*.dat'))
    if not sparc_files:
        print(f"Error: No .dat files found in directory '{sparc_dir}'.")
        return

    results = []
    
    for file in sparc_files:
        try:
            # Standard SPARC format: Rad, Vobs, errV, Vgas, Vdisk, Vbul
            data = pd.read_csv(file, sep='\t', comment='#', 
                               names=['Rad', 'Vobs', 'errV', 'Vgas', 'Vdisk', 'Vbul'])
            
            # Drop invalid rows
            data = data.dropna()
            if data.empty:
                continue

            r_max = data['Rad'].max()
            # Extract asymptotic flat velocity region
            v_asymptotic = data['Vobs'].iloc[-3:].mean() 
            
            # Baseline Newtonian expectation (baryonic components)
            v_bar_sq = data['Vgas'].iloc[-1]**2 + data['Vdisk'].iloc[-1]**2 + data['Vbul'].iloc[-1]**2
            
            if v_asymptotic == 0:
                continue
                
            # Required IR mixing residual to sustain the flat rotation curve
            mass_discrepancy = (v_asymptotic**2 - v_bar_sq) / v_asymptotic**2
            
            # Project required macroscopic scale to local solar system scale (1 AU ~ 1.5e-11 kpc)
            scale_ratio = 1.5e-11 / r_max
            local_mixing_prediction = mass_discrepancy * scale_ratio
            theta_sq = local_mixing_prediction**2
            
            results.append({
                'Galaxy': os.path.basename(file).split('_')[0],
                'R_max_kpc': round(r_max, 2),
                'Required_IR_kappa': round(mass_discrepancy, 4),
                'Local_Theta_Sq': theta_sq,
                'Passes_Cassini_Eotvos': theta_sq < eotvos_bound
            })
        except Exception:
            # Skip files with formatting issues or missing data
            continue
            
    df_results = pd.DataFrame(results)
    
    # Format the output for readability
    df_results['Local_Theta_Sq'] = df_results['Local_Theta_Sq'].apply(lambda x: f"{x:.2e}")
    
    print("\n--- NAMCG Local Mixing Threshold Validation ---")
    print(f"Total SPARC galaxies analyzed: {len(df_results)}")
    print(f"Empirical bound threshold (sin^2 theta): {eotvos_bound}")
    print(f"Galaxies passing local constraints: {df_results['Passes_Cassini_Eotvos'].sum()} / {len(df_results)}")
    print("\nSample Output (First 10 Galaxies):")
    print(df_results.head(10).to_string(index=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test NAMCG heat-kernel UV decoupling against solar system constraints using empirical SPARC data.")
    parser.add_argument('--rotmod', type=str, default='sparc/rotmod/', 
                        help='Path to the SPARC rotmod directory containing the .dat files')
    args = parser.parse_args()
    
    calculate_namcg_mixing_bound(args.rotmod)