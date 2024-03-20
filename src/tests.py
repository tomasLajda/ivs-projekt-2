"""
@file tests.py
@brief File containing math library functionality tests.

@author
- Matúš Csirik (xcsirim00)
- Tomáš Lajda (xlajdat00)
@date March 19, 2024
"""
import pytest
import lajdaMath # temp name

def math():
    return lajdaMath()

def test_addition(math):
    assert math.add(1, 2) == 3

