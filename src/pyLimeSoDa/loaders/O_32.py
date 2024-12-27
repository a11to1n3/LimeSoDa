"""
This module provides functionality to load the O_32 dataset.

The O_32 dataset contains soil samples from Occitanie, France, with 32 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_O_32() -> dict:
    """
    Load the O_32 dataset from Occitanie, France.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': None (omitted for privacy)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 32 soil samples from Occitanie, France
        - Target variables (sampled March 2020, 0-20 cm depth):
            - SOC_target: Soil organic carbon (%), measured by difference of total C
              (dry combustion, DIN ISO 10694) and inorganic C (0.12 x CaCO3 content)
            - pH_target: pH in CaCl2 suspension (5:1 ratio, DIN ISO 10390)
            - Clay_target: Clay content (%), measured by sieve-pipette method (DIN ISO 11277)
        - Features:
            - MIR (1637): Reflectance (%) at 3800-751.1 cm⁻¹, ~2 cm⁻¹ intervals
              From Agilent 4300 handheld spectrometer, lab measurements on <2mm samples
        - Coordinates omitted for privacy
        - Regular grid sampling design
        - Located on Pleistocene fluvial deposits and Miocene marine deposits
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'O_32.npz')
    
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
