NRW.62 Dataset
==============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: MIR
 \item Sample size: 62
 \item Number of Features: 1,686
 \item Coordinates: Without coordinates because of privacy concerns
 \item Location: North Rhine-Westphalia, Germany
 \item Sampling Design: Stratified Systematic Sampling by sampling rectangular plots which received different fertilizer dosages, samples were taken in the center of the plots
 \item Study Area Size: 0.6 ha
 \item Geological Setting: Pleistocene periglacial slope deposits consisting of weathered sand- and claystones from the Upper Bunter sandstone
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Stefan Paetzold (s.paetzold@uni-bonn.de), University of Bonn

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
NRW.62

# Access the dataset
NRW.62$Dataset

# Access the folds
NRW.62$Folds

# Access the coordinates but empty for NRW.62 (i.e. NA)
NRW.62$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_NRW.62 <- NRW.62$Dataset[NRW.62$Folds != 1,]
testing_data_NRW.62 <- NRW.62$Dataset[NRW.62$Folds == 1,]

References
----------


