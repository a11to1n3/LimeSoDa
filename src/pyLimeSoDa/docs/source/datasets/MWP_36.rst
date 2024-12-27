MWP.36 Dataset
==============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, RSS
 \item Sample size: 36
 \item Number of Features: 5
 \item Coordinates: With coordinates (EPSG: 32633)
 \item Location: Mecklenburg-Western Pomerania, Germany
 \item Sampling Design: Random Sampling along field transects
 \item Study Area Size: 18 ha
 \item Geological Setting: Pleistocene young morainic landscape of the Weichselian glaciation with predominantly glacial sands
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Alexander Steiger (alexander.steiger@uni-rostock.de), University of Rostock

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
MWP.36

# Access the dataset
MWP.36$Dataset

# Access the folds
MWP.36$Folds

# Access the coordinates
MWP.36$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_MWP.36 <- MWP.36$Dataset[MWP.36$Folds != 1,]
testing_data_MWP.36 <- MWP.36$Dataset[MWP.36$Folds == 1,]

References
----------

Gee, G.W. & Bauder, J.W. (1986) Particle-Size Analysis. In: Klute, A., Ed., Methods of Soil Analysis, Part 1. Physical and Mineralogical Methods, Agronomy Monograph No. 9, 2nd Edition, American Society of Agronomy/Soil Science Society of America, Madison, WI, 383-411.\cr
\cr
Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
