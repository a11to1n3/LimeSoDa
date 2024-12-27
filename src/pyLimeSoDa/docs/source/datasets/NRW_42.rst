NRW.42 Dataset
==============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: MIR
 \item Sample size: 42
 \item Number of Features: 1,686
 \item Coordinates: Without coordinates because of privacy concerns
 \item Location: North Rhine-Westphalia, Germany
 \item Sampling Design: Regular Grid Sampling
 \item Study Area Size: 1.5 ha
 \item Geological Setting: Pleistocene periglacial slope deposits consisting of weathered Devonian sand-, silt-, & claystones, partially covered by Weichselian loess
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Stefan Paetzold (s.paetzold@uni-bonn.de), University of Bonn

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
NRW.42

# Access the dataset
NRW.42$Dataset

# Access the folds
NRW.42$Folds

# Access the coordinates but empty for NRW.42 (i.e. NA)
NRW.42$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_NRW.42 <- NRW.42$Dataset[NRW.42$Folds != 1,]
testing_data_NRW.42 <- NRW.42$Dataset[NRW.42$Folds == 1,]

References
----------


