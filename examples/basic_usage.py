import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from LimeSoDa import load_dataset
from LimeSoDa.utils import split_dataset


def basic_usage():
    """Basic usage example with 10-fold CV"""
    # Set random seed
    np.random.seed(2025)

    # Load dataset
    BB_250 = load_dataset("BB.250")

    # Perform 10-fold CV
    y_true_all = []
    y_pred_all = []

    for fold in range(1, 11):
        X_train, X_test, y_train, y_test = split_dataset(
            BB_250,
            fold=fold,
            targets="SOC_target",
        )

        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        y_true_all.extend(y_test.values)
        y_pred_all.extend(y_pred)

    # Calculate overall performance
    mean_r2 = r2_score(y_true_all, y_pred_all)
    mean_rmse = np.sqrt(mean_squared_error(y_true_all, y_pred_all))

    return mean_r2, mean_rmse


if __name__ == "__main__":
    mean_r2, mean_rmse = basic_usage()
    print("\nSOC prediction (10-fold CV):")
    print(f"Mean R-squared: {mean_r2:.7f}")
    print(f"Mean RMSE: {mean_rmse:.7f}")
