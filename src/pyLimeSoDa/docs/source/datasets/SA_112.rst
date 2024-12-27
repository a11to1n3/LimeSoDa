SA.112 Dataset
==============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, ERa, Gamma, NIR, pH-ISE, VI
 \item Sample size: 112
 \item Number of Features: 1,412
 \item Coordinates: Without coordinates because of privacy concerns
 \item Location: Saxony-Anhalt, Germany
 \item Sampling Design: Regular Grid Sampling but with missing values in the center of the field
 \item Study Area Size: 27 ha
 \item Previous Data Publication: None
 \item Geological Setting: Weichselian loess
 \item Contact Information:
   
     \item Stefan Paetzold (s.paetzold@uni-bonn.de), University of Bonn
     \item Hamed Tavakoli (HTavakoli@atb-potsdam.de), Leibniz Institute for Agricultural Engineering and Bioeconomy (ATB)

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
SA.112

# Access the dataset
SA.112$Dataset

# Access the folds
SA.112$Folds

# Access the coordinates but empty for SA.112 (i.e. NA)
SA.112$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_SA.112 <- SA.112$Dataset[SA.112$Folds != 1,]
testing_data_SA.112 <- SA.112$Dataset[SA.112$Folds == 1,]

References
----------


