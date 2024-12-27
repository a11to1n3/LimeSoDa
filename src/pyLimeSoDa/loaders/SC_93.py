"""
This module provides functionality to load the SC_93 dataset.

The SC_93 dataset contains soil samples from Santa Catarina, Brazil, with 93 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_SC_93() -> dict:
    """
    Load the SC_93 dataset from Santa Catarina, Brazil.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32722)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 93 soil samples from Santa Catarina, Brazil (108 ha study area)
        - Target variables (sampled December 2016, 0-20 cm depth):
            - SOC_target: Soil organic carbon (%), measured by light absorption after oxidization
            - pH_target: pH in water suspension (1:1 ratio)
            - Clay_target: Clay content (%), measured by sieve-pipette method
        - Features:
            - vis-NIR (2146): Reflectance (%) at 355-2500 nm, 1 nm intervals
              From ASD FieldSpec 4, lab measurements on <2mm samples
        - Coordinates in EPSG:32722
        - Conditioned Latin Hypercube sampling based on terrain parameters
        - Located on heavily weathered soils from volcanic rock (basalt, dacite)
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'SC_93.npz')
    
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
