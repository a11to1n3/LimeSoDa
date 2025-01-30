"""
This module provides functions for loading individual datasets in the LimeSoDa package.

The datasets are stored as numpy compressed (.npz) files and are loaded into a consistent structure:
{
    'Dataset': pandas.DataFrame,  # Contains soil properties and features
    'Folds': numpy.ndarray,  # Pre-defined folds for cross-validation
    'Coordinates': pandas.DataFrame or None  # Spatial coordinates if available
}

Functions:
- load_dataset: Load a specific dataset by name
- list_datasets: List all available datasets
"""

import os
import numpy as np
import pandas as pd
from pathlib import Path

# Get the data directory relative to this file
DATA_DIR = Path(__file__).parent.parent / 'data'

def load_dataset(name: str) -> dict:
    """
    Load a dataset by name.

    Args:
        name (str): Name of the dataset to load (e.g., 'BB.250')

    Returns:
        dict: A dictionary containing 'Dataset', 'Folds', and 'Coordinates' keys

    Raises:
        ValueError: If the specified dataset name is not found

    Example:
        >>> BB_250 = load_dataset('BB.250')
        >>> print(BB_250['Dataset'].head())
    """
    file_name = name + '.npz'
    file_path = DATA_DIR / file_name
    
    if not file_path.exists():
        # List available datasets to help user
        available = list_datasets()
        # Print file path for debugging
        print(f"Looking for file at: {file_path}")
        print(f"DATA_DIR is: {DATA_DIR}")
        print(f"Files in DATA_DIR: {os.listdir(DATA_DIR)}")
        raise ValueError(f"Dataset '{name}' not found. Available datasets: {available}")
        
    data = np.load(file_path, allow_pickle=True)
    
    if name == "Overview_Datasets":
        return pd.DataFrame(
            data['data'],
            index=data['index'], 
            columns=data['columns']
        )
        
    # Convert to pandas DataFrame if needed
    if 'dataset_data' in data.files:
        dataset = pd.DataFrame(
            data['dataset_data'],
            index=data['dataset_index'],
            columns=data['dataset_columns']
        )
        try:
            coords = pd.DataFrame(
                data['coordinates_data'],
                index=data['coordinates_index'],
                columns=data['coordinates_columns']
            )
        except KeyError:
            coords = np.nan
        return {'Dataset': dataset, 'Coordinates': coords, 'Folds': data['folds']}
        
    return dict(data)

def list_datasets() -> list:
    """
    List all available datasets in the LimeSoDa package.

    Returns:
        list: A list of dataset names (strings)

    Example:
        >>> datasets = list_datasets()
        >>> print(datasets)
        ['BB.250', 'SP.231', ...]
    """
    return sorted(
        f.stem
        for f in DATA_DIR.glob('*.npz')
    )