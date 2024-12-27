"""
This module provides functionality to load the BB.30_1 dataset.

The BB.30_1 dataset contains soil samples from Brandenburg, Germany, with 30 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_BB_30_1() -> dict:
    """
    Load the BB.30_1 dataset from Brandenburg, Germany.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:25833)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 30 soil samples from Brandenburg, Germany (19 ha study area)
        - Target variables (sampled August/October 2017, 0-30 cm depth):
            - SOC_target: Soil organic carbon (%), measured by dry combustion (DIN ISO 10694)
            - pH_target: pH in CaCl2 suspension (5:1 ratio, DIN ISO 10390)
            - Clay_target: Clay content (%), measured by sieve-pipette method (DIN ISO 11277)
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 5m LiDAR/photogrammetry
            - ERa (1): Electrical resistivity (Ω m) from Veris EC Surveyor
            - pH-ISE (1): pH from ion selective electrodes (Veris)
            - VI (1): NDVI from Sentinel-2
        - Coordinates in EPSG:25833
        - Multi-criteria sampling design
        - Located in Pleistocene young morainic landscape with glacial sand
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'BB_30_1.npz')
    
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
