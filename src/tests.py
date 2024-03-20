"""
@file tests.py
@brief File containing math library functionality tests.

@author
- Matúš Csirik (xcsirim00)
- Tomáš Lajda (xlajdat00)
@date March 19, 2024
"""
import pytest
import sys
import lajdaMath  # temp name


def math():
    return lajdaMath()


def test_addition(math):
    assert math.add(1, 2) == 3


# ADDITION TESTS START
def test_addition_float(math):
    assert math.add(0.1, 0.1) == 0.2
    assert math.add(math.add(math.add(
        math.add(math.add(math.add(math.add(math.add(math.add(math.add(0.1, 0.1), 0.1), 0.1), 0.1), 0.1), 0.1)), 0.1),
        0.1), 0.1) == 1


def test_addition_negative(math):
    assert math.add(-1, -2) == -3
    assert math.add(-1, 2) == 1
    assert math.add(1, -2) == -1


def test_addition_zero(math):
    assert math.add(0, 0) == 0
    assert math.add(-0, 0) == 0
    assert math.add(0, -0) == 0
    assert math.add(-0, -0) == 0
    assert math.add(2, 0) == 2
    assert math.add(0, 2) == 2
    assert math.add(-2, 0) == -2
    assert math.add(0, -2) == -2
    assert math.add(2, -2) == 0
    assert math.add(-2, 2) == 0


def test_addition_small(math):
    assert math.add(0.000_000_000_1, 0.000_000_000_2) == 0.000_000_000_3
    assert math.add(0.000_000_1, 0.000_000_2) == 0.000_000_3
    assert math.add(0.000_1, 0.000_2) == 0.000_3


def test_addition_large(math):
    assert math.add(1_000, 2_000) == 3_000
    assert math.add(1_000_000, 2_000_000) == 3_000_000
    assert math.add(1_000_000_000_000, 2_000_000_000_000) == 3_000_000_000_000


def test_addition_small_negative(math):
    assert math.add(-0.000_000_000_1, -0.000_000_000_2) == -0.000_000_000_3
    assert math.add(-0.000_000_1, -0.000_000_2) == -0.000_000_3
    assert math.add(-0.000_1, -0.000_2) == -0.000_3


def test_addition_large_negative(math):
    assert math.add(-1_000, -2_000) == -3_000
    assert math.add(-1_000_000, -2_000_000) == -3_000_000
    assert math.add(-1_000_000_000_000, -2_000_000_000_000) == -3_000_000_000_000


# ADDITION TESTS END
# SUBTRACTION TESTS START
def test_subtraction(math):
    assert math.sub(1, 1) == 0


def test_subtraction_float(math):
    assert math.sub(0.1, 2) == -1.9
    assert math.sub(math.sub(math.sub(
        math.sub(math.sub(math.sub(math.sub(math.sub(math.sub(math.sub(1, 0, 1), 0, 1), 0, 1), 0, 1), 0, 1), 0, 1), 0,
                 1), 0, 1), 0, 1), 0, 1) == 0


def test_subtraction_negative(math):
    assert math.sub(-1, -1) == 0
    assert math.sub(-1, -2) == 1
    assert math.sub(-1, 2) == -3
    assert math.sub(1, -2) == 3


def test_subtraction_zero(math):
    assert math.sub(0, 0) == 0
    assert math.sub(-0, 0) == 0
    assert math.sub(0, -0) == 0
    assert math.sub(-0, -0) == 0
    assert math.sub(2, 0) == 2
    assert math.sub(0, 2) == -2
    assert math.sub(-2, 0) == -2
    assert math.sub(0, -2) == 2
    assert math.sub(2, -2) == 4
    assert math.sub(-2, 2) == -4
    assert math.sub(2, 2) == 0


def test_subtraction_small(math):
    assert math.sub(0.000_000_000_1, 0.000_000_000_2) == -0.000_000_000_1
    assert math.sub(0.000_000_1, 0.000_000_2) == -0.000_000_1
    assert math.sub(0.000_1, 0.000_2) == -0.000_1


def test_subtraction_large(math):
    assert math.sub(1_000, 2_000) == -1_000
    assert math.sub(1_000_000, 2_000_000) == -1_000_000
    assert math.sub(1_000_000_000_000, 2_000_000_000_000) == -1_000_000_000_000


def test_subtraction_small_negative(math):
    assert math.sub(-0.000_000_000_1, -0.000_000_000_2) == 0.000_000_000_1
    assert math.sub(-0.000_000_1, -0.000_000_2) == 0.000_000_1
    assert math.sub(-0.000_1, -0.000_2) == 0.000_1


def test_subtraction_large_negative(math):
    assert math.sub(-1_000, -2_000) == -3_000
    assert math.sub(-1_000_000, -2_000_000) == -3_000_000
    assert math.sub(-1_000_000_000_000, -2_000_000_000_000) == -3_000_000_000_000

# SUBTRACTION TESTS END
