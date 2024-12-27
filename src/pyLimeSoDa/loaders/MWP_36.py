"""
This module provides functionality to load the MWP_36 dataset.

The MWP_36 dataset contains soil samples from Mecklenburg-Western Pomerania, Germany, with 36 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_MWP_36() -> dict:
    """
    Load the MWP_36 dataset from Mecklenburg-Western Pomerania, Germany.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32633)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 36 soil samples from Mecklenburg-Western Pomerania, Germany (18 ha study area)
        - Target variables (sampled August 2022, 0-15 cm depth):
            - SOC_target: Soil organic carbon (%), measured by Walkley-Black method
            - pH_target: pH in CaCl2 suspension (5:1 ratio, DIN ISO 10390)
            - Clay_target: Clay content (%), measured by sieve-pipette method
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 5m LiDAR/photogrammetry
            - RSS (3): Sentinel-2 bare soil bands (B02, B8A, B11)
        - Coordinates in EPSG:32633
        - Random sampling along field transects
        - Located on Pleistocene glacial sands
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'MWP_36.npz')
    
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
