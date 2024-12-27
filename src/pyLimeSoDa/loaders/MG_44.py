"""
This module provides functionality to load the MG_44 dataset.

The MG_44 dataset contains soil samples from Mato Grosso, Brazil, with 44 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_MG_44() -> dict:
    """
    Load the MG_44 dataset from Mato Grosso, Brazil.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32721)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 44 soil samples from Mato Grosso, Brazil (13 ha study area)
        - Target variables (sampled March 2016, 0-20 cm depth):
            - SOC_target: Soil organic carbon (mmolc/dm³), measured by Walkley-Black method
            - pH_target: pH in CaCl2 suspension (2.5:1 ratio)
            - Clay_target: Clay content (g/dm³), measured by hydrometer method
        - Features:
            - vis-NIR (351): Reflectance (%) at 431.6-2153.1nm, ~5nm intervals
              From Veris MSP3 spectrometer, lab measurements on <2mm samples
        - Coordinates in EPSG:32721
        - Random sampling from previous regular grid
        - Located on heavily weathered sandstone soils
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'MG_44.npz')
    
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
