import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from LimeSoDa import load_dataset
from LimeSoDa.utils import split_dataset, calculate_performance

def basic_usage():
    """Basic usage example with 10-fold CV"""
    # Set random seed
    np.random.seed(2025)
    
    # Load dataset
    BB_250 = load_dataset('BB.250')

    # Perform 10-fold CV
    r2_scores = []
    rmse_scores = []
    
    for fold in range(1, 11):
        X_train, X_test, y_train, y_test = split_dataset(BB_250, fold=fold, targets='SOC_target')
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        performance = calculate_performance(y_test, y_pred)
        r2_scores.append(performance['r2'])
        rmse_scores.append(performance['rmse'])

    mean_r2 = np.mean(r2_scores)
    std_r2 = np.std(r2_scores)
    mean_rmse = np.mean(rmse_scores)
    std_rmse = np.std(rmse_scores)

    return mean_r2, std_r2, mean_rmse, std_rmse

if __name__ == "__main__":
    mean_r2, std_r2, mean_rmse, std_rmse = basic_usage()
    print("\nSOC prediction (10-fold CV):")
    print(f"Mean R-squared: {mean_r2:.3f} ± {std_r2:.3f}")
    print(f"Mean RMSE: {mean_rmse:.3f} ± {std_rmse:.3f}")