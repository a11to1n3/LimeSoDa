import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
from LimeSoDa import load_dataset
from LimeSoDa.utils import split_dataset, calculate_performance, plot_soil_map, plot_feature_importance

def example_single_fold_single_target():
    """Example using single fold and single target"""
    data = load_dataset('BB.250')
    
    # Split using fold 1 and SOC target
    X_train, X_test, y_train, y_test = split_dataset(
        data=data,
        fold=1, 
        targets='SOC_target'
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train.values.ravel())
    y_pred = model.predict(X_test)
    performance = calculate_performance(y_test.values.ravel(), y_pred)
    
    return performance, model, (X_train, X_test, y_train, y_test)

def example_multiple_folds_single_target():
    """Example using multiple folds and single target"""
    data = load_dataset('BB.250')
    
    # Split using folds 1-3 and SOC target 
    X_train, X_test, y_train, y_test = split_dataset(
        data=data,
        fold=[1,2,3],
        targets='SOC_target'
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train.values.ravel())
    y_pred = model.predict(X_test)
    performance = calculate_performance(y_test.values.ravel(), y_pred)
    
    return performance, model, (X_train, X_test, y_train, y_test)

def example_single_fold_multiple_targets():
    """Example using single fold and multiple targets"""
    data = load_dataset('BB.250')
    
    # Split using fold 1 and multiple targets
    X_train, X_test, y_train, y_test = split_dataset(
        data=data,
        fold=1,
        targets=['pH_target', 'SOC_target', 'Clay_target']
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train.values)
    y_pred = model.predict(X_test)
    performance = calculate_performance(y_test.values, y_pred)
    
    return performance, model, (X_train, X_test, y_train, y_test)

def example_multiple_folds_multiple_targets():
    """Example using multiple folds and multiple targets"""
    data = load_dataset('BB.250')
    
    # Split using folds 1-3 and multiple targets
    X_train, X_test, y_train, y_test = split_dataset(
        data=data,
        fold=[1,2,3],
        targets=['pH_target', 'SOC_target']
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train.values)
    y_pred = model.predict(X_test)
    performance = calculate_performance(y_test.values, y_pred)
    
    return performance, model, (X_train, X_test, y_train, y_test)

def example_custom_folds():
    """Example using custom number of folds"""
    data = load_dataset('BB.250')
    
    # Split using fold 1 with 5 total folds
    X_train, X_test, y_train, y_test = split_dataset(
        data=data,
        fold=1,
        targets='SOC_target',
        n_folds=5
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train.values.ravel())
    y_pred = model.predict(X_test)
    performance = calculate_performance(y_test.values.ravel(), y_pred)
    
    return performance, model, (X_train, X_test, y_train, y_test)

def example_visualization():
    """Example showing visualization of results"""
    data = load_dataset('BB.250')
    
    # Get model and predictions
    _, model, (X_train, _, _, _) = example_single_fold_single_target()
    
    # Generate visualizations if coordinates available
    soil_map = None
    importance_plot = None
    
    if data.get('Coordinates') is not None:
        soil_map = plot_soil_map(data, 'SOC_target', title='SOC Distribution')
        
    feature_names = X_train.columns
    importances = model.coef_ if hasattr(model, 'coef_') else model.feature_importances_
    importance_plot = plot_feature_importance(importances, feature_names)
    
    return soil_map, importance_plot

if __name__ == "__main__":
    np.random.seed(2025)
    
    print("\nSingle fold, single target:")
    perf, _, _ = example_single_fold_single_target()
    print(f"R²: {perf['r2']:.3f}, RMSE: {perf['rmse']:.3f}")
    
    print("\nMultiple folds, single target:")
    perf, _, _ = example_multiple_folds_single_target()
    print(f"R²: {perf['r2']:.3f}, RMSE: {perf['rmse']:.3f}")
    
    print("\nSingle fold, multiple targets:")
    perf, _, _ = example_single_fold_multiple_targets()
    print(f"R²: {perf['r2']:.3f}, RMSE: {perf['rmse']:.3f}")
    
    print("\nMultiple folds, multiple targets:")
    perf, _, _ = example_multiple_folds_multiple_targets()
    print(f"R²: {perf['r2']:.3f}, RMSE: {perf['rmse']:.3f}")
    
    print("\nCustom folds:")
    perf, _, _ = example_custom_folds()
    print(f"R²: {perf['r2']:.3f}, RMSE: {perf['rmse']:.3f}")
