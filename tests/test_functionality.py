import sys
import os
from pathlib import Path
import pytest

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.append(str(src_path))

from LimeSoDa.loaders import *
from LimeSoDa.utils import *

@pytest.fixture
def loader_list():
    return [
        (lambda: load_dataset(name="BB.250"), "BB.250"),
        (lambda: load_dataset(name="BB.30_1"), "BB.30_1"),
        (lambda: load_dataset(name="BB.30_2"), "BB.30_2"),
        (lambda: load_dataset(name="BB.51"), "BB.51"),
        (lambda: load_dataset(name="BB.72"), "BB.72"),
        (lambda: load_dataset(name="B.204"), "B.204"),
        (lambda: load_dataset(name="CV.98"), "CV.98"),
        (lambda: load_dataset(name="G.104"), "G.104"),
        (lambda: load_dataset(name="G.150"), "G.150"),
        (lambda: load_dataset(name="H.138"), "H.138"),
        (lambda: load_dataset(name="MG.44"), "MG.44"),
        (lambda: load_dataset(name="MG.112"), "MG.112"),
        (lambda: load_dataset(name="MGS.101"), "MGS.101"),
        (lambda: load_dataset(name="MWP.36"), "MWP.36"),
        (lambda: load_dataset(name="NRW.42"), "NRW.42"),
        (lambda: load_dataset(name="NRW.62"), "NRW.62"),
        (lambda: load_dataset(name="NRW.115"), "NRW.115"),
        (lambda: load_dataset(name="NSW.52"), "NSW.52"),
        (lambda: load_dataset(name="O.32"), "O.32"),
        (lambda: load_dataset(name="PC.45"), "PC.45"),
        (lambda: load_dataset(name="RP.62"), "RP.62"),
        (lambda: load_dataset(name="SA.112"), "SA.112"),
        (lambda: load_dataset(name="SC.50"), "SC.50"),
        (lambda: load_dataset(name="SC.93"), "SC.93"),
        (lambda: load_dataset(name="SL.125"), "SL.125"),
        (lambda: load_dataset(name="SM.40"), "SM.40"),
        (lambda: load_dataset(name="SP.231"), "SP.231"),
        (lambda: load_dataset(name="SSP.58"), "SSP.58"),
        (lambda: load_dataset(name="SSP.460"), "SSP.460"),
        (lambda: load_dataset(name="UL.120"), "UL.120"),
        (lambda: load_dataset(name="W.50"), "W.50")
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