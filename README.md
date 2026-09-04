# 1D-London-Superconductor-Simulator
Interactive 1D London Equation Simulator for B and J fields using Matplotlib and Python
## Overview

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

This project requires **Python 3.x** and the following libraries:
* `numpy`
* `matplotlib`
* `PyQt5`
