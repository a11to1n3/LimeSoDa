"""
This module provides functionality to load the UL_120 dataset.

The UL_120 dataset contains soil samples from Uppsala Län, Sweden, with 120 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_UL_120() -> dict:
    """
    Load the UL_120 dataset from Uppsala Län, Sweden.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with dummy coordinates (EPSG:4326)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 120 soil samples from Uppsala Län, Sweden (97 ha study area)
        - Target variables (sampled September 2005, 0-20 cm depth):
            - SOM_target: Soil organic matter (%), measured by loss on ignition with clay correction
            - pH_target: pH in water suspension (5:1 ratio)
            - Clay_target: Clay content (%), measured by sieve-pipette method
        - Features:
            - ERa (1): Apparent electrical resistivity (Ω m) from EM38 sensor (0-150 cm depth)
            - vis-NIR (2081): Reflectance (%) at 420-2500 nm, 1 nm intervals
              From FieldSpec Pro FR, lab measurements on <2mm samples
        - Coordinates are dummy values (EPSG:4326) for privacy
        - Mixed sampling design: regular grid and targeted sampling based on ERa and reflectance
        - Located on glacial and postglacial clay with elements of sandy till
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'UL_120.npz')
    
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
