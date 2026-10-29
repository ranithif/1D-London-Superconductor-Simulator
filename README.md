# Interactive 1D Superconductor Simulation
Interactive 1D London Equation Simulator for B and J fields using Matplotlib and Python
## Overview
This project uses the London equations to model how a magnetic field and the associated screening current vary inside a simple 1D superconducting slab.

The model demonstrates the Meissner effect: when a superconductor is placed in an external magnetic field, the field does not remain uniform inside the material. Instead, it decreases exponentially over a characteristic distance called the London penetration depth.

The left graph, (B(x)), shows the magnetic field decreasing as it penetrates into the superconductor. The right graph, (J(x)), shows the corresponding screening current density required to produce this change in magnetic field.

The simulation allows the penetration depth to be varied interactively, making it possible to see how changing a material parameter affects the magnetic field and current distributions.

<img width="1013" height="559" alt="Screenshot 2026-09-07 at 12 20 35" src="https://github.com/user-attachments/assets/79fa995c-49ed-40fb-b832-6d6e24115761" />


## Equations
* **Magnetic Field $B(x)$:**
  $$B(x) = B_0 \frac{\cosh(x / \lambda_L)}{\cosh(d / 2\lambda_L)}$$

* **Current Density $J(x)$:**
  $$J(x) = -\frac{B_0}{\mu_0 \lambda_L} \frac{\sinh(x / \lambda_L)}{\cosh(d / 2\lambda_L)}$$
## How to Run
Clone this repository:
   ```bash
   git clone https://github.com/ranithif/1d-london-superconductor-simulator.git
   cd 1d-london-superconductor-simulator
```

This project requires **Python 3.x** and the following libraries:
* `numpy`
* `matplotlib`
* `PyQt5`
