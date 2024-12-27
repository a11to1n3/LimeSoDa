BB.30_2 Dataset
===============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, ERa, Gamma, RSS, VI
 \item Sample size: 30
 \item Number of Features: 13
 \item Coordinates: With coordinates (EPSG: 25833)
 \item Location: Brandenburg, Germany
 \item Sampling Design: Regular Grid Sampling
 \item Study Area Size: 1.4 ha
 \item Geological Setting: Pleistocene young morainic landscape of the Weichselian glaciation with predominantly glacial sand
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Pablo Rosso (Pablo.Rosso@zalf.de), Leibniz Centre for Agricultural Landscape Research (ZALF)
     \item Sebastian Vogel (SVogel@atb-potsdam.de), Leibniz Institute for Agricultural Engineering and Bioeconomy (ATB)

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
BB.30_2

# Access the dataset
BB.30_2$Dataset

# Access the folds
BB.30_2$Folds

# Access the coordinates
BB.30_2$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_BB.30_2 <- BB.30_2$Dataset[BB.30_2$Folds != 1,]
testing_data_BB.30_2 <- BB.30_2$Dataset[BB.30_2$Folds == 1,]

References
----------


