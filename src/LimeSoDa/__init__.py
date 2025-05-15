"""
LimeSoDa: Precision Liming Soil Datasets

This package provides access to a collection of soil datasets for precision liming applications.
It includes 31 datasets with soil properties and features for modeling purposes.

The main goals of LimeSoDa are:
1. To enable reliable benchmarking of various modeling approaches in Digital Soil Mapping and Pedometrics
2. To provide an open collection of multiple datasets for soil science research

Each dataset in LimeSoDa contains:
- Target soil properties: Soil Organic Matter (SOM) or Soil Organic Carbon (SOC), pH, and clay content
- Dataset-specific features from laboratory-based spectroscopy, in-situ proximal soil sensing, and remote sensing
- Pre-defined folds for 10-fold cross-validation
- Spatial coordinates (where available)

Data Structure:
- Dataset: pandas DataFrame with soil properties and features
- Folds: numpy array with fold assignments for cross-validation
- Coordinates: pandas DataFrame with spatial coordinates

Main functions:
- load_dataset: Load a specific dataset by name
- list_datasets: List all available datasets

For detailed information on each dataset, use the help function:
>>> help(LimeSoDa.loaders.BB_250)

For usage examples, see the package README or the online documentation.
"""

from .loaders import load_dataset, list_datasets
from . import utils

__all__ = ['load_dataset', 'list_datasets', 'utils']
__version__ = '0.1.4'