Introduction
============

Purpose
-------

LimeSoDa aims to enable more reliable benchmarking and comparison of various modeling approaches in Digital Soil Mapping and Pedometrics by providing an open collection of multiple datasets. Currently, most benchmarking studies are based on a single dataset because there is a lack of open and easily usable datasets from a soil context.

Dataset Structure
-----------------

Each dataset in LimeSoDa is structured as follows:

-  **Dataset**: A pandas DataFrame containing:

   - Target soil properties (first 3 columns)
   - Features for modeling (remaining columns)

-  **Folds**: A numpy array with pre-defined folds for cross-validation

-  **Coordinates**: A pandas DataFrame with spatial coordinates (if available, else empty)

Target Soil Properties
----------------------

All datasets include the following target soil properties:

- Soil organic carbon (SOC) or soil organic matter (SOM)
- pH
- Clay content

Feature Groups
--------------

Datasets may include various feature groups such as:

- Capacitive soil moisture sensor (CSMoisture)
- Digital elevation model and terrain parameters (DEM)
- Apparent electrical resistivity (ERa)
- Gamma-ray activity (Gamma)
- Mid infrared spectroscopy (MIR)
- Near infrared spectroscopy (NIR)
- Ion selective electrodes for pH determination (pH-ISE)
- Remote sensing derived spectral data (RSS)
- X-ray fluorescence derived elemental concentrations (XRF)
- Vegetation Indices (VI)
- Visible- and near infrared spectroscopy (vis-NIR)
