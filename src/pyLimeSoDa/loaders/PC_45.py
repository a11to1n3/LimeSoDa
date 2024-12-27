"""
This module provides functionality to load the PC_45 dataset.

The PC_45 dataset contains soil samples from Pest County, Hungary, with 45 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_PC_45() -> dict:
    """
    Load the PC_45 dataset from Pest County, Hungary.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': None (coordinates not available)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 45 soil samples from Pest County, Hungary (4.5 ha study area)
        - Target variables (sampled November 2004, 0-20 cm depth):
            - SOC_target: Soil organic carbon (%), measured by Tyurin method
            - pH_target: pH in water suspension (2.5:1 ratio, MSz-08-0206/2-1978)
            - Clay_target: Clay content (%), measured by sieve-pipette method (MSZ-08-0205-1978)
        - Features:
            - CSMoist (1): Volumetric moisture content (%) from capacitive sensor
            - ERa (3): Apparent electrical resistivity (Ω m) from EM, ERS and P sensors
        - Coordinates not available
        - Stratified systematic sampling with three 70m transects across different environments
        - Located on Danube alluvial plain and wind-blown dune region with calcareous sediments
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'PC_45.npz')
    
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
