"""
This module provides functionality to load the RP_62 dataset.

The RP_62 dataset contains soil samples from Rhineland-Palatinate, Germany, with 62 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_RP_62() -> dict:
    """
    Load the RP_62 dataset from Rhineland-Palatinate, Germany.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': None (omitted for privacy)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 62 soil samples from Rhineland-Palatinate, Germany (3.3 ha study area)
        - Target variables:
            - SOC_target: Soil organic carbon (%), measured by Walkley-Black method
              (sampled October 2017, 0-30 cm depth)
            - pH_target: pH in water suspension (5:1 ratio, DIN ISO 10390)
              (sampled May 2020, 0-30 cm depth)
            - Clay_target: Clay content (%), measured by sieve-pipette method (DIN ISO 11277)
              (sampled October 2017, 0-30 cm depth)
        - Features:
            - ERa (1): Apparent electrical resistivity (Ω m) from rolling electrodes
            - Gamma (5): Gamma radiation counts from passive sensor
            - NIR (1401): Reflectance (%) at 1000-2400 nm, 1 nm intervals
            - pH-ISE (1): In-situ pH from ion selective electrodes
            - VI (2): NDVI and GNDVI from Sentinel-2
        - Coordinates omitted for privacy
        - Regular grid sampling design
        - Located on Pleistocene periglacial slope deposits with Weichselian loess
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'RP_62.npz')
    
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
