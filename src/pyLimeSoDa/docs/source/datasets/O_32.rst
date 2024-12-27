O.32 Dataset
============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: MIR
 \item Sample size: 32
 \item Number of Features: 1,637
 \item Coordinates: Without coordinates because of privacy concerns
 \item Location: Occitanie, France
 \item Sampling Design: Regular Grid Sampling
 \item Study Area Size: XXX [? What was the size of the study area?]
 \item Geological Setting: Pleistocene fluvial deposits and Miocene marine deposits
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Stefan Paetzold (s.paetzold@uni-bonn.de), University of Bonn

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
O.32

# Access the dataset
O.32$Dataset

# Access the folds
O.32$Folds

# Access the coordinates but empty for O.32 (i.e. NA)
O.32$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_O.32 <- O.32$Dataset[O.32$Folds != 1,]
testing_data_O.32 <- O.32$Dataset[O.32$Folds == 1,]

References
----------


