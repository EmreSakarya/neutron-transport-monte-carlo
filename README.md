# Neutron Transport Monte Carlo Simulation (Slab Geometry)

![Language](https://img.shields.io/badge/language-Python-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ⚛️ Project Overview

This project investigates the neutron transport problem in a purely absorbing **slab geometry** (infinite plate). It calculates the **Escape Probability ($P_{esc}$)** and **Blackness ($\beta$)** of the slab using stochastic **Monte Carlo** simulations and compares the results with the exact analytical solution derived from exponential integral functions ($E_3$).

The study demonstrates the convergence of the Monte Carlo method as the number of simulated particles ($N$) increases from $10^2$ to $10^6$, confirming the $1/\sqrt{N}$ error scaling law.

### 🔬 Physics & Methodology
* **Geometry:** 1D Slab of thickness $H = 3.0$ cm.
* **Source:** Uniformly distributed isotropic neutron source inside the slab.
* **Interaction:** Pure absorption ($\Sigma_a = 0.5$ cm$^{-1}$).
* **Analytical Solution:** Based on the $E_3$ function:
$$P_{esc} = \frac{1 - 2E_3(\tau)}{2\tau}$$
* **Monte Carlo Method:**
  1.  Sample position $z$ uniformly in $[0, H]$.
  2.  Sample direction cosine $\mu$ uniformly in $[-1, 1]$.
  3.  Sample free path length from exponential distribution.
  4.  Check if particle reaches the boundary before absorption.

---

## 📊 Visuals & Results

The simulation tracks the convergence of the escape probability and blackness towards the analytical reference values.

![Convergence Plot](docs/convergence_plot.png)
*(Note: Upload the generated 'convergence_plot.png' to the docs/ folder)*

**Results Summary:**
| Particles ($N$) | $P_{MC}$ (Simulation) | Relative Error (%) |
| :--- | :--- | :--- |
| $10^2$ | 0.2900 | ~3.5% |
| $10^4$ | 0.3015 | ~0.3% |
| $10^6$ | 0.3005 | ~0.02% |

*Exact Analytical Value:* $P_{esc} \approx 0.3006$

---

## 📂 Project Structure

    neutron-transport-monte-carlo/
    ├── docs/
    │   ├── Montecarlo.pdf         # Detailed project report
    │   └── convergence_plot.png   # Convergence graph
    ├── src/
    │   └── monte_carlo_slab.py    # Simulation source code
    ├── requirements.txt           # Python dependencies
    └── README.md

---

## 🚀 How to Run

### Prerequisites
You need Python and the scientific computing stack installed.

    pip install -r requirements.txt

### Running the Simulation
    python src/monte_carlo_slab.py

This will print the comparison table to the console and save the convergence plots as an image file.

---

## 👨‍💻 Author

**Emre Sakarya**
* Hacettepe University, Department of Nuclear Engineering
* Project: NEM 394 Engineering Project II

---

*For detailed derivations of the exponential integral solution, please refer to the [Project Report](docs/Montecarlo.pdf).*
