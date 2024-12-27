"""
This module provides functionality to load the MGS_101 dataset.

The MGS_101 dataset contains soil samples from Mato Grosso do Sul, Brazil, with 101 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_MGS_101() -> dict:
    """
    Load the MGS_101 dataset from Mato Grosso do Sul, Brazil.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32721)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 101 soil samples from Mato Grosso do Sul, Brazil (95 ha study area)
        - Target variables (sampled September 2022, 0-20 cm depth):
            - SOC_target: Soil organic carbon (%), measured by Walkley-Black method
            - pH_target: pH in water suspension (2.5:1 ratio)
            - Clay_target: Clay content (%), measured by sieve-pipette method
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 30m Copernicus SAR
            - RSS (12): Sentinel-2 bare soil bands (B01-B12)
            - VI (2): NDVI and GNDVI from Sentinel-2
        - Coordinates in EPSG:32721
        - Regular grid sampling design
        - Located on heavily weathered soils from Andesitic Basalt
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'MGS_101.npz')
    
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
