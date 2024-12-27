"""
This module provides functionality to load the BC_58 dataset.

Note: This dataset will likely be removed due to data quality concerns.
"""

import pandas as pd
import numpy as np
import os

def load_BC_58() -> dict:
    """
    Load the BC_58 dataset.
    
    Warning: This dataset will likely be removed due to data quality concerns.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates

    Raises:
        FileNotFoundError: If the dataset file is not found
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'BC_58.npz')
    
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
