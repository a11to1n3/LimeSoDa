SP.231 Dataset
==============

Description
-----------


 \item Target Soil Properties: SOM, pH, Clay
 \item Groups of Features: vis-NIR
 \item Sample size: 231
 \item Number of Features: 271
 \item Coordinates: With coordinates (EPSG: 32654)
 \item Location: Saitama Prefecture, Japan
 \item Sampling Design: Two sampling designs over multiple fields depending on the soil conditions: (1) Systematic Sampling, in which samples are taken in the corners and middle of the field and (2) Fully Random Sampling
 \item Study Area Size: 3.1 ha
 \item Geological Setting: Silandic Andosols
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Masakazu Kodaira (kodaira@cc.tuat.ac.jp), Tokyo University of Agriculture and Technology

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
SP.231

# Access the dataset
SP.231$Dataset

# Access the folds
SP.231$Folds

# Access the coordinates
SP.231$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_SP.231 <- SP.231$Dataset[SP.231$Folds != 1,]
testing_data_SP.231 <- SP.231$Dataset[SP.231$Folds == 1,]

References
----------

Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
