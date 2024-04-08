"""
@file profiling_tests.py
@brief File containing profiling functionality tests.

@author
- Matúš Csirik (xcsirim00)
@date April 8, 2024
"""

import pytest
import profiling  # replace with the actual name of your module

def test_profiling():
    numbers = [1, 2, 3, 4, 5]
    expected_std_dev = 1.5811388300841898  # pre-calculated standard deviation for this list
    assert profiling.calculate_std_dev(numbers) == pytest.approx(expected_std_dev)
