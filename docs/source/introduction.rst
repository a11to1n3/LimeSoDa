Introduction
============

Purpose
-------

pyLimeSoDa aims to enable more reliable benchmarking and comparison of various modeling approaches in Digital Soil Mapping and Pedometrics by providing an open collection of multiple datasets.

Background
----------

Precision liming requires accurate soil property maps. This package provides datasets that can be used to develop and test mapping algorithms for key soil properties related to liming decisions.

Dataset Structure
-----------------

Each dataset in pyLimeSoDa is structured as follows:

1. **Dataset**: A pandas DataFrame containing:
   
   - Target soil properties (first 3 columns)
   - Features for modeling (remaining columns)

2. **Folds**: A numpy array with pre-defined folds for cross-validation

3. **Coordinates**: A pandas DataFrame with spatial coordinates (if available)

Target Soil Properties
----------------------

All datasets include the following target soil properties:

1. Soil Organic Carbon (SOC) or Soil Organic Matter (SOM)
2. pH
3. Clay content

Feature Groups
--------------

Datasets may include various feature groups such as:

- DEM (Digital Elevation Model)
- ERa (Apparent Electrical Resistivity)
- Gamma (Gamma-ray activity)
- vis-NIR (Visible and Near-Infrared Spectroscopy)
- MIR (Mid-Infrared Spectroscopy)
- RSS (Remote Sensing Spectral data)
- VI (Vegetation Indices)
- And more...