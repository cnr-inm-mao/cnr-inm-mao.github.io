# Bio-Inspired Underwater Glider Dataset

## Overview

Benchmark dataset for dimensionality reduction and optimization of a bio-inspired autonomous underwater glider.

The dataset is designed to support **PME-based methods**, surrogate modeling, and multi-fidelity optimization workflows.

**DOI**: https://zenodo.org/records/18936594  
**Repository**: https://zenodo.org/records/18936594  

---

## Dataset Description

- **Number of configurations**: 16,385  
- **Design variables**: 32  
- **Sampling strategy**: Sobol sequence  
- **Geometry representation**: multi-section parametric model  
- **Discretization**: 784 spatial elements  

---

## Data Structure

The dataset follows a structured representation:

- **Geometry (D)**  
  3 × 784 matrix (spatial coordinates)

- **Design variables (U)**  
  32-dimensional parameter vector

- **Physics (optional)**  
  Pressure coefficient (Cp) distribution

- **Outputs**
  - Drag  
  - Lift  

---

## Simulation Setup

- Flow model: potential flow solver with viscous correction  
- Freestream velocity: 0.25 m/s  
- Angle of attack: 8°  
- Fluid density: 1030 kg/m³  

---

## Use Cases

- Dimensionality reduction (PME, PI-PME, PD-PME)  
- Surrogate-based optimization  
- Multi-fidelity modeling  
- Explainable design-space compression  

---

## Files

The dataset includes:

- `database.mat`  
- `range_design.mat`  
- metadata files  

---

## Reproducibility

The dataset is fully documented and directly usable within PME-toolkit workflows.
