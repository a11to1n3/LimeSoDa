"""
This module provides functionality to load the W_50 dataset.

The W_50 dataset contains soil samples from Wisconsin, USA, with 50 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_W_50() -> dict:
    """
    Load the W_50 dataset from Wisconsin, USA.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': None (dataset not georeferenced for privacy)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 50 soil samples from Wisconsin, USA (80 ha study area)
        - Target variables (sampled July 2019, 0-10 cm depth):
            - SOC_target: Soil organic carbon (%), measured by dry combustion
            - pH_target: pH in water suspension (1:1 ratio)
            - Clay_target: Clay content (%), measured by hydrometer method
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 3m LiDAR
            - ERa (1): Apparent electrical resistivity (Ω m) from DUALEM-1HS (0-30 cm depth)
            - VI (2): NDVI, GNDVI from Sentinel-2 imagery
            - XRF (10): Mg, Al, Si, Ca, Ti, Mn, Fe, Zn, Sr, Zr (ppm) from Delta Premium PXRF
        - No coordinates for privacy
        - Conditioned Latin Hypercube sampling based on ERa, terrain, and NDVI
        - Located on glacial outwash and Johnson End Moraine sediments
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'W_50.npz')
    
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
