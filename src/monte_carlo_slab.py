import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import expn

# --- GIVEN PARAMETERS ---
SIGMA_A = 0.5   
H = 3.0        
S_BAR = 2.0 * H
N_VALUES = [10**2, 10**4, 10**6]

# --- ANALYTICAL SOLUTION ---
def analytic_solution(sigma_a, h):
    # Analytic solution for escape probability and blackness
    tau = sigma_a * h
    e3 = expn(3, tau)
    p_esc = (1.0 - 2.0 * e3) / (2.0 * tau)
    beta = sigma_a * (2.0 * h) * p_esc
    return p_esc, beta

# --- MONTE CARLO SIMULATION ---
def monte_carlo_run(N, sigma_a, h, seed):
    rng = np.random.default_rng(seed)

    # Neutron start positions (Uniform z in [0, H])
    z = rng.uniform(0.0, h, size=N)

    # Direction cosine (Isotropic -> Uniform mu in [-1, 1])
    mu = rng.uniform(-1.0, 1.0, size=N)

    # Avoid division by zero
    tiny = 1e-12
    mu[np.abs(mu) < tiny] = np.sign(mu[np.abs(mu) < tiny]) * tiny

    # Distance to slab boundary
    d_boundary = np.where(mu > 0.0, (h - z) / mu, -z / mu)

    # Free path length in absorbing medium
    xi = rng.random(size=N)
    free_path = -np.log(xi) / sigma_a

    # Check if neutrons escape
    escaped = free_path >= d_boundary

    # Monte Carlo Estimators
    p_mc = np.mean(escaped)
    beta_mc = sigma_a * (2.0 * h) * p_mc

    # Simple statistical uncertainty
    sigma_p = np.sqrt(p_mc * (1.0 - p_mc) / N)
    sigma_beta = sigma_a * (2.0 * h) * sigma_p

    return p_mc, beta_mc, sigma_p, sigma_beta

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    p_an, beta_an = analytic_solution(SIGMA_A, H)

    print("Analytical reference values:")
    print(f"P_esc = {p_an:.6f}")
    print(f"beta  = {beta_an:.6f}")
    print("-" * 30)

    results = []

    for N in N_VALUES:
        seed = 42 + N
        p_mc, beta_mc, sig_p, sig_beta = monte_carlo_run(N, SIGMA_A, H, seed)

        err_p = abs(p_mc - p_an) / p_an
        err_beta = abs(beta_mc - beta_an) / beta_an

        results.append({
            "N_T": N,
            "P_esc_MC": p_mc,
            "beta_MC": beta_mc,
            "sigma_P": sig_p,
            "sigma_beta": sig_beta,
            "rel_err_P": err_p,
            "rel_err_beta": err_beta
        })

    df = pd.DataFrame(results)

    print("Monte Carlo results:")
    print(df.to_string(index=False))
    print()

    # --- PLOTTING ---
    N = df["N_T"].to_numpy()
    Pmc = df["P_esc_MC"].to_numpy()
    Bmc = df["beta_MC"].to_numpy()
    sP = df["sigma_P"].to_numpy()
    sB = df["sigma_beta"].to_numpy()
    errP = df["rel_err_P"].to_numpy()

    P_lo, P_hi = p_an - 1.96 * sP, p_an + 1.96 * sP
    B_lo, B_hi = beta_an - 1.96 * sB, beta_an + 1.96 * sB

    # Figure 1: Convergence plots (P_esc and Beta)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    ax1.plot(N, Pmc, marker="o", linewidth=2, label="Monte Carlo")
    ax1.axhline(p_an, linestyle="--", color='r', linewidth=2, label=f"Analytical ({p_an:.4f})")
    ax1.fill_between(N, P_lo, P_hi, alpha=0.2, label="95% CI")
    ax1.set_xscale("log")
    ax1.set_xlabel("Number of particles $N_T$")
    ax1.set_ylabel("Escape probability $P_{esc}$")
    ax1.set_title("(a) $P_{esc}$ convergence")
    ax1.grid(True, which="both", alpha=0.4)
    ax1.legend()

    ax2.plot(N, Bmc, marker="s", linewidth=2, label="Monte Carlo")
    ax2.axhline(beta_an, linestyle="--", color='r', linewidth=2, label=f"Analytical ({beta_an:.4f})")
    ax2.fill_between(N, B_lo, B_hi, alpha=0.2, label="95% CI")
    ax2.set_xscale("log")
    ax2.set_xlabel("Number of particles $N_T$")
    ax2.set_ylabel("Blackness $\\beta$")
    ax2.set_title("(b) $\\beta$ convergence")
    ax2.grid(True, which="both", alpha=0.4)
    ax2.legend()

    plt.tight_layout()
    plt.savefig("convergence_plot.png")  # Saves this plot for README
    print("Graph saved as 'convergence_plot.png'")
    # plt.show() 

    # Figure 2: Relative error scaling
    plt.figure(figsize=(7.5, 5.5))
    plt.loglog(N, 100 * errP, marker="o", linewidth=2, label="Relative error (%)")
    ref = (100 * errP[0]) * np.sqrt(N[0] / N)
    plt.loglog(N, ref, linestyle=":", linewidth=2, label="$\\sim 1/\\sqrt{N_T}$")
    plt.xlabel("Number of particles $N_T$")
    plt.ylabel("Relative error (%)")
    plt.title("Relative error scaling")
    plt.grid(True, which="both", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    # plt.show()

    # Figure 3: Statistical uncertainty
    plt.figure(figsize=(7.5, 5.5))
    plt.loglog(N, sP, marker="d", linewidth=2, label="$\\sigma_P$")
    ref_s = sP[0] * np.sqrt(N[0] / N)
    plt.loglog(N, ref_s, linestyle=":", linewidth=2, label="$\\sim 1/\\sqrt{N_T}$")
    plt.xlabel("Number of particles $N_T$")
    plt.ylabel("Statistical uncertainty")
    plt.title("Uncertainty scaling")
    plt.grid(True, which="both", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    # plt.show()
