"""
This module provides functions for loading individual datasets in the Lime_SoDa package.

The datasets are stored as pickle (.pkl) files and are loaded into a consistent structure:
{
    'Dataset': pandas.DataFrame,  # Contains soil properties and features
    'Folds': numpy.ndarray,  # Pre-defined folds for cross-validation
    'Coordinates': pandas.DataFrame or None  # Spatial coordinates if available
}

Functions:
- load_dataset: Load a specific dataset by name
- list_datasets: List all available datasets

Individual dataset loaders (e.g., load_BB_250) are also available but typically called via load_dataset.
"""

from .BB_250 import load_BB_250
from .B_204 import load_B_204
from .BB_30_1 import load_BB_30_1
from .BB_30_2 import load_BB_30_2
from .BB_51 import load_BB_51
from .BB_72 import load_BB_72
from .BC_58 import load_BC_58
from .CV_98 import load_CV_98
from .G_104 import load_G_104
from .H_138 import load_H_138
from .MG_44 import load_MG_44
from .MGS_101 import load_MGS_101
from .MWP_36 import load_MWP_36
from .NRW_115 import load_NRW_115
from .NRW_42 import load_NRW_42
from .NRW_62 import load_NRW_62
from .NSW_52 import load_NSW_52
from .O_32 import load_O_32
from .PC_45 import load_PC_45
from .RP_62 import load_RP_62
from .SA_112 import load_SA_112
from .SC_50 import load_SC_50
from .SC_93 import load_SC_93
from .SL_125 import load_SL_125
from .SM_40 import load_SM_40
from .SP_231 import load_SP_231
from .SSP_460 import load_SSP_460
from .SSP_58 import load_SSP_58
from .UL_120 import load_UL_120
from .W_50 import load_W_50

# Create mapping of dataset names to loader functions
_DATASET_LOADERS = {
    name.replace('load_', '').replace('_', '.'): func
    for name, func in locals().items()
    if name.startswith('load_') and callable(func)
}

def load_dataset(name: str) -> dict:
    """
    Load a dataset by name.

    Args:
        name (str): Name of the dataset to load (e.g., 'BB.250')

    Returns:
        dict: A dictionary containing 'Dataset', 'Folds', and 'Coordinates' keys

    Raises:
        ValueError: If the specified dataset name is not found

    Example:
        >>> BB_250 = load_dataset('BB.250')
        >>> print(BB_250['Dataset'].head())
    """
    if name in _DATASET_LOADERS:
        return _DATASET_LOADERS[name]()
    else:
        raise ValueError(f"Dataset '{name}' not found")

def list_datasets() -> list:
    """
    List all available datasets in the Lime_SoDa package.

    Returns:
        list: A list of dataset names (strings)

    Example:
        >>> datasets = list_datasets()
        >>> print(datasets)
        ['BB.250', 'SP.231', ...]
    """
    return sorted(_DATASET_LOADERS.keys())