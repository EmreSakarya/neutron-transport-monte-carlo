# Neutron Transport Monte Carlo Simulation (Slab Geometry)

![Language](https://img.shields.io/badge/language-Python-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ⚛️ Project Overview

This project investigates the neutron transport problem in a purely absorbing **slab geometry** (infinite plate) with thickness $H=3.0$ and absorption cross-section $\Sigma_a=0.5$.

It calculates the **Escape Probability ($P_{esc}$)** and **Blackness ($\beta$)** using stochastic **Monte Carlo** simulations ($N=10^2, 10^4, 10^6$) and compares them with the exact **Analytical Solution** derived from exponential integral functions ($E_3$).

### 🔬 Physics & Methodology
* **Geometry:** 1D Slab, Thickness $H = 3.0$ cm.
* **Source:** Uniformly distributed isotropic neutron source.
* **Analytical Solution:**
  $$P_{esc} = \frac{1 - 2E_3(\tau)}{2\tau}, \quad \beta = \Sigma_a (2H) P_{esc}$$
  where $\tau = \Sigma_a H = 1.5$ (Optical Thickness).

---

## 📊 Visuals & Results

The simulation results converge to the exact analytical values as the number of particles increases. The plot below shows the convergence of the Escape Probability with the 95% confidence interval shaded.

![Convergence Plot](docs/fig1_convergence.png)

### Results Summary
Comparison of Monte Carlo results with the Analytical Reference ($P_{esc} \approx 0.2955$).

| Particles ($N$) | $P_{MC}$ (Simulation) | Relative Error (%) |
| :--- | :--- | :--- |
| $10^2$ | 0.2400 | ~18.8% |
| $10^4$ | 0.2922 | ~1.12% |
| $10^6$ | 0.2965 | ~0.35% |

*Exact Analytical Value:* $P_{esc} = 0.295507$

---

## 📂 Project Structure

    neutron-transport-monte-carlo/
    ├── docs/
    │   ├── Montecarlo.pdf         # Detailed project report
    │   └── fig1_convergence.png   # Convergence graph
    ├── src/
    │   └── monte_carlo_slab.py    # Main simulation code
    ├── requirements.txt           # Python dependencies
    └── README.md

---

## 🚀 How to Run

### Prerequisites
    pip install -r requirements.txt

### Running the Simulation
    python src/monte_carlo_slab.py

This script will:
1. Calculate the exact analytical values.
2. Run Monte Carlo simulations for $N=10^2, 10^4, 10^6$.
3. Print the comparison table to the console.
4. Save the convergence plot to the `docs/` folder.

---

## 👨‍💻 Author

**Emre Sakarya**
* Hacettepe University, Department of Nuclear Engineering
* Project: NEM 394 Engineering Project II

---

*For detailed physics and derivations, please refer to the [Project Report](docs/Montecarlo.pdf).*
