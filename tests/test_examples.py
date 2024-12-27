import pytest
from examples.basic_usage import example_1_single_fold, example_2_multiple_targets, example_3_nested_cv

def test_example_1():
    """Test single fold example"""
    perf = example_1_single_fold()
    assert 'r2' in perf
    assert 'rmse' in perf
    assert -1 <= perf['r2'] <= 1
    assert perf['rmse'] >= 0

def test_example_2():
    """Test multiple targets example"""
    perf = example_2_multiple_targets()
    assert 'r2' in perf
    assert 'rmse' in perf
    assert -1 <= perf['r2'] <= 1
    assert perf['rmse'] >= 0

def test_example_3():
    """Test nested CV example"""
    results = example_3_nested_cv()
    assert 'outer_scores' in results
    assert 'inner_cv_scores' in results
    assert 'final_score' in results
    assert 'final_std' in results
    assert len(results['outer_scores']) == 5
    assert len(results['inner_cv_scores']) == 5
    assert -1 <= results['final_score'] <= 1
    assert results['final_std'] >= 0
