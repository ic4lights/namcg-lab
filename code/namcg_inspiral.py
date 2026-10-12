import numpy as np
import matplotlib.pyplot as plt


def run_namcg_laboratory(
    G_toy=36.0,
    eta=0.006,
    M=1.0,
    mu=1.0,
    d0=1.0,
    dt=1.0e-3,
    num_steps=12000,
):
    r = np.array([d0, 0.0])
    v = np.array([0.0, np.sqrt(G_toy * M / d0)])
    traj = np.zeros((num_steps + 1, 2))
    E_mech = np.zeros(num_steps + 1)
    W_diss = np.zeros(num_steps + 1)
    traj[0] = r

    def a_N(rvec):
        d = np.linalg.norm(rvec)
        return -G_toy * M * rvec / d**3

    def a_d(rvec, vvec):
        d = np.linalg.norm(rvec)
        return -eta * vvec / d**4

    def mechanical_energy(rvec, vvec):
        d = np.linalg.norm(rvec)
        return 0.5 * mu * np.dot(vvec, vvec) - G_toy * M * mu / d

    E_mech[0] = mechanical_energy(r, v)
    for n in range(num_steps):
        F_d = mu * a_d(r, v)
        W_diss[n + 1] = W_diss[n] + np.dot(F_d, v) * dt
        v_half = v + 0.5 * dt * (a_N(r) + a_d(r, v))
        r = r + dt * v_half
        v = v_half + 0.5 * dt * (a_N(r) + a_d(r, v_half))
        traj[n + 1] = r
        E_mech[n + 1] = mechanical_energy(r, v)
    return traj, E_mech, W_diss


def plot_laboratory(traj, E_mech, W_diss, filename):
    E_bal = E_mech - W_diss
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.6))
    axes[0].plot(traj[:, 0], traj[:, 1], lw=0.8)
    axes[0].set_aspect("equal")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    axes[0].set_title("Laboratory trajectory")
    t = np.arange(len(E_mech))
    axes[1].plot(t, E_mech, label=r"$E_{\mathrm{mech}}$")
    axes[1].plot(t, W_diss, label=r"$W_{\mathrm{diss}}$")
    axes[1].plot(t, E_bal, label=r"$\mathcal{E}$")
    axes[1].set_xlabel("step")
    axes[1].set_title("Energy balance")
    axes[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(filename)
    plt.close(fig)


if __name__ == "__main__":
    traj, E_mech, W_diss = run_namcg_laboratory()
    plot_laboratory(
        traj,
        E_mech,
        W_diss,
        "figs/namcg_gr_simulation_corrected.pdf",
    )