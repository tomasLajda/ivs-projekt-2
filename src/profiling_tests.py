"""
@file profiling_tests.py
@brief File containing profiling functionality tests.

@author
- Matúš Csirik (xcsirim00)
@date April 8, 2024
"""

import pytest
import profiling  # replace with the actual name of your module

# Define a custom approx function to use a relative tolerance
def approx(value, rel=1e-1):
    return pytest.approx(value, rel=rel)

def test_basic_profiling():
    numbers = [1, 2, 3, 4, 5]
    expected_std_dev = 1.5811388300841898  # pre-calculated standard deviation for this list
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

def test_profiling_large_input():
    numbers = list(range(1001))  # create a list of 1001 numbers (0-1000)
    expected_std_dev = 289.301524  # pre-calculated standard deviation for this list
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

def test_profiling_single_number():
    numbers = [5]
    expected_std_dev = 0  # standard deviation of a single number is 0
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

def test_profiling_empty_list():
    numbers = []
    with pytest.raises(ValueError):
        profiling.calculate_std_dev(numbers)

def test_profiling_non_numeric_input():
    numbers = [1, 2, 'three', 4, 5]
    with pytest.raises(TypeError):
        profiling.calculate_std_dev(numbers)

def test_profiling_large_numbers():
    numbers = [1e100, 1e101, 1e102]
    expected_std_dev = 5e101  # pre-calculated standard deviation for this list
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

def test_profiling_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    expected_std_dev = 1.5811388300841898  # pre-calculated standard deviation for this list
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

def test_profiling_mixed_positive_negative_numbers():
    numbers = [-1, 2, -3, 4, -5]
    expected_std_dev = 3.7416573867739413  # pre-calculated standard deviation for this list
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

def test_profiling_decimal_numbers():
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    expected_std_dev = 1.7204650534085253  # pre-calculated standard deviation for this list
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

def test_profiling_same_numbers():
    numbers = [5, 5, 5, 5, 5]
    expected_std_dev = 0  # standard deviation of a list with same numbers is 0
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

def test_profiling_zero():
    numbers = [0, 1, 2, 3, 4]
    expected_std_dev = 1.4142135623730951  # pre-calculated standard deviation for this list
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

def test_profiling_list_with_duplicates():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    expected_std_dev = 1.3451854182698108  # pre-calculated standard deviation for this list
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)

# End of profiling_tests.py