# PME-toolkit

<div style="text-align:left; margin-bottom:1rem;">
  <a href="https://github.com/cnr-inm-mao/pme-toolkit">
    <img src="../../assets/logos/logo-pmetk.png" width="240">
  </a>
</div>

## Overview

PME-toolkit is an open-source framework for **design-space dimensionality reduction** based on the Parametric Model Embedding (PME) methodology and its physics-aware extensions.

The toolkit supports reproducible workflows for engineering design optimization and reduced-order modeling.

---

## Key Features

- reduced-order representation of design spaces  
- analytical backmapping to original variables  
- support for physics-informed (PI-PME) and physics-driven (PD-PME) variants  
- unified MATLAB and Python implementations  
- standardized input/output configuration (JSON-based workflows)  

<p style="text-align:center; margin-bottom:0.5rem; font-size:0.9rem; opacity:0.8;">
  <em>
    Example of first three PI-PME modes 
    <a href="../../datasets/dr_glider/">(glider dataset)</a>
  </em>
</p>
<div style="display:flex; gap:1rem; justify-content:center; align-items:flex-start; flex-wrap:wrap; margin:1.5rem 0;">

  <div style="text-align:center; width:220px;">
    <video autoplay loop muted playsinline style="width:220px; max-width:100%; border-radius:8px;">
      <source src="../../assets/videos/aug_mode1.mp4" type="video/mp4">
    </video>
    <p style="margin-top:0.3rem; font-size:0.9rem; opacity:0.7;">Mode 1</p>
  </div>

  <div style="text-align:center; width:220px;">
    <video autoplay loop muted playsinline style="width:220px; max-width:100%; border-radius:8px;">
      <source src="../../assets/videos/aug_mode2.mp4" type="video/mp4">
    </video>
    <p style="margin-top:0.3rem; font-size:0.9rem; opacity:0.7;">Mode 2</p>
  </div>

  <div style="text-align:center; width:220px;">
    <video autoplay loop muted playsinline style="width:220px; max-width:100%; border-radius:8px;">
      <source src="../../assets/videos/aug_mode3.mp4" type="video/mp4">
    </video>
    <p style="margin-top:0.3rem; font-size:0.9rem; opacity:0.7;">Mode 3</p>
  </div>

</div>

---

## Capabilities

PME-toolkit enables:

- dimensionality reduction of high-dimensional design spaces  
- integration of geometry, design variables, and physics  
- explainable surrogate-based optimization  
- reproducible benchmarking workflows  

---

## Resources

- 🔗 [GitHub Repository](https://github.com/cnr-inm-mao/pme-toolkit)  
- 📖 [Documentation](https://cnr-inm-mao.github.io/pme-toolkit/)  
- 📦 [PyPI](https://pypi.org/project/pme-toolkit/)  
- 📄 [Zenodo](https://zenodo.org/records/19068340)  
- 📝 JOSS submission: under review  

---

## Related Datasets

PME-toolkit is designed to work with benchmark datasets available in this repository:

- Bio-inspired underwater glider  
- RAE2822 airfoil  

👉 See [Datasets](../datasets/index.md)

---

## Citation

If you use PME-toolkit in your research, please cite the associated publication (JOSS or related articles).

---

## Development Status

- actively developed  
- tested on benchmark datasets  
- aligned MATLAB/Python implementations  
