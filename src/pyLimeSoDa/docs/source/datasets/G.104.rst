G.104 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, RSS, VI
 \item Sample size: 104
 \item Number of Features: 16
 \item Coordinates: With coordinates (EPSG: 32722)
 \item Location: Goias, Brazil
 \item Sampling Design: Regular Grid Sampling
 \item Study Area Size: 95 ha
 \item Geological Setting: Heavily weathered soils originating from sedimentary rocks (Claystone, Sandstone)
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Domingos Sarvio Magalhaes Valente (valente@ufv.br), Federal University of Vicosa

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
G.104

# Access the dataset
G.104$Dataset

# Access the folds
G.104$Folds

# Access the coordinates
G.104$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_G.104 <- G.104$Dataset[G.104$Folds != 1,]
testing_data_G.104 <- G.104$Dataset[G.104$Folds == 1,]

References
----------

Gee, G.W. & Bauder, J.W. (1986) Particle-Size Analysis. In: Klute, A., Ed., Methods of Soil Analysis, Part 1. Physical and Mineralogical Methods, Agronomy Monograph No. 9, 2nd Edition, American Society of Agronomy/Soil Science Society of America, Madison, WI, 383-411.\cr
\cr
Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
