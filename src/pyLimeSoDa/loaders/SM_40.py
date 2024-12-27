"""
This module provides functionality to load the SM_40 dataset.

The SM_40 dataset contains soil samples from South Moravia, Czechia, with 40 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_SM_40() -> dict:
    """
    Load the SM_40 dataset from South Moravia, Czechia.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32633)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 40 soil samples from South Moravia, Czechia (53 ha study area)
        - Target variables:
            - SOC_target: Soil organic carbon (%), measured by Walkley-Black method
              (sampled May 2004, 0-30 cm depth)
            - pH_target: pH in KCl suspension
              (sampled May 2004, 0-30 cm depth)
            - Clay_target: Clay content (%), measured by hydrometer method
              (sampled April 2006, 0-30 cm depth)
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 2m LiDAR
            - ERa (1): Apparent electrical resistivity (Ω m) from EM38 sensor (0-75 cm depth)
        - Coordinates in EPSG:32633
        - Stratified sampling from previous regular grid
        - Located on Weichselian sandy loess
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'SM_40.npz')
    
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
