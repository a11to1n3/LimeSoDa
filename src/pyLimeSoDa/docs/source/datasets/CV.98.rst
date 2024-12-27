CV.98 Dataset
=============

Description
-----------


 \item Target Soil Properties: SOC, pH, Clay
 \item Groups of Features: vis-NIR
 \item Sample size: 98
 \item Number of Features: 2,151
 \item Coordinates: Without coordinates because dataset was not georeferenced
 \item Location: Canton of Vaud, Switzerland
 \item Sampling Design: Stratified Random Sampling based on different treatments of organic amendments, fertilization, crop rotation and soil cultivation
 \item Study Area Size: 28 ha
 \item Geological Setting: Glacial or fluvioglacial deposits
 \item Previous Data Publication: Full dataset published in Metzger et al. (2024) but under embargo until June 2025
 \item Contact Information:
   
     \item Konrad Metzger (konrad.metzger@agroscope.admin.ch), Agroscope
     \item Luca Bragazza (luca.bragazza@agroscope.admin.ch), Agroscope

Details
-------



Examples
--------

.. code-block:: R

# Load the dataset list
CV.98

# Access the dataset
CV.98$Dataset

# Access the folds
CV.98$Folds

# Access the coordinates but empty for CV.98 (i.e. NA)
CV.98$Coordinates

# How to split the dataset into training and testing folds for the example of the first fold
training_data_CV.98 <- CV.98$Dataset[CV.98$Folds != 1,]
testing_data_CV.98 <- CV.98$Dataset[CV.98$Folds == 1,]

References
----------

Gee, G.W. & Bauder, J.W. (1986) Particle-Size Analysis. In: Klute, A., Ed., Methods of Soil Analysis, Part 1. Physical and Mineralogical Methods, Agronomy Monograph No. 9, 2nd Edition, American Society of Agronomy/Soil Science Society of America, Madison, WI, 383-411.\cr
\cr
Metzger, K., Liebisch, F., Herrera, J. M., Guillaume, T., Walder, F. & Bragazza, L. (2024). Agroscope_SoilSpectralLibrary _2024. Zenodo repository. https://doi.org/10.5281/zenodo.11204174 \cr
\cr
Walkley, A. & Black, I. A. (1934). An examination of the Degtjareff method for determining soil organic matter, and a proposed modification of the chromic acid titration method. Soil science, 37(1), 29-38.
