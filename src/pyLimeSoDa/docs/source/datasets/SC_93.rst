SC.93 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: vis-NIR
 \item Sample size: 93
 \item Number of Features: 2,146
 \item Coordinates: With coordinates (EPSG: 32722)
 \item Location: Santa Catarina, Brazil
 \item Sampling Design: conditioned Latin Hypercube Sampling based on terrain parameters
 \item Study Area Size: 108 ha
 \item Geological Setting: Heavily weathered soils originating from volcanic rock of the Serra Geral Formation (basalt, dacit)
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Taciara Zborowski Horst (taciaraz@utfpr.edu.br), Federal University of Technology – Paraná
     \item Ricardo Simão Diniz Dalmolin (dalmolin@ufsm.br), Federal University of Santa Maria

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
SC.93

# Access the dataset
SC.93$Dataset

# Access the folds
SC.93$Folds

# Access the coordinates
SC.93$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_SC.93 <- SC.93$Dataset[SC.93$Folds != 1,]
testing_data_SC.93 <- SC.93$Dataset[SC.93$Folds == 1,]

References
----------

Gee, G.W. & Bauder, J.W. (1986) Particle-Size Analysis. In: Klute, A., Ed., Methods of Soil Analysis, Part 1. Physical and Mineralogical Methods, Agronomy Monograph No. 9, 2nd Edition, American Society of Agronomy/Soil Science Society of America, Madison, WI, 383-411.\cr
\cr
Tedesco, M.J., Gianello, C., Bissani, C., Bohnen, H. & Volkweiss, S.J. (1995) Análise de solo, plantas e outros materiais. [Analysis of soil, plants and other materials.] 2nd Edition, Departamento de Solos da Universidade Federal do Rio Grande do Sul, Porto Alegre, 174.
