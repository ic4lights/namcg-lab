import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Cosmological Parameters & JWST Data
OMEGA_M = 0.315
OMEGA_L = 1.0 - OMEGA_M

# JADES/CEERS Observational Data
jwst_z10_Muv = np.array([-21.5, -20.5, -19.5, -18.5])
jwst_z10_Phi = np.array([1.5e-5, 8.0e-5, 4.0e-4, 1.2e-3])
jwst_z10_err = np.array([0.8e-5, 3.0e-5, 1.0e-4, 0.4e-3])

jwst_z12_Muv = np.array([-21.0, -20.0, -19.0])
jwst_z12_Phi = np.array([3.0e-6, 2.5e-5, 1.5e-4])
jwst_z12_err = np.array([2.0e-6, 1.0e-5, 0.5e-4])

def beta_dynamic(z, beta_ref=0.5, z_ref=11.0, gamma=0.8):
    """Calculates dynamical scaling of the conformal trace anomaly."""
    return beta_ref * ((1.0 + z_ref) / (1.0 + z))**gamma

def E(a):
    return np.sqrt(OMEGA_M * a**-3 + OMEGA_L)

def lcdm_growth_factor(z):
    a_target = 1.0 / (1.0 + z)
    def integrand(a): return 1.0 / (a * E(a))**3
    integral, _ = integrate.quad(integrand, 0, a_target)
    integral0, _ = integrate.quad(integrand, 0, 1.0)
    return (E(a_target) * integral) / (E(1.0) * integral0)

def namcg_growth_factor(z):
    beta_z = beta_dynamic(z)
    return lcdm_growth_factor(z) * (1.0 + beta_z * np.log(1.0 + z))

def theoretical_uvlf(M_uv_range, z, is_namcg=False):
    D_z = namcg_growth_factor(z) if is_namcg else lcdm_growth_factor(z)
    # Halo Mass to UV Magnitude Mapping
    M_h_range = 10**((4.5 - M_uv_range) / 2.5) / (0.05 * 0.049 / OMEGA_M)
    sigma_z = 0.81 * (1e13 / M_h_range)**0.3 * D_z 
    nu_c = 1.686 / sigma_z
    rho_m = 2.78e11 * OMEGA_M  
    # Sheth-Tormen Mass Function
    phi = np.sqrt(2/np.pi) * (rho_m / M_h_range) * 0.3 * nu_c * np.exp(-0.5 * nu_c**2)
    return np.maximum(phi, 1e-30) * 0.921

# Output Generation
M_uv_plot = np.linspace(-22.5, -17.5, 50)
plt.figure(figsize=(10, 6))

plt.errorbar(jwst_z10_Muv, jwst_z10_Phi, yerr=jwst_z10_err, fmt='bo', 
             label='JWST Data (z $\\approx$ 10)')
plt.plot(M_uv_plot, theoretical_uvlf(M_uv_plot, 10.0, is_namcg=False), 
         'b--', alpha=0.5, label='Standard $\\Lambda$CDM (z=10)')
plt.plot(M_uv_plot, theoretical_uvlf(M_uv_plot, 10.0, is_namcg=True), 
         'b-', linewidth=2.5, label='NAMCG Dynamic (z=10)')

plt.errorbar(jwst_z12_Muv, jwst_z12_Phi, yerr=jwst_z12_err, fmt='ro', 
             label='JWST Data (z $\\approx$ 12)')
plt.plot(M_uv_plot, theoretical_uvlf(M_uv_plot, 12.0, is_namcg=False), 
         'r--', alpha=0.5, label='Standard $\\Lambda$CDM (z=12)')
plt.plot(M_uv_plot, theoretical_uvlf(M_uv_plot, 12.0, is_namcg=True), 
         'r-', linewidth=2.5, label='NAMCG Dynamic (z=12)')

plt.yscale('log')
plt.gca().invert_xaxis()
plt.ylim(1e-7, 1e-2)
plt.xlim(-17.5, -23.0)
plt.xlabel('Absolute UV Magnitude ($M_{UV}$)', fontsize=12)
plt.ylabel('Number Density $\\Phi$ (Mpc$^{-3}$ mag$^{-1}$)', fontsize=12)
plt.legend(loc='upper right', framealpha=0.9)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figs/Figure_3_Dynamic_NAMCG_UVLF.pdf', format='pdf', dpi=300, bbox_inches='tight')
