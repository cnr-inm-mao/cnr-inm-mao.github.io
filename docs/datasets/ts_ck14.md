# CK14-e ASV Experimental Time-Series Dataset

## Overview

Experimental dataset collected during a campaign conducted at the CNR-INM "Emilio Castagneto" towing tank (Rome) on the Codevintec CK14-e autonomous surface vehicle (ASV).

The dataset includes **raw and processed time-series data**, as well as synchronized experimental videos.

**DOI**: [https://zenodo.org/records/17315035](https://zenodo.org/records/17315035)  

---

## Experimental Setup

Experiments were conducted in the CNR-INM towing tank using a **moored configuration** of the CK14-e ASV.

Test conditions include:

- **Irregular waves**
  - Pierson–Moskowitz spectrum  

- **Regular waves**
  - wavelength ratios: λ/L = 1, 1.5, 2, 3  

---

## Dataset Content

The dataset is organized into three main components:

---

### 🎥 Raw Video Data

File: `ck14gopro_videos.zip`

Contains GoPro Hero 7 recordings of the experiments:

- `c15.cam0.avi`, `GH010194.mp4`, `GH010195.mp4`  
  → moored tests in irregular waves (Pierson–Moskowitz)

- `GH010196.mp4`  
  → moored tests in regular waves (λ/L = 1, 1.5, 2, 3)

---

### 📡 Raw Sensor Data

File: `ck14rawdata.zip`

Includes measurements from onboard sensors and wave probes:

- `250307_IRR_ss7_PM_moored_*`  
  → irregular wave tests (Pierson–Moskowitz)

- `250307_REG_WP_PM_moored_1`  
  → regular wave tests (λ/L = 1, 1.5, 2, 3)

- `250307_ZERO_*`  
  → calibration data for wave probes  

---

### 📊 Post-Processed Data

File: `ck14postprocessed.zip`

Processed datasets ready for analysis:

- `ck14pp_c15_1`, `ck14pp_c16_1`, `ck14pp_c17_1`  
  → irregular wave tests  

- `ck14pp_c18_1`, `ck14pp_c18_2`, `ck14pp_c18_3`, `ck14pp_c18_4`  
  → regular wave tests (λ/L = 1, 1.5, 2, 3)

---

## Data Characteristics

- Time-series signals from onboard instrumentation  
- Wave elevation measurements  
- Synchronized experimental video recordings  
- Calibration datasets for probe correction  

---

## Use Cases

- System identification  
- Time-series modeling  
- Validation of numerical solvers  
- Machine learning for dynamical systems  
- Experimental benchmarking  

---

## Reproducibility

The dataset includes:

- raw measurements  
- processed signals  
- calibration data  

enabling reproducible analysis workflows and validation studies.
