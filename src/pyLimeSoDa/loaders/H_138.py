"""
This module provides functionality to load the H_138 dataset.

The H_138 dataset contains soil samples from Hubei, China, with 138 reference soil samples.
"""

import pandas as pd
import numpy as np
import os

def load_H_138() -> dict:
    """
    Load the H_138 dataset from Hubei, China.

    Returns:
        dict: A dictionary containing:
            - 'Dataset': pandas DataFrame with soil properties and features
            - 'Folds': numpy array with fold assignments for cross-validation
            - 'Coordinates': pandas DataFrame with spatial coordinates (EPSG:32649)

    Raises:
        FileNotFoundError: If the dataset file is not found

    Notes:
        - 138 soil samples from Hubei, China (420 ha study area)
        - Target variables (sampled June 2013, May 2014, Nov 2014, 0-20 cm depth):
            - SOC_target: Soil organic carbon (%), measured by difference of total C
              (dry combustion, DIN ISO 10694) and inorganic C (0.12 x CaCO3 content)
            - pH_target: pH in water suspension
            - Clay_target: Clay content (%), measured by sieving and x-ray sedimentation
        - Features:
            - MIR (2489): Reflectance (%) at 5397.9-599.8 cm⁻¹, ~2 cm⁻¹ intervals
              From VERTEX 70v FT-IR spectrometer, lab measurements on <2mm samples
        - Coordinates in EPSG:32649
        - Two-phase sampling design:
            1. Adapted Latin Hypercube considering legacy data and terrain
            2. Uncertainty-guided sampling based on Random Forest predictions
        - Located on Jurassic sedimentary rocks (dolomite, silt, limestone)
    """
    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', 'H_138.npz')
    
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
