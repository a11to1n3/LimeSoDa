import pytest
import numpy as np
from examples.basic_usage import basic_usage
from examples.advanced_usage import (
    example_single_fold_single_target,
    example_multiple_folds_single_target, 
    example_single_fold_multiple_targets,
    example_multiple_folds_multiple_targets,
    example_custom_folds,
    example_visualization
)
import folium

def test_basic_usage():
    """Test basic usage example with 10-fold CV"""
    mean_r2, std_r2, mean_rmse, std_rmse = basic_usage()
    assert isinstance(mean_r2, float)
    assert isinstance(std_r2, float)
    assert isinstance(mean_rmse, float)
    assert isinstance(std_rmse, float)
    assert 0 <= mean_r2 <= 1
    assert std_r2 >= 0
    assert mean_rmse >= 0
    assert std_rmse >= 0

def test_single_fold_single_target():
    """Test single fold and single target example"""
    perf, model, (X_train, X_test, y_train, y_test) = example_single_fold_single_target()
    assert isinstance(perf, dict)
    assert 'r2' in perf and 'rmse' in perf
    assert 0 <= perf['r2'] <= 1
    assert perf['rmse'] >= 0
    assert hasattr(model, 'fit') and hasattr(model, 'predict')
    assert len(X_train) > 0 and len(X_test) > 0
    assert len(y_train) > 0 and len(y_test) > 0

def test_multiple_folds_single_target():
    """Test multiple folds and single target example"""
    perf, model, (X_train, X_test, y_train, y_test) = example_multiple_folds_single_target()
    assert isinstance(perf, dict)
    assert 'r2' in perf and 'rmse' in perf
    assert 0 <= perf['r2'] <= 1
    assert perf['rmse'] >= 0

def test_single_fold_multiple_targets():
    """Test single fold and multiple targets example"""
    perf, model, (X_train, X_test, y_train, y_test) = example_single_fold_multiple_targets()
    assert isinstance(perf, dict)
    assert 'r2' in perf and 'rmse' in perf
    assert 0 <= perf['r2'] <= 1
    assert perf['rmse'] >= 0
    assert y_train.shape[1] > 1  # Multiple targets

def test_multiple_folds_multiple_targets():
    """Test multiple folds and multiple targets example"""
    perf, model, (X_train, X_test, y_train, y_test) = example_multiple_folds_multiple_targets()
    assert isinstance(perf, dict)
    assert 'r2' in perf and 'rmse' in perf
    assert 0 <= perf['r2'] <= 1
    assert perf['rmse'] >= 0
    assert y_train.shape[1] > 1  # Multiple targets

def test_custom_folds():
    """Test custom folds example"""
    perf, model, (X_train, X_test, y_train, y_test) = example_custom_folds()
    assert isinstance(perf, dict)
    assert 'r2' in perf and 'rmse' in perf
    assert 0 <= perf['r2'] <= 1
    assert perf['rmse'] >= 0

def test_visualization():
    """Test visualization example"""
    soil_map, importance_plot = example_visualization()
    # Maps may be None if no coordinates available
    if soil_map is not None:
        assert isinstance(soil_map, folium.folium.Map)
    if importance_plot is not None:
        assert isinstance(importance_plot, np.ndarray)
