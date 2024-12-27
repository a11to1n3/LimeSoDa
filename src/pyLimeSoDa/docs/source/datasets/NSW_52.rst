NSW.52 Dataset
==============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, RSS
 \item Sample size: 52
 \item Number of Features: 5
 \item Coordinates: With coordinates (EPSG: 32755)
 \item Location: New South Wales, Australia
 \item Sampling Design: Two sampling designs and campaigns over multiple fields: (1) Random Sampling from k-means clustering based on digital soil maps, digital elevation model, air-borne gamma radiometric data and remote sensing satellite images, and (2) Stratified Random Sampling based on soil type and land use parameters
 \item Study Area Size: 1,158 ha
 \item Geological Setting: Alluvial deposits of basaltic sediments
 \item Previous Data Publication: None
 \item Contact Information:
    
     \item Patrick Filippi (patrick.filippi@sydney.edu.au), University of Sydney
     \item Edward Jones (edjones1684@gmail.com), University of Sydney

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
NSW.52

# Access the dataset
NSW.52$Dataset

# Access the folds
NSW.52$Folds

# Access the coordinates
NSW.52$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_NSW.52 <- NSW.52$Dataset[NSW.52$Folds != 1,]
testing_data_NSW.52 <- NSW.52$Dataset[NSW.52$Folds == 1,]

References
----------

Gee, G.W. & Bauder, J.W. (1986) Particle-Size Analysis. In: Klute, A., Ed., Methods of Soil Analysis, Part 1. Physical and Mineralogical Methods, Agronomy Monograph No. 9, 2nd Edition, American Society of Agronomy/Soil Science Society of America, Madison, WI, 383-411.\cr
\cr
Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
