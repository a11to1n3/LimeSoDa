import sys
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.append(str(src_path))

from pyLimeSoDa.loaders import *
from pyLimeSoDa.utils import split_dataset, calculate_performance

def example_1_single_fold(data=None):
    """Example 1: Single fold, single target prediction"""
    print("\nExample 1: Single Fold, Single Target")
    print("-" * 40)
    
    if data is None:
        data = load_BB_250()
    X_train, X_test, y_train, y_test = split_dataset(data, fold=1, targets='SOC_target')
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    performance = calculate_performance(y_test.values, y_pred)
    print("SOC prediction:")
    print(f"R-squared: {performance['r2']:.3f}")
    print(f"RMSE: {performance['rmse']:.3f}")
    return performance

def example_2_multiple_targets(data=None):
    """Example 2: Multiple folds, multiple targets prediction"""
    print("\nExample 2: Multiple Folds, Multiple Targets")
    print("-" * 40)
    
    if data is None:
        data = load_BB_250()
    X_train, X_test, y_train, y_test = split_dataset(
        data=data,
        fold=[1,2,3],
        targets=['pH_target', 'Clay_target']
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    performance = calculate_performance(y_test.values, y_pred)
    print("pH and Clay prediction:")
    print(f"R-squared: {performance['r2']:.3f}")
    print(f"RMSE: {performance['rmse']:.3f}")
    return performance

def example_3_nested_cv(data=None):
    """Example 3: Nested cross-validation"""
    print("\nExample 3: Nested Cross-Validation")
    print("-" * 40)
    
    if data is None:
        data = load_BB_250()
    outer_scores = []
    inner_cv_scores = []
    
    # Outer loop: 5 folds for testing
    for outer_fold in range(1, 6):
        # Get outer train/test split
        X_outer_train, X_outer_test, y_outer_train, y_outer_test = split_dataset(
            data,
            fold=outer_fold,
            targets='SOC_target',
            n_folds=5
        )
        
        # Inner cross-validation for hyperparameter tuning
        inner_scores = []
        for inner_fold in range(1, 5):
            # Create temporary dataset with outer training data
            inner_data = {
                'Dataset': pd.concat([X_outer_train, y_outer_train], axis=1),
                'Folds': np.array([i % 4 + 1 for i in range(len(X_outer_train))])
            }
            
            X_inner_train, X_inner_val, y_inner_train, y_inner_val = split_dataset(
                inner_data,
                fold=inner_fold,
                targets='SOC_target',
                n_folds=4
            )
            
            # Train and validate on inner fold
            model = LinearRegression()
            model.fit(X_inner_train, y_inner_train)
            y_inner_pred = model.predict(X_inner_val)
            inner_perf = calculate_performance(y_inner_val.values, y_inner_pred)
            inner_scores.append(inner_perf['r2'])
        
        # Train final model on all outer training data
        model = LinearRegression()
        model.fit(X_outer_train, y_outer_train)
        y_outer_pred = model.predict(X_outer_test)
        outer_perf = calculate_performance(y_outer_test.values, y_outer_pred)
        outer_scores.append(outer_perf['r2'])
        inner_cv_scores.append(np.mean(inner_scores))
        
        print(f"\nOuter Fold {outer_fold}:")
        print(f"Inner CV R² scores: {np.mean(inner_scores):.3f} ± {np.std(inner_scores):.3f}")
        print(f"Test R² score: {outer_perf['r2']:.3f}")

    final_score = np.mean(outer_scores)
    final_std = np.std(outer_scores)
    print(f"\nFinal Nested CV R² score: {final_score:.3f} ± {final_std:.3f}")
    return {'outer_scores': outer_scores, 'inner_cv_scores': inner_cv_scores, 
            'final_score': final_score, 'final_std': final_std}

def main():
    """Run all examples"""
    print("pyLimeSoDa Usage Examples")
    print("=" * 40)
    
    # Load and show dataset info
    data = load_BB_250()
    print("Dataset Information:")
    print(f"Features: {[c for c in data['Dataset'].columns if not c.endswith('_target')]}")
    print(f"Targets: {[c for c in data['Dataset'].columns if c.endswith('_target')]}")
    print(f"Sample size: {len(data['Dataset'])}")
    
    # Run examples
    example_1_single_fold(data)
    example_2_multiple_targets(data)
    example_3_nested_cv(data)

if __name__ == "__main__":
    main()
