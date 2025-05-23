SSP.58 Dataset
=============

Description
-----------
* Target Soil Properties: SOC, pH, Clay
* Groups of Features: vis-NIR
* Sample size: 58
* Number of Features: 351
* Coordinates: Without coordinates because dataset was not georeferenced
* Location: State of Sao Paulo, Brazil
* Sampling Design: Stratified random sampling based on treatment doses of K₂O and CaO
* Study Area Size: 0.7 ha
* Geological Setting: Heavily weathered soils originating from diabase
* Previous Data Publication: Full dataset published in Tavares et al. (2022)
* Contact Information:
    * Tiago Rodrigues Tavares (tiagosrt@usp.br), University of Sao Paulo
    * José Paulo Molin (jpmolin@usp.br), University of Sao Paulo
* License: CC BY-SA 4.0
* Publication/Modification Date (d/m/y): 28.02.25, version 1.0
* Changelog:
    * Version 1.0 (28.02.25): Initial release
    * Version 1.1 (15.05.25): Unit bug fix for SOC

Details
-------

Dataset
^^^^^^^
The dataset contains the following target soil properties and features:

Target Soil Properties:
""""""""""""""""""""""

SOC - Soil Organic Carbon
    * Code: ``SOC_target``
    * Unit: g dm⁻³
    * Protocol: Measured through titration after oxidization of the organic carbon (Walkley & Black 1934)
    * Sampling Date: September 2015
    * Sampling Depth: 0 - 20 cm

pH
    * Code: ``pH_target``
    * Unit: Unitless
    * Protocol: Measured in CaCl₂ suspension with a glass electrode with a 2.5:1 liquid:soil volumetric ratio
    * Sampling Date: September 2015
    * Sampling Depth: 0 - 20 cm

Clay
    * Code: ``Clay_target``
    * Unit: g dm⁻³
    * Protocol: Hydrometer method, measured through fractioning the soil into the sand fractions by sieving, and the silt and clay fractions by measuring suspension density using a hydrometer (Bouyoucos 1927)
    * Sampling Date: September 2015
    * Sampling Depth: 0 - 20 cm

Groups of Features:
"""""""""""""""""

vis-NIR – Visible and Near Infrared Spectroscopy
    * Number of Features: 351
    * Code(s): ``wl_431.6``, ``wl_437.4``, ``wl_449.1`` ... ``wl_2153.1``
    * Unit: % (Reflectance)
    * Sensing: vis-NIR spectrometer of former Veris MSP3 (Veris Technologies, Salina, Kansas, USA) which is based on two spectrometers (USB4000, Ocean optics, Largo, FL, USA) for the visible region and (C9914GB, Hamamatsu Photonics, Hamamatsu, Japan) for the NIR region, on dried and sieved samples (<2 mm) in the laboratory, spectral range was 343 - 2,200 nm at ~5 nm intervals
    * Processing: Discarding noisy edges of the spectrum (343 - 431.6 nm & 2,153.1 - 2,200 nm)
    * Sampling Date: September 2015
    * Spectral Information (After Data Processing):
        * Data Representation: Wavelength (in nm)
        * Spectral Resolution: ~5 nm
        * Spectral Range: 431.6 - 2,153.1 nm

Examples
--------

.. code-block:: python

    from LimeSoDa import load_dataset, split_dataset
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score, mean_squared_error
    import numpy as np

    # Load and explore the dataset
    data = load_dataset("SSP.58")
    dataset = data["Dataset"]
    folds = data["Folds"]
    coords = data["Coordinates"]  # Note: No coordinates available

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

Bouyoucos, G. J. (1927). The hydrometer as a new method for the mechanical analysis of soils. Soil science, 23(5), 343-354.

Tavares, T. R., Molin, J. P., Nunes, L. C., Alves, E. E. N., Krug, F. J., & de Carvalho, H. W. P. (2022). Spectral data of tropical soils using dry-chemistry techniques (VNIR, XRF, and LIBS): A dataset for soil fertility prediction. Data in Brief, 41, 108004.

Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
