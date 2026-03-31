# RAE2822 Airfoil Dataset

## Overview

Benchmark dataset for aerodynamic shape optimization and dimensionality reduction based on the RAE2822 airfoil.

**DOI**: [https://zenodo.org/records/18958555](https://zenodo.org/records/18958555)

<div style="text-align:center; margin:1.5rem 0;">
  <video width="600" autoplay loop muted playsinline>
    <source src="../../assets/videos/rae_samples.mp4" type="video/mp4">
  </video>
</div>  

---

## Dataset Description

- **Number of configurations**: 16,385  
- **Design variables**: 20  
- **Parameterization**: basis function expansion  
- **Discretization**: 129 surface points  

---

## Data Structure

- **Geometry (D)**  
  Airfoil coordinates (x, y)

- **Design variables (U)**  
  20 parameters in normalized range [0,1]

- **Physics**
  - Pressure coefficient (Cp)

- **Outputs**
  - Lift coefficient (Cl)  
  - Drag coefficient (Cd)  
  - Moment coefficient (Cm)  

---

## Simulation Setup

- Solver: XFOIL  
- Mach number: 0.4  
- Reynolds number: 6.5 × 10⁶  
- Angle of attack: 0°  

---

## Use Cases

- Benchmarking dimensionality reduction methods  
- Surrogate model validation  
- Aerodynamic optimization  

---

## Files

- `database.mat`  
- metadata and documentation files  

---

## Reproducibility

All configurations are pre-validated (no NaNs) and suitable for benchmarking studies.
