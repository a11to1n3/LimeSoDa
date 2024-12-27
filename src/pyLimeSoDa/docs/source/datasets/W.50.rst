W.50 Dataset
============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: DEM, ERa, VI, XRF
 \item Sample size: 50
 \item Number of Features: 15
 \item Coordinates: Without coordinates because of privacy concerns
 \item Location: Wisconsin, USA
 \item Sampling Design: conditioned Latin Hypercube Sampling based on electrical conductivity, terrain parameters, and normalized difference vegetation index
 \item Study Area Size: 80 ha
 \item Geological Setting: Glacial outwash and sediments of the Johnson End Moraine
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Jingyi Huang, (jhuang426@wisc.edu), University of Wisconsin-Madison

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
W.50

# Access the dataset
W.50$Dataset

# Access the folds
W.50$Folds

# Access the coordinates but empty for W.50 (i.e. NA)
W.50$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_W.50 <- W.50$Dataset[W.50$Folds != 1,]
testing_data_W.50 <- W.50$Dataset[W.50$Folds == 1,]

References
----------

Burt, R. (Ed.) (2014). Kellogg soil survey laboratory methods manual. United States Department of Agriculture, Natural Resources Conservation Service, National Soil Survey Center, Kellogg Soil Survey Laboratory.\cr
\cr
Gee, G. W., & Bauder, J. W. (1979). Particle size analysis by hydrometer: a simplified method for routine textural analysis and a sensitivity test of measurement parameters. Soil Science Society of America Journal, 43(5), 1004-1007.\cr
\cr
Nelson, D.W. & Sommers, L.E. (1996) Total Carbon, Organic Carbon, and Organic Matter. In: Sparks, D.L., Page, A.L., Helmke, P.A., Loeppert, R.H., Soltanpour, P.N., Tabatabai, M.A., Johnston, C.T. & Sumner, M.E., Eds., Methods of Soil Analysis. Part 3. Chemical Methods, Soil Science Society of America, Madison, WI, 961-1010.
