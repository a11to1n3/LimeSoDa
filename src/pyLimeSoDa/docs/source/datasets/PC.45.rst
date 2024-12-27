PC.45 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: CSMoist, ERa
 \item Sample size: 45
 \item Number of Features: 4
 \item Coordinates: Without coordinates as coordinates could not be found anymore
 \item Location: Pest County, Hungary
 \item Sampling Design: Stratified Systematic Sampling, where three 70 m wide transects were selected based on contrasting environmental settings and soil types ((1) agricultural land, (2) salt affected grassland, (3) forest)
 \item Study Area Size: 4.5 ha
 \item Geological Setting: Alluvial plain of the Danube (2 transects) and wind-blown dune region, where the calcareous sediments are originating from the Danube
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Csilla.Farkas (Csilla.Farkas@nibio.no), Norwegian Institute of Bioeconomy Research (NIBIO)
     \item Tibor Tóth (tibor@rissac.hu), HUN-REN Centre for Agricultural Research

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
PC.45

# Access the dataset
PC.45$Dataset

# Access the folds
PC.45$Folds

# Access the coordinates but empty for PC.45 (i.e. NA)
PC.45$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_PC.45 <- PC.45$Dataset[PC.45$Folds != 1,]
testing_data_PC.45 <- PC.45$Dataset[PC.45$Folds == 1,]

References
----------

Tyurin, I. V. (1935). Comparative study of the methods for the determination of organic carbon in soils and water extracts from soils. Materials on genesis and geography of soils, ML Academy of Sci USSR, 139-158.
