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
* Sampling Design: Two sampling designs and campaigns over multiple fields: (1) Random Sampling from k-means clustering based on digital soil maps, digital elevation model, air-borne gamma radiometric data and remote sensing satellite images, and (2) Stratified Random Sampling based on soil type and land use parameters
* Study Area Size: 1,158 ha
* Geological Setting: Alluvial deposits of basaltic sediments
* Previous Data Publication: None
* Contact Information:
    * Patrick Filippi (patrick.filippi@sydney.edu.au), University of Sydney
    * Edward Jones (edjones1684@gmail.com), University of Sydney
* License: CC BY-SA 4.0
* Publication/Modification Date (d/m/y): XXX.2025, version 1.0
* Changelog:
    * Version 0.1.0 (XXX.2025): Initial release

Details
-------

The dataset contains the following target soil properties and features:

Target Soil Properties:

SOC - Soil Organic Carbon
    * Code: SOC_target
    * Unit: %
    * Protocol: Measured through titration after oxidization of the organic carbon (Walkley & Black 1934)
    * Sampling Date: July 2018 & December 2018
    * Sampling Depth: 0 - 10 cm

pH
    * Code: pH_target
    * Unit: Unitless
    * Protocol: Measured in CaCl2 suspension with a glass electrode with a 5:1 liquid:soil volumetric ratio
    * Sampling Date: July 2018 & December 2018
    * Sampling Depth: 0 - 10 cm

Clay
    * Code: Clay_target
    * Unit: %
    * Protocol: Sieve-Pipette method, measured through fractioning the soil into the sand fractions by sieving, and the silt and clay fractions by sedimentation in water (Gee and Bauder 1986)
    * Sampling Date: July 2018 & December 2018
    * Sampling Depth: 0 - 10 cm

Groups of Features:

DEM – Digital Elevation Model and Terrain Parameters
    * Number Features: 2
    * Code(s): Altitude, Slope
    * Unit: Altitude in m, Slope in °
    * Sensing: Digital elevation model raster (5 m) based on LiDAR and photogrammetry from the "Elevation and Depth – Foundation Spatial Data (ELVIS)"
    * Processing: Calculating Slope with terrain function of the raster package, extracting DEM values from raster at soil sampling locations
    * Sampling Date: April 2016

RSS – Remote Sensing Derived Spectral Data
    * Number Features: 3
    * Code(s): B02, B8A, B11
    * Unit: Unitless
    * Sensing: Sentinel-2 bare soil Image (Level-2A) from "Copernicus Open Access Hub", with bands of 10 - 20 m spatial resolution
    * Processing: Extracting RSS values from raster at soil sampling locations, selecting bands spread throughout the spectral range with lower intercorrelation
    * Sampling Date: July 2018

Examples
--------

.. code-block:: python

    # Load and explore the dataset
    data = load_dataset("NSW.52")
    dataset = data["Dataset"]
    folds = data["Folds"]
    coords = data["Coordinates"]

    # Split into train/test using fold 1
    X_train, X_test, y_train, y_test = split_dataset(
        data=data,
        fold=1,
        targets=["pH_target", "SOC_target", "clay_target"]
    )

    # Calculate model performance
    predictions = model.predict(X_test)
    metrics = calculate_performance(y_test, predictions)
    print(f"R2: {metrics['r2']:.3f}, RMSE: {metrics['rmse']:.3f}")

    # Visualize soil properties
    soil_map = plot_soil_map(data, "pH_target", zoom_start=14)
    soil_map.save("NSW52_pH_map.html")

References
----------

Gee, G.W. & Bauder, J.W. (1986) Particle-Size Analysis. In: Klute, A., Ed., Methods of Soil Analysis, Part 1. Physical and Mineralogical Methods, Agronomy Monograph No. 9, 2nd Edition, American Society of Agronomy/Soil Science Society of America, Madison, WI, 383-411.

Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
