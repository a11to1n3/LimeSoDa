"""
This module provides functionality to load the CV_98 dataset.

The CV_98 dataset contains soil samples from Canton of Vaud, Switzerland, with 98 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_CV_98() -> dict:
    """
    Load the CV_98 dataset from Canton of Vaud, Switzerland.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': None (dataset not georeferenced)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 98 soil samples from Canton of Vaud, Switzerland (28 ha study area)
        - Target variables (sampled May-June and Sept-Oct 2021, 0-20 cm depth):
            - SOC_target: Soil organic carbon (%), measured by Walkley-Black method
            - pH_target: pH in water suspension (5:1 ratio, NF ISO 10390)
            - Clay_target: Clay content (%), measured by sieve-pipette method
        - Features:
            - vis-NIR (2151): Reflectance (%) at 350-2500nm, 1nm intervals
              From PSR+3500 spectrometer, in-situ measurements
        - No coordinates (not georeferenced)
        - Stratified random sampling based on treatments
        - Located on glacial/fluvioglacial deposits
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'CV_98.npz')
    
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
