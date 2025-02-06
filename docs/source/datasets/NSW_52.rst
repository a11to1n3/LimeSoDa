NSW.52 Dataset
=============

Description
-----------

* Target Soil Properties: SOC, pH, Clay
* Groups of Features: DEM, RSS 
* Sample size: 52
* Number of Features: 5
* Coordinates: With coordinates (EPSG: 32755)
* Location: New South Wales, Australia
* Sampling Design: Two sampling designs and campaigns over multiple fields: (1) random sampling from k-means clustering based on digital soil maps, digital elevation model, air-borne gamma radiometric data and remote sensing satellite images, and (2) stratified random sampling based on soil type and land use parameters
* Study Area Size: 1,158 ha
* Geological Setting: Alluvial deposits of basaltic sediments
* Previous Data Publication: None
* Contact Information:
    * Patrick Filippi (patrick.filippi@sydney.edu.au), University of Sydney
    * Edward Jones (edjones1684@gmail.com), University of Sydney
* License: CC BY-SA 4.0
* Publication/Modification Date (d/m/y): XXX.03.2025, version 1.0
* Changelog:
    * Version 1.0 (XXX.03.2025): Initial release

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
    * Sampling Date: July 2018 and December 2018
    * Sampling Depth: 0 - 10 cm

pH
    * Code: ``pH_target``
    * Unit: Unitless
    * Protocol: Measured in CaCl₂ suspension with a glass electrode with a 5:1 liquid:soil volumetric ratio
    * Sampling Date: July 2018 and December 2018
    * Sampling Depth: 0 - 10 cm

Clay
    * Code: ``Clay_target``
    * Unit: %
    * Protocol: Hydrometer method; separation of the fractions by sieving and sedimentation. Measurement of the separated fractions by weighing the density of the suspension (Gee and Bauder 1979)
    * Sampling Date: July 2018 and December 2018
    * Sampling Depth: 0 - 10 cm

Groups of Features:
"""""""""""""""""

DEM – Digital Elevation Model and Terrain Parameters
    * Number Features: 2
    * Code(s): ``Altitude``, ``Slope``
    * Unit: ``Altitude`` in m, ``Slope`` in °
    * Sensing: Digital elevation model raster (5 m) based on LiDAR and photogrammetry from the "Elevation and Depth – Foundation Spatial Data (ELVIS)"
    * Processing: Calculating ``Slope`` with ``terrain`` function of the raster R-package, extracting DEM values from raster at soil sampling locations
    * Sampling Date: April 2016

RSS – Remote Sensing Derived Spectral Data
    * Number Features: 3
    * Code(s): ``B02``, ``B8A``, ``B11``
    * Unit: Unitless
    * Sensing: Sentinel-2 bare soil image (Level-2A) from "Copernicus Open Access Hub", with bands of 10 - 20 m spatial resolution
    * Processing: Extracting RSS values from raster at soil sampling locations, selecting bands spread throughout the spectral range with lower intercorrelation due to low sample size
    * Sampling Date: July 2018

Examples
--------

.. code-block:: python

    from LimeSoDa import load_dataset, split_dataset
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score, mean_squared_error
    import numpy as np

    # Load and explore the dataset
    data = load_dataset("NSW.52")
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

Gee, G. W., & Bauder, J. W. (1979). Particle size analysis by hydrometer: a simplified method for routine textural analysis and a sensitivity test of measurement parameters. Soil Science Society of America Journal, 43(5), 1004-1007.

Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
