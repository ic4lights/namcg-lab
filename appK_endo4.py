import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats as stats

# ==========================================
# 1. Define Correlation Models
# ==========================================

def hellings_downs_curve(theta):
    """Standard GR Hellings-Downs spatial correlation for tensor modes."""
    x = (1 - np.cos(theta)) / 2
    # Handle zero separation case (pulsar with itself) to avoid log(0)
    hd = np.where(x == 0, 1.0, 3 * x * np.log(x + 1e-12) - 0.25 * x + 0.5)
    return hd

def namcg_scalar_curve(theta):
    """
    Theoretical spatial correlation for a pure NAMCG conformal/breathing mode.
    Modeled as an isotropic monopolar correlation.
    """
    return np.ones_like(theta)

def mixed_namcg_correlation(theta, kappa_b):
    """
    Linear combination of GR tensor and NAMCG scalar correlations.
    kappa_b: Fractional power in the conformal mode.
    """
    return (1 - kappa_b) * hellings_downs_curve(theta) + kappa_b * namcg_scalar_curve(theta)

# ==========================================
# 2. Empirical PTA Data (Representative)
# ==========================================
# These values are representative of binned spatial correlation data 
# consistent with recent 15-year PTA dataset structures.
angular_bins_deg = np.array([12.5, 27.5, 42.5, 57.5, 72.5, 87.5, 102.5, 117.5, 132.5, 147.5, 162.5, 177.5])
angular_bins_rad = np.radians(angular_bins_deg)

# Representative observed correlation values (Gamma) and 1-sigma uncertainties
gamma_obs = np.array([
    0.35,  0.15, -0.05, -0.25, -0.35, -0.30, -0.15,  0.05,  0.10,  0.20,  0.25,  0.30
])
gamma_err = np.array([
    0.15,  0.12,  0.10,  0.10,  0.12,  0.14,  0.15,  0.16,  0.15,  0.14,  0.15,  0.18
])

# ==========================================
# 3. Statistical Fitting & Upper Limit
# ==========================================

def perform_namcg_fit():
    print("--- NAMCG Conformal Mode constraints via PTA Data ---")
    
    # Fit the mixed model to the empirical data
    # Bounds: kappa_b must be between 0 (Pure GR) and 1 (Pure Scalar)
    popt, pcov = curve_fit(
        mixed_namcg_correlation, 
        angular_bins_rad, 
        gamma_obs, 
        sigma=gamma_err, 
        absolute_sigma=True,
        bounds=(0.0, 1.0)
    )
    
    kappa_b_fit = popt[0]
    kappa_b_std = np.sqrt(pcov[0, 0])
    
    # Calculate 95% Confidence Upper Limit (1-tailed normal distribution approximation)
    # Z-score for 95% is 1.645
    z_95 = stats.norm.ppf(0.95)
    kappa_b_upper_limit = kappa_b_fit + (z_95 * kappa_b_std)
    
    print(f"Best-fit Scalar Fraction (\u03BA_b): {kappa_b_fit:.4f} \u00B1 {kappa_b_std:.4f}")
    print(f"95% Confidence Upper Limit: \u03BA_b < {kappa_b_upper_limit:.4f}")
    
    # Calculate reduced Chi-Squared
    residuals = gamma_obs - mixed_namcg_correlation(angular_bins_rad, kappa_b_fit)
    chi_sq = np.sum((residuals / gamma_err)**2)
    dof = len(gamma_obs) - 1
    reduced_chi_sq = chi_sq / dof
    print(f"Reduced \u03C7\u00B2: {reduced_chi_sq:.3f}")
    
    return kappa_b_fit, kappa_b_upper_limit

# ==========================================
# 4. Visualization
# ==========================================
def plot_results(kappa_b_fit, kappa_b_upper_limit):
    theta_smooth = np.linspace(0.01, np.pi, 200)
    theta_smooth_deg = np.degrees(theta_smooth)
    
    plt.figure(figsize=(10, 6))
    
    # Empirical Data
    plt.errorbar(angular_bins_deg, gamma_obs, yerr=gamma_err, fmt='ko', label='Binned PTA Data (Rep.)', capsize=4, zorder=5)
    
    # Standard GR
    plt.plot(theta_smooth_deg, hellings_downs_curve(theta_smooth), 'k--', label='Pure GR (\u03BA_b = 0)')
    
    # Best Fit NAMCG
    plt.plot(theta_smooth_deg, mixed_namcg_correlation(theta_smooth, kappa_b_fit), 'b-', linewidth=2, 
             label=f'Best Fit NAMCG (\u03BA_b = {kappa_b_fit:.3f})')
    
    # 95% Upper Limit Constraint
    plt.plot(theta_smooth_deg, mixed_namcg_correlation(theta_smooth, kappa_b_upper_limit), 'r-.', 
             label=f'95% Upper Limit (\u03BA_b = {kappa_b_upper_limit:.3f})')

    plt.axhline(0, color='gray', linestyle=':', linewidth=1)
    plt.title('NAMCG Conformal Mode Bounds from Spatial Correlations')
    plt.xlabel('Pulsar Angular Separation (degrees)')
    plt.ylabel(r'Correlation Coefficient $\Gamma(\theta)$')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    best_fit, upper_limit = perform_namcg_fit()
    plot_results(best_fit, upper_limit)