"""
This module provides functionality to load the SC_50 dataset.

The SC_50 dataset contains soil samples from Santa Catarina, Brazil, with 50 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_SC_50() -> dict:
    """
    Load the SC_50 dataset from Santa Catarina, Brazil.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32722)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 50 soil samples from Santa Catarina, Brazil (13 ha study area)
        - Target variables (sampled November 2013, 0-20 cm depth):
            - SOC_target: Soil organic carbon (%), measured by Walkley-Black method
            - pH_target: pH in water suspension (5:1 ratio)
            - Clay_target: Clay content (%), measured by sieve-pipette method (DIN ISO 11277)
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 30m SAR DEM
            - ERa (1): Apparent electrical resistivity (Ω m) from LandMapper ERM-02
        - Coordinates in EPSG:32722
        - Regular grid sampling design
        - Located on heavily weathered soils from Mesozoic basalt rocks
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'SC_50.npz')
    
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
