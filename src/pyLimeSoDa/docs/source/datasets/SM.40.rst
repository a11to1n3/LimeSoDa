SM.40 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, ERa
 \item Sample size: 40
 \item Number of Features: 3
 \item Coordinates: With coordinates (EPSG: 32633)
 \item Location: South Moravia, Czechia
 \item Sampling Design: Stratified Sampling from previous Regular Grid Sampling, stratification was handpicked to cover contrasting areas
 \item Study Area Size: 53 ha
 \item Geological Setting: Weichselian sandy loess [? Eventually wrong ?]
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Vojtech Lukas (vojtech.lukas@mendelu.cz), Mendel University in Brno

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
SM.40

# Access the dataset
SM.40$Dataset

# Access the folds
SM.40$Folds

# Access the coordinates
SM.40$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_SM.40 <- SM.40$Dataset[SM.40$Folds != 1,]
testing_data_SM.40 <- SM.40$Dataset[SM.40$Folds == 1,]

References
----------

Bouyoucos, G. J. (1927). The hydrometer as a new method for the mechanical analysis of soils. Soil science, 23(5), 343-354.\cr
\cr
Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38. \cr
\cr
Zbíral, J., Honsa, I., Malý, S. & Čižmář, D (2004). Analýza půd III : jednotné pracovní postupy [Soil Analysis III : Unified working procedures]. Brno: UKZUZ, 199\cr
\cr
Zbíral, J. (2002). Analýza půd I : jednotné pracovní postupy [Soil analysis I: Integrated work procedures]. Brno: UKZUZ, 197
