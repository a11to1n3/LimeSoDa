SC.50 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, ERa
 \item Sample size: 50
 \item Number of Features: 3
 \item Coordinates: With coordinates (EPSG: 32722)
 \item Location: Santa Catarina, Brazil
 \item Sampling Design: Regular Grid Sampling
 \item Study Area Size: 13 ha
 \item Geological Setting: Heavily weathered soils originating from Mesozoic basalt rocks
 \item Previous Data Publication: Full dataset published in Bottega & Safanelli (2024)
 \item Contact Information:
   
     \item Eduardo Bottega (bottega.elb@gmail.com), Federal University of Santa Maria
     \item José Lucas Safanelli (jsafanelli@woodwellclimate.org), Woodwell Climate Research Center

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
SC.50

# Access the dataset
SC.50$Dataset

# Access the folds
SC.50$Folds

# Access the coordinates
SC.50$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_SC.50 <- SC.50$Dataset[SC.50$Folds != 1,]
testing_data_SC.50 <- SC.50$Dataset[SC.50$Folds == 1,]

References
----------

Bottega, E. L. & Safanelli J. L. (2024). Data for "Site-Specific Management Zones Delineation Based on Apparent Soil Electrical Conductivity in Two Contrasting Fields of Southern Brazil". Zenodo repository.  https://doi.org/10.5281/zenodo.13770031 \cr
\cr
Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
