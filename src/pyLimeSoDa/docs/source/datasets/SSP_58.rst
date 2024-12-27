SSP.58 Dataset
==============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: vis-NIR
 \item Sample size: 58
 \item Number of Features: 351
 \item Coordinates: Without coordinates because dataset was not georeferenced
 \item Location: State of Sao Paulo, Brazil

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
SSP.58

# Access the dataset
SSP.58$Dataset

# Access the folds
SSP.58$Folds

# Access the coordinates but empty for SSP.58 (i.e. NA)
SSP.58$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_SSP.58 <- SSP.58$Dataset[SSP.58$Folds != 1,]
testing_data_SSP.58 <- SSP.58$Dataset[SSP.58$Folds == 1,]

References
----------

Bouyoucos, G. J. (1927). The hydrometer as a new method for the mechanical analysis of soils. Soil science, 23(5), 343-354.\cr
\cr
Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.\cr
\cr
Tavares, T. R., Molin, J. P., Nunes, L. C., Alves, E. E. N., Krug, F. J., & de Carvalho, H. W. P. (2022). Spectral data of tropical soils using dry-chemistry techniques (VNIR, XRF, and LIBS): A dataset for soil fertility prediction. Data in Brief, 41, 108004.
