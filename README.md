# LimeSoDa

Python package of LimeSoDa. See also the [R package implementation](https://github.com/JonasSchmidinger/LimeSoDa).

Precision Liming Soil Datasets (LimeSoDa) is a collection of 31 datasets from a field- and farm-scale soil mapping context. These datasets are "ready-to-use" for modeling purposes, as they include target soil properties and features in a tidy tabular format. The target soil properties are soil organic matter (SOM) or soil organic carbon (SOC), pH, and clay content, while the features for modeling are dataset-specific. The primary goal of `LimeSoDa` is to enable more reliable benchmarking of machine learning methods in digital soil mapping and pedometrics.

## Installation

Install LimeSoDa from Pypi:
```bash
pip install LimeSoda
```


Install LimeSoDa from source:
```bash
pip install git+https://github.com/a11to1n3/LimeSoDa.git
```

## Quick Start

Get started with LimeSoDa by accessing and exploring a dataset:

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from LimeSoDa import load_dataset
from LimeSoDa.utils import split_dataset

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

print("\nSOC prediction (10-fold CV):")
print(f"Mean R-squared: {mean_r2:.7f}")  # Mean R-squared: 0.7507837
print(f"Mean RMSE: {mean_rmse:.7f}")     # Mean RMSE: 0.2448791
```

## Documentation

For detailed information, visit the [official documentation](https://limesoda.readthedocs.io/en/latest/). You can also find practical usage examples in the [examples](examples/) directory.


## Available Datasets

LimeSoDa includes a diverse collection of datasets, each varying in sample size and geographic focus:

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

## Citation

If you utilize this package in your research, please cite the associated paper:

```bibtex
@misc{schmidinger2025limesodadatasetcollectionbenchmarking,
      title={LimeSoDa: A Dataset Collection for Benchmarking of Machine Learning Regressors in Digital Soil Mapping}, 
      author={J. Schmidinger and S. Vogel and V. Barkov and A. -D. Pham and R. Gebbers and H. Tavakoli and J. Correa and T. R. Tavares and P. Filippi and E. J. Jones and V. Lukas and E. Boenecke and J. Ruehlmann and I. Schroeter and E. Kramer and S. Paetzold and M. Kodaira and A. M. J. -C. Wadoux and L. Bragazza and K. Metzger and J. Huang and D. S. M. Valente and J. L. Safanelli and E. L. Bottega and R. S. D. Dalmolin and C. Farkas and A. Steiger and T. Z. Horst and L. Ramirez-Lopez and T. Scholten and F. Stumpf and P. Rosso and M. M. Costa and R. S. Zandonadi and J. Wetterlind and M. Atzmueller},
      year={2025},
      eprint={2502.20139},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2502.20139}, 
}
```

## License

LimeSoDa is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Contributing

We welcome contributions! Feel free to submit a [Pull Request](https://github.com/a11to1n3/LimeSoDa/pulls) to enhance LimeSoDa.
