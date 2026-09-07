# Interactive 1D Superconductor Simulation
Interactive 1D London Equation Simulator for B and J fields using Matplotlib and Python
## Overview
Superconductors refuse to let magnetic fields exist inside their bulk, so they use electric currents flowing along their surface to cancel the external field out. These are called screening currents.

The left graph $B(x)$, shows how far the magnetic field manages to leak into the slab before it dies to zero and the right graph $J(x)$ shows the screening currents running along the surface of the material that push the penetrating field out.

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
