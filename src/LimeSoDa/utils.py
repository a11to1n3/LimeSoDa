"""
This module provides utility functions for working with LimeSoDa datasets.

Functions:
    Data Processing:
        - split_dataset: Split dataset into train/test sets based on folds

    Helper Functions:
        - _check_input_types: Validate input data types
        - _validate_folds: Validate fold indices
"""

import pandas as pd
import numpy as np
from typing import Union, List, Dict, Tuple

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

    # Get all target columns
    all_target_cols = [col for col in dataset.columns if col.endswith('_target')]
    
    # Determine which targets to use
    if targets is not None:
        targets = [targets] if isinstance(targets, str) else targets
        invalid_targets = [t for t in targets if t not in all_target_cols]
        if invalid_targets:
            raise ValueError(f"Invalid targets: {invalid_targets}. Valid targets: {', '.join(all_target_cols)}")
        target_cols = targets
    else:
        target_cols = all_target_cols

    # Remove all target columns from features
    X = dataset.drop(columns=all_target_cols)
    y = dataset[target_cols]

    train_mask = ~np.isin(folds, fold)
    test_mask = np.isin(folds, fold)

    return X[train_mask], X[test_mask], y[train_mask], y[test_mask]
