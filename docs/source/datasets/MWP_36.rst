MWP.36 Dataset
=============

Description
-----------

* Target Soil Properties: SOC, pH, Clay
* Groups of Features: DEM, RSS 
* Sample size: 36
* Number of Features: 5
* Coordinates: With coordinates (EPSG: 32633)
* Location: Mecklenburg-Western Pomerania, Germany
* Sampling Design: Simple random sampling along field transects
* Study Area Size: 18 ha
* Geological Setting: Pleistocene young morainic landscape of the Weichselian glaciation with predominantly glacial sand
* Previous Data Publication: None
* Contact Information:
    * Alexander Steiger (alexander.steiger@uni-rostock.de), University of Rostock
* License: CC BY-SA 4.0
* Publication/Modification Date (d/m/y): 28.02.25, version 1.0
* Changelog:
    * Version 1.0 (28.02.25): Initial release

Details
-------

Dataset
^^^^^^^
The dataset contains the following target soil properties and features:

Target Soil Properties:
""""""""""""""""""""""

SOC - Soil Organic Carbon
    * Code: ``SOC_target``
    * Unit: %
    * Protocol: Measured through titration after oxidization of the organic carbon (Walkley & Black 1934)
    * Sampling Date: August 2022
    * Sampling Depth: 0 – 15 cm

pH
    * Code: ``pH_target``
    * Unit: Unitless
    * Protocol: Measured in CaCl₂ suspension with a glass electrode with a 5:1 liquid:soil volumetric ratio (DIN ISO 10390)
    * Sampling Date: August 2022
    * Sampling Depth: 0 – 15 cm

Clay
    * Code: ``Clay_target``
    * Unit: %
    * Protocol: Sieve-Pipette method, measured through fractioning the soil into the sand fractions by sieving, and the silt and clay fractions by sedimentation in water (Gee and Bauder 1986)
    * Sampling Date: August 2022
    * Sampling Depth: 0 – 15 cm

Groups of Features:
"""""""""""""""""

DEM – Digital Elevation Model and Terrain Parameters
    * Number of Features: 2
    * Code(s): ``Altitude``, ``Slope``
    * Unit: ``Altitude`` in m, ``Slope`` in °
    * Sensing: Digital elevation model raster (5 m) based on LiDAR and photogrammetry from "LAiV Geodaten-MV"
    * Processing: Calculating ``Slope`` with ``terrain`` function of the raster R-package, extracting DEM values from raster at soil sampling locations
    * Sampling Date: Unknown

RSS – Remote Sensing Derived Spectral Data
    * Number of Features: 3
    * Code(s): ``B02``, ``B8A``, ``B11``
    * Unit: Unitless
    * Sensing: Sentinel-2 bare soil image (Level-2A) from "Copernicus Open Access Hub", with bands of 10 - 20 m spatial resolution
    * Processing: Extracting RSS values from raster at soil sampling locations, selecting bands spread throughout the spectral range with lower intercorrelation due to low sample size
    * Sampling Date: August 2022

Examples
--------

.. code-block:: python

    from LimeSoDa import load_dataset, split_dataset
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score, mean_squared_error
    import numpy as np

    # Load and explore the dataset
    data = load_dataset("MWP.36")
    dataset = data["Dataset"]
    folds = data["Folds"]
    coords = data["Coordinates"]

    # Split into train/test using fold 1
    X_train, X_test, y_train, y_test = split_dataset(
        data=data,
        fold=1,
        targets=["pH_target", "SOC_target", "Clay_target"]
    )

    # Fit model and get predictions
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # Calculate performance metrics
    r2 = r2_score(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    print(f"R-squared: {r2:.7f}")
    print(f"RMSE: {rmse:.7f}")

References
----------

Gee, G.W. & Bauder, J.W. (1986) Particle-Size Analysis. In: Klute, A., Ed., Methods of Soil Analysis, Part 1. Physical and Mineralogical Methods, Agronomy Monograph No. 9, 2nd Edition, American Society of Agronomy/Soil Science Society of America, Madison, WI, 383-411.

Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
