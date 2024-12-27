"""
This module provides functionality to load the BB.250 dataset.

The BB.250 dataset contains soil samples from Brandenburg, Germany, with 250 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_BB_250() -> dict:
    """
    Load the BB.250 dataset from Brandenburg, Germany.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 250 soil samples from Brandenburg, Germany (52 ha study area)
        - Target variables (sampled May 2020, 0-30 cm depth):
            - SOC_target: Soil organic carbon (%), measured by dry combustion (DIN ISO 10694)
            - pH_target: pH in CaCl2 suspension (5:1 ratio, DIN ISO 10390)
            - Clay_target: Clay content (%), measured by sieving/sedimentation (DIN ISO 11277)
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 5m LiDAR/photogrammetry
            - ERa (1): Electrical resistivity (Ω m) from Geophilus electrodes
            - Gamma (1): Total counts from passive gamma sensor
            - pH-ISE (1): pH from ion selective electrodes (Veris)
            - RSS (10): Sentinel-2 bare soil bands (B02-B12)
            - VI (2): NDVI and GNDVI from Sentinel-2
        - Coordinates in EPSG:25833
        - Triangular grid sampling design
        - Located in Pleistocene young morainic landscape

    Example:
        >>> BB_250 = load_BB_250()
        >>> print(BB_250['Dataset'].columns)
        >>> print(BB_250['Coordinates'].head())
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'BB_250.npz')
    
    try:
        loaded = np.load(file_path, allow_pickle=True)
        
        data = {}
        
        # Load Dataset
        if all(k in loaded for k in ['dataset_data', 'dataset_index', 'dataset_columns']):
            data['Dataset'] = pd.DataFrame(
                loaded['dataset_data'],
                index=loaded['dataset_index'],
                columns=loaded['dataset_columns']
            )
        
        # Load Folds
        if 'folds' in loaded:
            data['Folds'] = loaded['folds']
        
        # Load Coordinates
        if all(k in loaded for k in ['coordinates_data', 'coordinates_index', 'coordinates_columns']):
            data['Coordinates'] = pd.DataFrame(
                loaded['coordinates_data'],
                index=loaded['coordinates_index'],
                columns=loaded['coordinates_columns']
            )
        
        return data
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset file not found: {file_path}")