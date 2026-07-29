# LimeSoDa

<!-- Package Stats -->
[![PyPI Version](https://img.shields.io/pypi/v/limesoda?label=PyPI&color=blue)](https://pypi.org/project/limesoda/)
[![PyPI Downloads](https://static.pepy.tech/badge/limesoda)](https://pepy.tech/projects/limesoda)
[![Monthly Downloads](https://static.pepy.tech/badge/limesoda/month)](https://pepy.tech/projects/limesoda)
[![Python Versions](https://img.shields.io/pypi/pyversions/limesoda)](https://pypi.org/project/limesoda/)

<!-- Repository Stats -->
[![GitHub Stars](https://img.shields.io/github/stars/a11to1n3/LimeSoDa?style=social)](https://github.com/a11to1n3/LimeSoDa/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/a11to1n3/LimeSoDa?style=social)](https://github.com/a11to1n3/LimeSoDa/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/a11to1n3/LimeSoDa)](https://github.com/a11to1n3/LimeSoDa/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/a11to1n3/LimeSoDa)](https://github.com/a11to1n3/LimeSoDa/pulls)

<!-- License & Citation -->
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.geoderma.2025.117337-blue)](https://doi.org/10.1016/j.geoderma.2025.117337)
[![Paper](https://img.shields.io/badge/Paper-Geoderma-green)](https://www.sciencedirect.com/science/article/pii/S0016706125001752)

<!-- Community -->
[![Contributors](https://img.shields.io/github/contributors/a11to1n3/LimeSoDa)](https://github.com/a11to1n3/LimeSoDa/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/a11to1n3/LimeSoDa)](https://github.com/a11to1n3/LimeSoDa/commits/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/a11to1n3/LimeSoDa/graphs/commit-activity)

Paquete de Python de LimeSoDa. Ver también la [implementación del paquete en R](https://github.com/JonasSchmidinger/LimeSoDa).

Precision Liming Soil Datasets (LimeSoDa) es una colección de 31 conjuntos de datos provenientes de contextos de mapeo de suelos a escala de campo y finca. Estos conjuntos de datos están "listos para usar" con fines de modelado, ya que incluyen propiedades del suelo objetivo y características en un formato tabular ordenado (tidy). Las propiedades del suelo objetivo son la materia orgánica del suelo (SOM) o el carbono orgánico del suelo (SOC), el pH y el contenido de arcilla, mientras que las características para el modelado son específicas de cada conjunto de datos. El objetivo principal de `LimeSoDa` es permitir una comparativa (benchmarking) más fiable de los métodos de aprendizaje automático en el mapeo digital de suelos y pedometría.

## 📊 Características Principales

- **31 conjuntos de datos curados** para el mapeo digital de suelos.
- **Formato tabular listo para usar** con propiedades objetivo y características.
- **Divisiones de CV de 10 pliegues predefinidas** para un benchmarking reproducible.
- **Diversos tipos de características**, incluyendo espectroscopía, teledetección y datos de terreno.
- **Documentación exhaustiva** con ejemplos y tutoriales.

## Instalación

Instalar LimeSoDa desde Pypi:
```bash
pip install LimeSoda
```

Instalar LimeSoDa desde el código fuente:
```bash
pip install git+https://github.com/a11to1n3/LimeSoDa.git
```

## Inicio Rápido

Comienza a utilizar LimeSoDa accediendo y explorando un conjunto de datos:

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from LimeSoDa import load_dataset
from LimeSoDa.utils import split_dataset

# Establecer semilla aleatoria
np.random.seed(2025)

# Cargar conjunto de datos
BB_250 = load_dataset('BB.250')

# Realizar CV de 10 pliegues
y_true_all = []
y_pred_all = []

for fold in range(1, 11):
    X_train, X_test, y_train, y_test = split_dataset(BB_250, fold=fold, targets='SOC_target')
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    y_true_all.extend(y_test.values)
    y_pred_all.extend(y_pred)

# Calcular el rendimiento general
y_true_all = np.array(y_true_all)
y_pred_all = np.array(y_pred_all)
mean_r2 = r2_score(y_true_all, y_pred_all)
mean_rmse = np.sqrt(mean_squared_error(y_true_all, y_pred_all))

print("\nSOC prediction (10-fold CV):")
print(f"Mean R-squared: {mean_r2:.7f}")  # Mean R-squared: 0.7507837
print(f"Mean RMSE: {mean_rmse:.7f}")     # Mean RMSE: 0.2448791
```

## Documentación

Para obtener información detallada, visite la [documentación oficial](https://limesoda.readthedocs.io/en/latest/). También puede encontrar ejemplos prácticos de uso en el directorio [examples](examples/).

## Conjuntos de Datos Disponibles

LimeSoDa incluye una colección diversa de conjuntos de datos, que varían en tamaño de muestra y enfoque geográfico:

| Dataset ID | Tamaño de Muestra | Propiedades Objetivo | Grupos de Características | Coordenadas |
|------------|-------------------|-------------------|--------------------------|-------------|
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
| MG.112 | 112 | SOC, pH, Clay | DEM, ERa, RSS, VI | EPSG:32721 |
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

Los conjuntos de datos comprenden:

- **Conjunto de Datos Principal**: Contiene propiedades del suelo y características.
- **Pliegues de Validación**: Divisiones de validación cruzada de 10 pliegues predefinidas.
- **Coordenadas**: Proporcionadas cuando están disponibles.

## Características

Los siguientes grupos de características están presentes en los conjuntos de datos de LimeSoDa:

- Sensor de humedad del suelo capacitivo (CSMoisture)
- Modelo digital de elevación y parámetros del terreno (DEM)
- Resistividad eléctrica aparente (ERa)
- Actividad de rayos gamma (Gamma)
- Espectroscopía infrarroja media (MIR)
- Espectroscopía infrarroja cercana (NIR)
- Electrodos selectivos de iones para la determinación del pH (pH-ISE)
- Datos espectrales derivados de teledetección (RSS)
- Concentraciones elementales derivadas de fluorescencia de rayos X (XRF)
- Índices de Vegetación (VI)
- Espectroscopía visible e infrarroja cercana (vis-NIR)

## Citación

Si utiliza este paquete en su investigación, por favor cite el artículo asociado:

```bibtex
@article{schmidinger2025limesodadatasetcollectionbenchmarking,
      title={LimeSoDa: A Dataset Collection for Benchmarking of Machine Learning Regressors in Digital Soil Mapping}, 
      author={J. Schmidinger and S. Vogel and V. Barkov and A. -D. Pham and R. Gebbers and H. Tavakoli and J. Correa and T. R. Tavares and P. Filippi and E. J. Jones and V. Lukas and E. Boenecke and J. Ruehlmann and I. Schroeter and E. Kramer and S. Paetzold and M. Kodaira and A. M. J. -C. Wadoux and L. Bragazza and K. Metzger and J. Huang and D. S. M. Valente and J. L. Safanelli and E. L. Bottega and R. S. D. Dalmolin and C. Farkas and A. Steiger and T. Z. Horst and L. Ramirez-Lopez and T. Scholten and F. Stumpf and P. Rosso and M. M. Costa and R. S. Zandonadi and J. Wetterlind and M. Atzmueller},
      year={2025},
      journal = {Geoderma},
      volume = {459},
      pages = {117337},
      issn = {0016-7061},
      doi = {https://doi.org/10.1016/j.geoderma.2025.117337},
      url={https://www.sciencedirect.com/science/article/pii/S0016706125001752},
      publisher={Elsevier}
}
```

## Licencia

LimeSoDa está licenciado bajo [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Contribución

¡Agradecemos las contribuciones! No dude en enviar un [Pull Request](https://github.com/a11to1n3/LimeSoDa/pulls) para mejorar LimeSoDa.
