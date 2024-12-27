MG.44 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: vis-NIR
 \item Sample size: 44
 \item Number of Features: 351
 \item Coordinates: With coordinates (EPSG: 32721)
 \item Location: Mato Grosso, Brazil
 \item Sampling Design: Random Sampling from previous Regular Grid Sampling
 \item Study Area Size: 13 ha
 \item Geological Setting: Heavily weathered soils originating from Sandstone
 \item Previous Data Publication: Full dataset published in Tavares et al. (2022)
 \item Contact Information:
   
     \item Tiago Rodrigues Tavares, tiagosrt@usp.br, University of Sao Paulo
     \item José Paulo Molin (jpmolin@usp.br), University of Sao Paulo

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
MG.44

# Access the dataset
MG.44$Dataset

# Access the folds
MG.44$Folds

# Access the coordinates
MG.44$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_MG.44 <- MG.44$Dataset[MG.44$Folds != 1,]
testing_data_MG.44 <- MG.44$Dataset[MG.44$Folds == 1,]

References
----------

Bouyoucos, G. J. (1927). The hydrometer as a new method for the mechanical analysis of soils. Soil science, 23(5), 343-354.\cr
\cr
Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.\cr
\cr
Tavares, T. R., Molin, J. P., Nunes, L. C., Alves, E. E. N., Krug, F. J., & de Carvalho, H. W. P. (2022). Spectral data of tropical soils using dry-chemistry techniques (VNIR, XRF, and LIBS): A dataset for soil fertility prediction. Data in Brief, 41, 108004.
