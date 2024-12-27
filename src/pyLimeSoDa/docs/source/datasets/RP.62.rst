RP.62 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: ERa, Gamma, NIR, pH-ISE, VI
 \item Sample size: 62
 \item Number of Features: 1,410
 \item Coordinates: Without coordinates because of privacy concerns
 \item Location: Rhineland-Palatinate, Germany
 \item Sampling Design: Regular Grid Sampling
 \item Study Area Size: 3.3 ha
 \item Geological Setting: Pleistocene periglacial slope deposits consisting of Weichselian loess with variable amounts of weathered Devonian sand-, silt-, and claystones and scattered Tertiary basalt bombs
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Stefan Paetzold (s.paetzold@uni-bonn.de), University of Bonn
     \item Hamed Tavakoli (HTavakoli@atb-potsdam.de), Leibniz Institute for Agricultural Engineering and Bioeconomy (ATB)

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
RP.62

# Access the dataset
RP.62$Dataset

# Access the folds
RP.62$Folds

# Access the coordinates but empty for RP.62 (i.e. NA)
RP.62$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_RP.62 <- RP.62$Dataset[RP.62$Folds != 1,]
testing_data_RP.62 <- RP.62$Dataset[RP.62$Folds == 1,]

References
----------

Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
