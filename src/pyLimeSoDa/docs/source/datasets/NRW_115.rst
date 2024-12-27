NRW.115 Dataset
===============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: MIR
 \item Sample size: 115
 \item Number of Features: 1,686
 \item Coordinates: Without coordinates because of privacy concerns
 \item Location: North Rhine-Westphalia, Germany
 \item Sampling Design: Regular Grid Sampling on two adjacent fields in two sampling campaigns
 \item Study Area Size: 17 ha
 \item Geological Setting: Cretaceous marls partially covered by Saalian glacial till, aeolian sand and fluvial sediments
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Stefan Paetzold (s.paetzold@uni-bonn.de), University of Bonn

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
NRW.115

# Access the dataset
NRW.115$Dataset

# Access the folds
NRW.115$Folds

# Access the coordinates but empty for NRW.115 (i.e. NA)
NRW.115$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_NRW.115 <- NRW.115$Dataset[NRW.115$Folds != 1,]
testing_data_NRW.115 <- NRW.115$Dataset[NRW.115$Folds == 1,]

References
----------


