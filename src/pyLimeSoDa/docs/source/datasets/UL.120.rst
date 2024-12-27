UL.120 Dataset
==============

Description
-----------


 \item Target Soil Properties: SOM, pH, Clay
 \item Groups of Features: ERa, vis-NIR
 \item Sample size: 120
 \item Number of Features: 2,082
 \item Coordinates: Without coordinates because of privacy concerns instead with dummy coordinates (EPSG: 4326)
 \item Location: Uppsala Län, Sweden
 \item Sampling Design: Three sampling designs over multiple adjacent fields: (1) Regular Grid Sampling, targeted sampling through Surface Tortoise Sampling (Persson et al. 2023) based on (2) ERa and (3) Reflectance from remote sensing
 \item Study Area Size: 97 ha
 \item Geological Setting: Glacial and postglacial clay with elements of sandy till
 \item Previous Data Publication: None
 \item Contact Information:
   
     \item Johanna Wetterlind (Johanna.Wetterlind@slu.se), Swedish University of Agricultural Sciences
     \item Bo Stenberg (Bo.Stenberg@slu.se), Swedish University of Agricultural Sciences

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
UL.120

# Access the dataset
UL.120$Dataset

# Access the folds
UL.120$Folds

# Access the coordinates but for UL.120 only dummy coordinates
UL.120$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_UL.120 <- UL.120$Dataset[UL.120$Folds != 1,]
testing_data_UL.120 <- UL.120$Dataset[UL.120$Folds == 1,]

References
----------

Ekström, G. (1927). Klassifikation av Svenska Åkerjordar (Classification of Swedish arable soils). Sveriges Geologiska Undersökning, Ser C. 345, 161 pp. \cr
\cr
Gee, G.W. & Bauder, J.W. (1986) Particle-Size Analysis. In: Klute, A., Ed., Methods of Soil Analysis, Part 1. Physical and Mineralogical Methods, Agronomy Monograph No. 9, 2nd Edition, American Society of Agronomy/Soil Science Society of America, Madison, WI, 383-411.\cr
\cr
Persson, K., Söderström, M. & Mutua, J. (2023). SurfaceTortoise: Find Optimal Sampling Locations Based on Spatial Covariate(s). R package version 2.0.1.
