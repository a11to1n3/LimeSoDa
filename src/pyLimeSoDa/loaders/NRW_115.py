"""
This module provides functionality to load the NRW_115 dataset.

The NRW_115 dataset contains soil samples from North Rhine-Westphalia, Germany, with 115 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_NRW_115() -> dict:
    """
    Load the NRW_115 dataset from North Rhine-Westphalia, Germany.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': None (omitted for privacy)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 115 soil samples from North Rhine-Westphalia, Germany (17 ha study area)
        - Target variables (sampled October 2013 & November 2015, 0-30 cm depth):
            - SOC_target: Soil organic carbon (%), measured by difference of total C
              (dry combustion, DIN ISO 10694) and inorganic C (0.12 x CaCO3 content)
            - pH_target: pH in CaCl2 suspension (5:1 ratio, DIN ISO 10390)
            - Clay_target: Clay content (%), measured by sieve-pipette method (DIN ISO 11277)
        - Features:
            - MIR (1686): Reflectance (%) at 3799-549.6 cm⁻¹, ~2 cm⁻¹ intervals
              From Bruker Tensor 27 HTS-XT spectrometer, lab measurements on <2mm samples
        - Coordinates omitted for privacy
        - Regular grid sampling on two adjacent fields in two campaigns
        - Located on Cretaceous marls with partial glacial till, aeolian sand and fluvial sediments
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'NRW_115.npz')
    
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
