"""
This module provides functionality to load the SP_231 dataset.

The SP_231 dataset contains soil samples from Saitama Prefecture, Japan, with 231 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_SP_231() -> dict:
    """
    Load the SP_231 dataset from Saitama Prefecture, Japan.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32654)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 231 soil samples from Saitama Prefecture, Japan (3.1 ha study area)
        - Target variables (sampled Feb 2017, Dec 2017, Feb 2018, 0-15 cm depth):
            - SOM_target: Soil organic matter (%), measured by loss on ignition
            - pH_target: pH in water suspension (2.5:1 ratio)
            - Clay_target: Clay content (%), measured by sieve-pipette method
        - Features:
            - vis-NIR (271): Reflectance (%) at 350-1700 nm, 5 nm intervals
              From SAS3000 spectrometer, in-situ measurements
        - Coordinates in EPSG:32654
        - Mixed sampling design: systematic (corners/middle) and random sampling
        - Located on Silandic Andosols
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'SP_231.npz')
    
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
