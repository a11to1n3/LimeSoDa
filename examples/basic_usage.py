import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from LimeSoDa import load_dataset
from LimeSoDa.utils import split_dataset

def basic_usage():
    """Basic usage example with 10-fold CV"""
    # Set random seed
    np.random.seed(2025)
    
    # Load dataset
    BB_250 = load_dataset('BB.250')

    # Perform 10-fold CV
    y_true_all = []
    y_pred_all = []
    
    for fold in range(1, 11):
        X_train, X_test, y_train, y_test = split_dataset(BB_250, fold=fold, targets='SOC_target')
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        y_true_all.extend(y_test.values)
        y_pred_all.extend(y_pred)

    # Calculate overall performance
    y_true_all = np.array(y_true_all)
    y_pred_all = np.array(y_pred_all)
    mean_r2 = r2_score(y_true_all, y_pred_all)
    mean_rmse = np.sqrt(mean_squared_error(y_true_all, y_pred_all))
    std_r2 = 0  # Need bootstrapping for proper std calculation
    std_rmse = 0  # Need bootstrapping for proper std calculation

    return mean_r2, std_r2, mean_rmse, std_rmse

if __name__ == "__main__":
    mean_r2, std_r2, mean_rmse, std_rmse = basic_usage()
    print("\nSOC prediction (10-fold CV):")
    print(f"Mean R-squared: {mean_r2:.7f} ± {std_r2:.7f}")
    print(f"Mean RMSE: {mean_rmse:.7f} ± {std_rmse:.7f}")
