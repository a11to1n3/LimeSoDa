MGS.101 Dataset
===============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, RSS, VI
 \item Sample size: 101
 \item Number of Features: 16
 \item Coordinates: With coordinates (EPSG: 32721)
 \item Location: Mato Grosso do Sul, Brazil
 \item Sampling Design: Regular Grid Sampling
 \item Study Area Size: 95 ha
 \item Geological Setting: Heavily weathered soils originating from Andesitic Basalt
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Domingos Sarvio Magalhaes Valente (valente@ufv.br), Federal University of Vicosa

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
MGS.101

# Access the dataset
MGS.101$Dataset

# Access the folds
MGS.101$Folds

# Access the coordinates
MGS.101$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_MGS.101 <- MGS.101$Dataset[MGS.101$Folds != 1,]
testing_data_MGS.101 <- MGS.101$Dataset[MGS.101$Folds == 1,]

References
----------

Gee, G.W. & Bauder, J.W. (1986) Particle-Size Analysis. In: Klute, A., Ed., Methods of Soil Analysis, Part 1. Physical and Mineralogical Methods, Agronomy Monograph No. 9, 2nd Edition, American Society of Agronomy/Soil Science Society of America, Madison, WI, 383-411.\cr
\cr
Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
