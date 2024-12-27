H.138 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: MIR
 \item Sample size: 138
 \item Number of Features: 2,489
 \item Coordinates: With coordinates (EPSG: 32649)
 \item Location: Hubei, China
 \item Sampling Design: Two sampling designs: (1) adapted Latin Hypercube Sampling taking into account legacy samples, correlation and accessibility based on terrain parameters and (2) Uncertainty Guided Sampling based on uncertainty predictions from a Random Forest model (Stumpf et al. 2017)
 \item Study Area Size: 420 ha
 \item Geological Setting: Sedimentary rocks, mainly dolomite with silt and limestone formed in the middle and lower Jurassic
 \item Previous Data Publication: Full dataset published in Wadoux et al. (2025) [?Not yet published but planned?]
 \item Contact Information:
   
     \item Alexandre M.J.-C- Wadoux (Alexandre.Wadoux@inrae.fr), University of Montpellier

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
H.138

# Access the dataset
H.138$Dataset

# Access the folds
H.138$Folds

# Access the coordinates
H.138$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_H.138 <- H.138$Dataset[H.138$Folds != 1,]
testing_data_H.138 <- H.138$Dataset[H.138$Folds == 1,]

References
----------

[ ? Add data publication when published ?]\cr
\cr
Stumpf, F., Schmidt, K., Goebes, P., Behrens, T., Schönbrodt-Stitt, S., Wadoux, A., Xiang, W. & Scholten, T. (2017). Uncertainty-guided sampling to improve digital soil maps. Catena, 153, 30-38.
