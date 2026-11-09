"""
Proposal 062: re-derivation of the worked example of appH L2797 (the beta_K=1
point on S^2_N with a tree cubic), to check whether the recorded numbers are
self-consistent (no correction needed, or a PRIOR-CLAIM-ERROR flag).

Units: F sqrt|g| N^2 vartheta^2 / 32 pi^2, vartheta = 1, x = chi^2/vartheta = 3/10.
At large N with Uhat/N^2 -> 1, That/N^2 -> 4 (appH L2797):
    U4 = -(Uhat/N^2) x^2 = -0.09
    U2(V=T) = -(3/4)(That/N^2) x = -0.9
The manuscript records "a tree quartic 7.935 and a tree cubic -12.36" at
x = 3/10: read as the VALUES of the tree terms at chi (not coefficients), and
eps = U4/Utilde with Utilde = the tree-quartic value.

Quantities checked against L2797:
    |eps| = 0.09/7.935 = 0.0113...  (recorded: |eps| ~ 0.011)
    U_chichi = D^2 U, D = chi d/dchi, on term values: 16*quartic_value +
               9*cubic_value + 4*U2 + 16*U4 = 16*7.935 + 9*(-12.36) + 4*(-0.9) + 16*(-0.09)
               = 10.68            (recorded: U_chichi = 10.68)
    beta_K = 1 in the cubic case requires 4U4 + 6U2 + 5Y = 4*Utilde, giving Y = 7.5;
    with Y = 7.5: beta_K = 2(4U4+2U2+Y)/(4Utilde+4U4-2U2-3Y) = 1.000 and the
    denominator equals 10.68 = U_chichi; Y = (15/2)(N_K/N^2) gives N_K/N^2 = 1.
"""

def main():
    x = 0.3
    Uhat_frac, That_frac = 1.0, 4.0
    U4 = -Uhat_frac * x**2
    U2 = -(3/4) * That_frac * x
    quartic_value, cubic_value = 7.935, -12.36
    eps = U4 / quartic_value
    Uchichi = 16*quartic_value + 9*cubic_value + 4*U2 + 16*U4
    print(f"U4 = {U4:.6f}   U2(V=T) = {U2:.6f}")
    print(f"eps = U4/Utilde = {eps:.6f}   |eps| = {abs(eps):.4f}   (recorded |eps| ~ 0.011)")
    print(f"U_chichi = D^2 U = {Uchichi:.6f}   (recorded 10.68)")
    Y = (4*quartic_value - 4*U4 - 6*U2) / 5.0
    beta = 2*(4*U4 + 2*U2 + Y) / (4*quartic_value + 4*U4 - 2*U2 - 3*Y)
    denom = 4*quartic_value + 4*U4 - 2*U2 - 3*Y
    print(f"Y from beta_K=1 condition: Y = {Y:.4f};  beta_K = {beta:.6f};  denominator = {denom:.4f}")
    print(f"N_K/N^2 = (2/15) Y = {2*Y/15:.4f}")
    ok = (abs(abs(eps) - 0.011) < 5e-4) and (abs(Uchichi - 10.68) < 5e-3) and (abs(beta - 1) < 1e-9)
    print("all recorded values reproduced:", ok)

if __name__ == "__main__":
    main()
