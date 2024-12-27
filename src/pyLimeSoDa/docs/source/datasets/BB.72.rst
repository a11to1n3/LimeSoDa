BB.72 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, ERa, Gamma, pH-ISE, RSS, VI
 \item Sample size: 72
 \item Number of Features: 17
 \item Coordinates: With coordinates (EPSG: 25833)
 \item Location: Brandenburg, Germany
 \item Sampling Design: Regular Grid Sampling
 \item Study Area Size: 3.4 ha
 \item Geological Setting: Pleistocene young morainic landscape of the Weichselian glaciation with predominantly glacial sand
 \item Previous Data Publication: Target soil properties published but under boycott in Vogel et al. 2022
 \item Contact Information:
   
     \item Sebastian Vogel (SVogel@atb-potsdam.de), Leibniz Institute for Agricultural Engineering and Bioeconomy (ATB)
     \item Jörg Rühlmann (ruehlmann@igzev.de), Leibniz Institute of Vegetable and Ornamental Crops (IGZ)

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
BB.72

# Access the dataset
BB.72$Dataset

# Access the folds
BB.72$Folds

# Access the coordinates
BB.72$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_BB.72 <- BB.72$Dataset[BB.72$Folds != 1,]
testing_data_BB.72 <- BB.72$Dataset[BB.72$Folds == 1,]

References
----------

Vogel S., Bönecke E., Kling C., Kramer E., Lück K., Nagel A., Philipp G., Rühlmann J., Schröter I. & Gebbers, R. (2022), Base neutralizing capacity from agricultural fields in the quaternary landscape of North-East Germany, BONARES Repository, https://doi.org/10.20387/bonares-zh3x-nd80
