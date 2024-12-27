"""
This module provides functionality to load the SSP_58 dataset.

The SSP_58 dataset contains soil samples from Sao Paulo, Brazil, with 58 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_SSP_58() -> dict:
    """
    Load the SSP_58 dataset from Sao Paulo, Brazil.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': None (dataset was not georeferenced)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 58 soil samples from Sao Paulo, Brazil (0.7 ha study area)
        - Target variables (sampled September 2015, 0-20 cm depth):
            - SOC_target: Soil organic carbon (mmolc/dm3), measured by Walkley-Black method
            - pH_target: pH in CaCl2 suspension (2.5:1 ratio)
            - Clay_target: Clay content (g/dm3), measured by hydrometer method
        - Features:
            - vis-NIR (351): Reflectance (%) at 431.6-2153.1 nm, ~5 nm intervals
              From Veris MSP3 spectrometer, lab measurements on <2mm samples
        - No coordinates (dataset not georeferenced)
        - Stratified random sampling based on K2O and CaO treatment doses
        - Located on heavily weathered soils from diabase
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'SSP_58.npz')
    
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
