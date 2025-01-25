import pytest
import numpy as np
import json
import pandas as pd
from pathlib import Path

FIXTURES_DIR = Path(__file__).parent / "fixtures"

def load_dataset_stats():
    return pd.read_csv(FIXTURES_DIR / "dataset_statistics.csv", index_col=0)

def load_feature_distributions():
    with open(FIXTURES_DIR / "feature_distributions.json") as f:
        return json.load(f)

@pytest.mark.parametrize("dataset", load_dataset_stats().index)
def test_dataset_dimensions(dataset):
    stats = load_dataset_stats()
    row = stats.loc[dataset]
    
    assert row.n_samples > 0
    assert row.n_features > 0
    assert isinstance(row.has_coordinates, (bool, np.bool_))

@pytest.mark.parametrize("dataset", load_dataset_stats().index)
def test_feature_distributions(dataset):
    distributions = load_feature_distributions()
    
    # Check that dataset exists in distributions
    assert dataset in distributions
    
    # Check each feature in this dataset
    for feature, stats in distributions[dataset].items():
        required_stats = ["mean", "std", "min", "max", "median", "25th", "75th"]
        for stat in required_stats:
            assert stat in stats
            assert isinstance(stats[stat], (int, float))
            
        # Basic sanity checks
        assert stats["min"] <= stats["25th"] <= stats["median"] <= stats["75th"] <= stats["max"]
        assert stats["mean"] >= stats["min"] 
        assert stats["mean"] <= stats["max"]
        assert stats["std"] >= 0
