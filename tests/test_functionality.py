import sys
import os
from pathlib import Path
import pytest

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.append(str(src_path))

from pyLimeSoDa.loaders import *
from pyLimeSoDa.utils import *

@pytest.fixture
def loader_list():
    return [
        (load_B_204, "B_204"),
        (load_BB_30_1, "BB_30_1"),
        (load_BB_30_2, "BB_30_2"), 
        (load_BB_51, "BB_51"),
        (load_BB_72, "BB_72"),
        (load_BB_250, "BB_250"),
        (load_BC_58, "BC_58"),
        (load_CV_98, "CV_98"),
        (load_G_104, "G_104"),
        (load_H_138, "H_138"),
        (load_MG_44, "MG_44"),
        (load_MGS_101, "MGS_101"),
        (load_MWP_36, "MWP_36"),
        (load_NRW_42, "NRW_42"),
        (load_NRW_62, "NRW_62"),
        (load_NRW_115, "NRW_115"),
        (load_NSW_52, "NSW_52"),
        (load_O_32, "O_32"),
        (load_PC_45, "PC_45"),
        (load_RP_62, "RP_62"),
        (load_SA_112, "SA_112"),
        (load_SC_50, "SC_50"),
        (load_SC_93, "SC_93"),
        (load_SL_125, "SL_125"),
        (load_SM_40, "SM_40"),
        (load_SP_231, "SP_231"),
        (load_SSP_58, "SSP_58"),
        (load_SSP_460, "SSP_460"),
        (load_UL_120, "UL_120"),
        (load_W_50, "W_50")
    ]

def test_loader(loader_list):
    for loader_func, name in loader_list:
        data = loader_func()
        # Basic structure tests
        assert isinstance(data, dict), "Data should be a dictionary"
        assert 'Dataset' in data, "Data should have 'Dataset' key"
        assert 'Folds' in data, "Data should have 'Folds' key"
        assert len(data['Dataset']) > 0, "Dataset should not be empty"
        assert set(range(1,11)) <= set(data['Folds'].flatten()), "Folds should contain values 1-10"
        
        # Target variables tests
        targets = [col for col in data['Dataset'].columns if col.endswith('_target')]
        assert len(targets) > 0, f"{name} should have target variables"
        
        # Coordinates test if available
        if 'Coordinates' not in data or data['Coordinates'] is None or data['Coordinates'].shape[1] < 2:
            continue
        assert isinstance(data['Coordinates'], pd.DataFrame), f"{name} coordinates should be a DataFrame"
        assert len(data['Coordinates']) == len(data['Dataset']), f"{name} coordinates length should match dataset"

@pytest.fixture
def sample_data(loader_list):
    # Get first successful dataset
    for loader_func, _ in loader_list:
        try:
            data = loader_func()
            return data
        except:
            continue
    pytest.skip("No dataset could be loaded")

def test_split_dataset(sample_data):
    X_train, X_test, y_train, y_test = split_dataset(sample_data, fold=1)
    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(y_train) > 0 
    assert len(y_test) > 0

def test_calculate_performance(sample_data):
    X_train, X_test, y_train, y_test = split_dataset(sample_data, fold=1)
    y_pred = [0.5] * len(y_test)  # Using a list instead of numpy array
    metrics = calculate_performance(y_test.iloc[:,0], y_pred)
    assert 'r2' in metrics
    assert 'rmse' in metrics

def test_plot_feature_importance(sample_data):
    X_train, X_test, y_train, y_test = split_dataset(sample_data, fold=1)
    importance = np.array([0.5] * X_train.shape[1])  # Convert to numpy array
    plot_feature_importance(importance, X_train.columns)

def test_plot_soil_map(sample_data):
    if 'Coordinates' in sample_data and sample_data['Coordinates'] is not None:
        if any('x_' in col for col in sample_data['Coordinates'].columns) and any('y_' in col for col in sample_data['Coordinates'].columns):
            m = plot_soil_map(sample_data, sample_data['Dataset'].columns[-1])
            assert m is not None
        else:
            pytest.skip("No x_coord/y_coord columns available")
    else:
        pytest.skip("No coordinates available")