BB.30_1 Dataset
===============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, ERa, pH-ISE. VI
 \item Sample size: 30
 \item Number of Features: 8
 \item Coordinates: With coordinates (EPSG: 25833)
 \item Location: Brandenburg, Germany
 \item Sampling Design: Multi Criteria Sampling (Bönecke et al. 2021) based on quantile coverage of the sensing-features (ERa and pH-ISE), clustering of large and low values of sensing-features and spatial coverage
 \item Study Area Size: 19 ha
 \item Geological Setting: Pleistocene young morainic landscape of the Weichselian glaciation with predominantly glacial sand
 \item Previous Data Publication: Target soil properties published but under boycott in Vogel et al. 2022
 \item Contact Information:
   
     \item Sebastian Vogel (SVogel@atb-potsdam.de), Leibniz Institute for Agricultural Engineering and Bioeconomy (ATB)

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
BB.30_1

# Access the dataset
BB.30_1$Dataset

# Access the folds
BB.30_1$Folds

# Access the coordinates
BB.30_1$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_BB.30_1 <- BB.30_1$Dataset[BB.30_1$Folds != 1,]
testing_data_BB.30_1 <- BB.30_1$Dataset[BB.30_1$Folds == 1,]

References
----------

Vogel S., Bönecke E., Kling C., Kramer E., Lück K., Nagel A., Philipp G., Rühlmann J., Schröter I. & Gebbers, R. (2022), Base neutralizing capacity from agricultural fields in the quaternary landscape of North-East Germany, BONARES Repository, https://doi.org/10.20387/bonares-zh3x-nd80 \cr
\cr
Bönecke, E., Meyer, S., Vogel, S., Schröter, I., Gebbers, R., Kling, C., Kramer, E., Lück, K., Nagel A., Philipp, G., Gerlach F., Palme S., Scheibe D., Ziegler K. & Rühlmann, J. (2021). Guidelines for precise lime management based on high-resolution soil pH, texture and SOM maps generated from proximal soil sensing data. Precision Agriculture, 22, 493-523.
