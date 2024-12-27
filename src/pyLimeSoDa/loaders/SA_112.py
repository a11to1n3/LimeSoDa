"""
This module provides functionality to load the SA_112 dataset.

The SA_112 dataset contains soil samples from Saxony-Anhalt, Germany, with 112 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_SA_112() -> dict:
    """
    Load the SA_112 dataset from Saxony-Anhalt, Germany.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': None (omitted for privacy)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 112 soil samples from Saxony-Anhalt, Germany (27 ha study area)
        - Target variables (sampled October 2016, 0-30 cm depth):
            - SOC_target: Soil organic carbon (%), measured by difference of total C
              (dry combustion, DIN ISO 10694) and inorganic C (0.12 x CaCO3 content)
            - pH_target: pH in water suspension (5:1 ratio, DIN ISO 10390)
            - Clay_target: Clay content (%), measured by sieve-pipette method (DIN ISO 11277)
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 5m LiDAR/photogrammetry
            - ERa (1): Apparent electrical resistivity (Ω m) from rolling electrodes
            - Gamma (5): Gamma radiation counts from passive sensor
            - NIR (1401): Reflectance (%) at 1000-2400 nm, 1 nm intervals
            - pH-ISE (1): In-situ pH from ion selective electrodes
            - VI (2): NDVI and GNDVI from Sentinel-2
        - Coordinates omitted for privacy
        - Regular grid sampling with missing values in field center
        - Located on Weichselian loess
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'SA_112.npz')
    
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
