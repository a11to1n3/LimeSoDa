Usage Examples
==============

This section provides detailed examples of how to use the pyLimeSoDa package for various soil mapping tasks.

Basic Usage
-----------

First, let's import the necessary modules and load a dataset:

.. code-block:: python

   import pyLimeSoDa as pls
   from pyLimeSoDa.utils import split_dataset, calculate_performance
   from sklearn.linear_model import LinearRegression
   import numpy as np
   import pandas as pd

   # Load a dataset
   BB_250 = pls.load_dataset('BB.250')

   # Print dataset information
   print(BB_250['Dataset'].head())
   print(BB_250['Folds'])
   if BB_250['Coordinates'] is not None:
       print(BB_250['Coordinates'].head())

Example 1: Single Fold, Single Target
-------------------------------------

In this example, we'll use a single fold and predict the SOC_target:

.. code-block:: python

   # Split data using fold 1 and SOC_target
   X_train, X_test, y_train, y_test = split_dataset(BB_250, fold=1, targets='SOC_target')
   model = LinearRegression()
   model.fit(X_train, y_train)
   y_pred = model.predict(X_test)
   performance = calculate_performance(y_test, y_pred)
   print("\nSingle fold, SOC prediction:")
   print(f"R-squared: {performance['r2']:.3f}")
   print(f"RMSE: {performance['rmse']:.3f}")

Example 2: Multiple Folds, Multiple Targets
-------------------------------------------

Here, we'll use multiple folds and predict both pH and clay targets:

.. code-block:: python

   # Split data using folds 1-3 and both pH and clay targets
   X_train, X_test, y_train, y_test = split_dataset(
       data=BB_250,
       fold=[1,2,3],
       targets=['pH_target', 'Clay_target']
   )
   model = LinearRegression()
   model.fit(X_train, y_train)
   y_pred = model.predict(X_test)
   performance = calculate_performance(y_test, y_pred)
   print("\nMultiple folds, pH and Clay prediction:")
   print(f"R-squared: {performance['r2']:.3f}")
   print(f"RMSE: {performance['rmse']:.3f}")

Example 3: Nested Cross-Validation
----------------------------------

This example demonstrates a more advanced technique using nested cross-validation:

.. code-block:: python

   # Outer loop: 5 folds for testing
   # Inner loop: 4 folds for validation
   outer_scores = []
   for outer_fold in range(1, 6):
       # Get outer train/test split
       X_outer_train, X_outer_test, y_outer_train, y_outer_test = split_dataset(
           BB_250,
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
           inner_perf = calculate_performance(y_inner_val, y_inner_pred)
           inner_scores.append(inner_perf['r2'])
       
       # Train final model on all outer training data
       model = LinearRegression()
       model.fit(X_outer_train, y_outer_train)
       y_outer_pred = model.predict(X_outer_test)
       outer_perf = calculate_performance(y_outer_test, y_outer_pred)
       outer_scores.append(outer_perf['r2'])
       
       print(f"\nOuter Fold {outer_fold}:")
       print(f"Inner CV R² scores: {np.mean(inner_scores):.3f} ± {np.std(inner_scores):.3f}")
       print(f"Test R² score: {outer_perf['r2']:.3f}")

   print(f"\nFinal Nested CV R² score: {np.mean(outer_scores):.3f} ± {np.std(outer_scores):.3f}")

These examples demonstrate various ways to use the pyLimeSoDa package, from simple single-fold, single-target predictions to more complex nested cross-validation scenarios. They showcase the flexibility of the `split_dataset` function and how it can be used with different machine learning workflows.