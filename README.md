# pyLimeSoDa

[![Python Package](https://github.com/a11to1n3/pyLimeSoDa/actions/workflows/python-package.yml/badge.svg)](https://github.com/a11to1n3/pyLimeSoDa/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/a11to1n3/pyLimeSoDa/branch/main/graph/badge.svg)](https://codecov.io/gh/a11to1n3/pyLimeSoDa)

Precision Liming Soil Datasets (LimeSoDa) is a collection of datasets from a field- and farm-scale soil mapping context and this is the associated python dataset package **pyLimeSoDa**. These datasets are 'ready-to-go' for modeling purposes, as they contain target soil properties and features in a tabular format. Target soil properties for all datasets are; soil organic matter (SOM) or -carbon (SOC), pH and clay, while the features for modeling are dataset-specific. The goal of LimeSoDa is to enable more reliable benchmarking and comparison of various modeling approaches in Digital Soil Mapping and Pedometrics by providing an open collection of multiple datasets. 

## Installation

Install pyLimeSoDa via pip:
```bash
pip install pyLimeSoDa
```

Or directly from GitHub:

```bash
pip install git+https://github.com/a11to1n3/pyLimeSoDa.git
```

## Quick Start

Get started with pyLimeSoDa by accessing and exploring a dataset:

```python
import pyLimeSoDa as pls
from pyLimeSoDa.utils import split_dataset, calculate_performance
from sklearn.linear_model import LinearRegression
import numpy as np

# Load a dataset
BB_250 = pls.load_dataset('BB.250')

# Print dataset information
print(BB_250['Dataset'].head())
print(BB_250['Folds'])
if BB_250['Coordinates'] is not None:
    print(BB_250['Coordinates'].head())

# Example 1: Single fold, single target
# Split data using fold 1 and SOC_target
X_train, X_test, y_train, y_test = split_dataset(BB_250, fold=1, targets='SOC_target')

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

performance = calculate_performance(y_test, y_pred)
print("\nSingle fold, SOC prediction:")
print(f"R-squared: {performance['r2']:.3f}")
print(f"RMSE: {performance['rmse']:.3f}")

# Example 2: Multiple folds, multiple targets
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

# Example 3: Nested Cross-Validation
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
```

## Available Datasets

pyLimeSoDa includes a diverse collection of datasets, each varying in sample size and geographic focus:

| Dataset ID | Sample Size | Target Properties | Feature Groups | Coordinates |
|------------|-------------|-------------------|----------------|-------------|
| B.204 | 204 | SOC, pH, Clay | DEM, RSS, VI | EPSG:32723 |
| BB.250 | 250 | SOC, pH, Clay | DEM, ERa, Gamma, pH-ISE, RSS, VI | EPSG:25833 |
| BB.30_1 | 30 | SOC, pH, Clay | DEM, ERa, pH-ISE, VI | EPSG:25833 |
| BB.30_2 | 30 | SOC, pH, Clay | DEM, ERa, Gamma, RSS, VI | EPSG:25833 |
| BB.51 | 51 | SOC, pH, Clay | DEM, ERa, pH-ISE | EPSG:25833 |
| BB.72 | 72 | SOC, pH, Clay | DEM, ERa, Gamma, pH-ISE, RSS, VI | EPSG:25833 |
| CV.98 | 98 | SOC, pH, Clay | vis-NIR | NA |
| G.104 | 104 | SOC, pH, Clay | DEM, RSS, VI | EPSG:32722 |
| G.150 | 150 | SOC, pH, Clay | DEM, ERa, RSS, VI | EPSG:32722 |
| H.138 | 138 | SOC, pH, Clay | MIR | EPSG:32649 |
| MG.112 | 112 | SOC, pH, Clay |  DEM, ERa, RSS, VI | EPSG:32721 |
| MG.44 | 44 | SOC, pH, Clay | vis-NIR | EPSG:32721 |
| MGS.101 | 101 | SOC, pH, Clay | DEM, RSS, VI | EPSG:32721 |
| MWP.36 | 36 | SOC, pH, Clay | DEM, RSS | EPSG:32633 |
| NRW.115 | 115 | SOC, pH, Clay | MIR | NA |
| NRW.42 | 42 | SOC, pH, Clay | MIR | NA |
| NRW.62 | 62 | SOC, pH, Clay | MIR | NA |
| NSW.52 | 52 | SOC, pH, Clay | DEM, RSS | EPSG:32755 |
| O.32 | 32 | SOC, pH, Clay | MIR | NA |
| PC.45 | 45 | SOC, pH, Clay | CSMoist, ERa | NA |
| RP.62 | 62 | SOC, pH, Clay | ERa, Gamma, NIR, pH-ISE, VI | NA |
| SA.112 | 112 | SOC, pH, Clay | DEM, ERa, Gamma, NIR, pH-ISE, VI | NA |
| SC.50 | 50 | SOC, pH, Clay | DEM, ERa | EPSG:32722 |
| SC.93 | 93 | SOC, pH, Clay | vis-NIR | EPSG:32722 |
| SL.125 | 125 | SOM, pH, Clay | ERa, vis-NIR | EPSG:4326 (dummy) |
| SM.40 | 40 | SOC, pH, Clay | DEM, ERa | EPSG:32633 |
| SP.231 | 125 | SOM, pH, Clay | vis-NIR | EPSG:32654 |
| SSP.460 | 460 | SOC, pH, Clay | vis-NIR | NA |
| SSP.58 | 58 | SOC, pH, Clay | vis-NIR | NA |
| UL.120 | 120 | SOM, pH, Clay | ERa, vis-NIR | EPSG:4326 (dummy) |
| W.50 | 50 | SOC, pH, Clay | DEM, ERa, VI, XRF | NA |

Datasets comprise:

- **Main Dataset**: Contains soil properties and features
- **Validation Folds**: Pre-defined 10-fold cross-validation splits
- **Coordinates**: Provided where available

## Features
The following groups of features are present in datasets of LimeSoDa:

- Capacitive soil moisture sensor (CSMoisture)
- Digital elevation model and terrain parameters (DEM)
- Apparent electrical resistivity (ERa)
- Gamma-ray activity (Gamma)
- Mid infrared spectroscopy (MIR)
- Near infrared spectroscopy (NIR)
- Ion selective electrodes for pH determination (pH-ISE)
- Remote sensing derived spectral data (RSS)
- X-ray fluorescence derived elemental concentrations (XRF)
- Vegetation Indices (VI)
- Visible- and near infrared spectroscopy (vis-NIR)



## Documentation

Comprehensive documentation and usage examples are available in the [examples](examples/) directory.

## Citation

If you utilize this package in your research, please cite the associated paper:

```bibtex
@article{schmidinger2025limesoda,
    title={LimeSoDa: An open dataset collection for machine learning benchmarking in digital soil mapping},
    author={Schmidinger, J. and Others},
    journal={XXX},
    year={2025}
}
```

## License

LimeSoDa is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Contributing

We welcome contributions! Feel free to submit a [Pull Request](https://github.com/JonasSchmidinger/pyLimeSoDa/pulls) to enhance LimeSoDa.
