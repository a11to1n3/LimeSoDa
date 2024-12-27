"""
This module provides functionality to load the B.204 dataset.

The B.204 dataset contains soil samples from Bahia, Brazil, with 204 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_B_204() -> dict:
    """
    Load the B.204 dataset from Bahia, Brazil.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32723)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 204 soil samples from Bahia, Brazil (204 ha study area)
        - Target variables (sampled October 2016, 0-20 cm depth):
            - SOC_target: Soil organic carbon (%), measured by Walkley-Black method
            - pH_target: pH in water suspension (2.5:1 ratio)
            - Clay_target: Clay content (%), measured by sieve-pipette method
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 30m SAR
            - RSS (12): Sentinel-2 bare soil bands (B01-B12)
            - VI (2): NDVI and GNDVI from Sentinel-2
        - Coordinates in EPSG:32723
        - Regular grid sampling design
        - Located in area with heavily weathered soils from sedimentary rocks

    Example:
        >>> B_204 = load_B_204()
        >>> print(B_204['Dataset'].columns)
        >>> print(B_204['Coordinates'].head())
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'B_204.npz')
    
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
