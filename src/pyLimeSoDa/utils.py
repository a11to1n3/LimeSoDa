"""
This module provides utility functions for working with Lime_SoDa datasets.

Functions:
    Data Processing:
        - split_dataset: Split dataset into train/test sets based on folds
        - normalize_features: Normalize features using various methods

    Evaluation:
        - calculate_performance: Calculate R-squared and RMSE metrics
        - cross_validate: Perform k-fold cross validation

    Visualization:
        - plot_soil_map: Plot soil properties on a map
        - plot_feature_importance: Plot feature importance from models

    Helper Functions:
        - _check_input_types: Validate input data types
        - _validate_folds: Validate fold indices
"""

import pandas as pd
import numpy as np
from typing import Union, List, Dict, Tuple
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import folium

def _check_input_types(data: dict, fold: Union[int, List[int]], targets: Union[str, List[str], None]) -> None:
    """Validate input data types for dataset functions."""
    if not isinstance(data, dict) or 'Dataset' not in data or 'Folds' not in data:
        raise TypeError("data must be a dictionary with 'Dataset' and 'Folds' keys")
    if not isinstance(fold, (int, list)):
        raise TypeError("fold must be an integer or list of integers")
    if targets is not None and not isinstance(targets, (str, list)):
        raise TypeError("targets must be None, a string, or list of strings")

def _validate_folds(folds: Union[int, List[int]], n_folds: int) -> List[int]:
    """Validate and convert fold indices."""
    if isinstance(folds, int):
        folds = [folds]
    if any(f < 1 or f > n_folds for f in folds):
        raise ValueError(f"Folds must be between 1 and {n_folds}")
    return folds

def split_dataset(data: dict, fold: Union[int, List[int]], targets: Union[str, List[str]] = None, n_folds: int = 10) -> Tuple:
    """
    Split a dataset into training and testing sets based on the specified fold(s).

    Args:
        data (dict): Dataset dictionary containing 'Dataset' and 'Folds' keys
        fold (int | list[int]): The fold number(s) to use as test set(s)
        targets (str | list[str], optional): Target variable(s) to use
        n_folds (int, optional): Number of folds in dataset. Defaults to 10.

    Returns:
        tuple: (X_train, X_test, y_train, y_test)

    Raises:
        TypeError: If input types are invalid
        ValueError: If folds or targets are invalid
    """
    _check_input_types(data, fold, targets)
    fold = _validate_folds(fold, n_folds)

    dataset = data['Dataset']
    folds = data['Folds']

    target_cols = [col for col in dataset.columns if col.endswith('_target')]
    
    if targets is not None:
        targets = [targets] if isinstance(targets, str) else targets
        invalid_targets = [t for t in targets if t not in target_cols]
        if invalid_targets:
            raise ValueError(f"Invalid targets: {invalid_targets}. Valid targets: {', '.join(target_cols)}")
        target_cols = targets

    X = dataset.drop(columns=target_cols)
    y = dataset[target_cols]

    train_mask = ~np.isin(folds, fold)
    test_mask = np.isin(folds, fold)

    return X[train_mask], X[test_mask], y[train_mask], y[test_mask]

def calculate_performance(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """
    Calculate R-squared and RMSE for model predictions.

    Args:
        y_true (np.ndarray): True target values
        y_pred (np.ndarray): Predicted target values

    Returns:
        dict: Dictionary with 'r2' and 'rmse' metrics
    """
    r2 = 1 - np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2)
    rmse = np.sqrt(np.mean((y_true - y_pred)**2))
    return {'r2': r2, 'rmse': rmse}

def plot_soil_map(data: dict, target: str, title: str = None, zoom_start: int = 12) -> folium.Map:
    """
    Plot soil properties on an interactive map.

    Args:
        data (dict): Dataset dictionary containing 'Dataset' and 'Coordinates' keys
        target (str): Target variable to plot (must end with '_target')
        title (str, optional): Map title. Defaults to target name.
        zoom_start (int, optional): Initial zoom level. Defaults to 12.

    Returns:
        folium.Map: Interactive map with soil properties
    """
    if 'Coordinates' not in data:
        raise ValueError("Dataset must contain 'Coordinates' key for mapping")
    
    coords = data['Coordinates']
    values = data['Dataset'][target]
    
    x_col = next(col for col in coords.columns if col.startswith('x_'))
    y_col = next(col for col in coords.columns if col.startswith('y_'))
    
    center = [coords[y_col].mean(), coords[x_col].mean()]
    m = folium.Map(location=center, zoom_start=zoom_start)
    
    for y, x, val in zip(coords[y_col], coords[x_col], values):
        folium.CircleMarker(
            location=[y, x],
            radius=8,
            color='black',
            fill=True,
            fillColor=plt.cm.viridis(val/values.max()),
            fillOpacity=0.7,
            popup=f"{target}: {val:.2f}"
        ).add_to(m)
        
    return m

def plot_feature_importance(importance: np.ndarray, feature_names: List[str], title: str = "Feature Importance") -> None:
    """
    Plot feature importance from models.

    Args:
        importance (np.ndarray): Array of feature importance values
        feature_names (list[str]): List of feature names
        title (str, optional): Plot title. Defaults to "Feature Importance".
    """
    sorted_idx = np.argsort(importance)
    pos = np.arange(sorted_idx.shape[0]) + .5
    
    plt.figure(figsize=(10, 6))
    plt.barh(pos, importance[sorted_idx])
    plt.yticks(pos, np.array(feature_names)[sorted_idx])
    plt.xlabel('Importance')
    plt.title(title)
    plt.tight_layout()