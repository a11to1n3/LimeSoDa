"""
This module provides functionality to load the NSW_52 dataset.

The NSW_52 dataset contains soil samples from New South Wales, Australia, with 52 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_NSW_52() -> dict:
    """
    Load the NSW_52 dataset from New South Wales, Australia.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32755)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 52 soil samples from New South Wales, Australia (1,158 ha study area)
        - Target variables (sampled July & December 2018, 0-10 cm depth):
            - SOC_target: Soil organic carbon (%), measured by Walkley-Black method
            - pH_target: pH in CaCl2 suspension (5:1 ratio)
            - Clay_target: Clay content (%), measured by sieve-pipette method
        - Features:
            - DEM (2): Altitude (m), Slope (°) from 5m LiDAR/photogrammetry
            - RSS (3): Sentinel-2 bare soil bands (B02, B8A, B11)
        - Coordinates in EPSG:32755
        - Two sampling designs: k-means cluster-based random sampling and 
          stratified random sampling based on soil type/land use
        - Located on alluvial deposits of basaltic sediments
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'NSW_52.npz')
    
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
