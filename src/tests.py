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
    assert math.sub(-1_000, -2_000) == 1_000
    assert math.sub(-1_000_000, -2_000_000) == 1_000_000
    assert math.sub(-1_000_000_000_000, -2_000_000_000_000) == 1_000_000_000_000

# SUBTRACTION TESTS END
# MULTIPLICATION TESTS START

def test_multiplication(math):
    assert math.mul(5, 2) == 10;


def test_multiplication_zero(math):
    assert math.mul(0, 1) == 0
    assert math.mul(1, 0) == 0
    assert math.mul(0, 0) == 0


def test_multiplication_negative(math):
    assert math.mul(-1, 2) == -2
    assert math.mul(1, -2) == -2
    assert math.mul(-1, -2) == 2


def test_multiplication_float(math):
    assert math.mul(1.1 * 10) == 11
    assert math.mul(1.1 * 1) == 1.1
    assert math.mul(0.5 * 10) == 5


def test_multiplication_small(math):
    assert math.mul(0.000_000_000_1, 0.000_000_000_2) == 0.000_000_000_000_000_000_02
    assert math.mul(0.000_000_000_1, 2) == 0.000_000_000_2


def test_multiplication_large(math):
    assert math.mul(1_000_000_000_000, 2_000_000_000_000) == 2_000_000_000_000_000_000_000_000
    assert math.mul(1_000_000_000_000, 2) == 2_000_000_000_000


# MULTIPLICATION TESTS END
# DIVISION TESTS START

def test_division(math):
    assert math.div(4, 2) == 2


def test_division_zero(math):
    with pytest.raises(ValueError):
        math.div(4, 0)


def test_division_negative(math):
    assert math.div(2, -1) == -1
    assert math.div(-2, 1) == -1
    assert math.div(-2, -1) == 1


def test_division_float(math):
    assert math.div(1, 2) == 0.5
    assert math.div(1, 100) == 0.01
    assert math.div(3, 90) == 0.05


def test_division_periodic(math):
    assert math.div(1, 3) == pytest.approx(0.3333, rel=1e-4)
    assert math.div(2, 7) == pytest.approx(0.2857, rel=1e-4)
    assert math.div(1, 6) == pytest.approx(0.1667, rel=1e-4)
    # 1e-4 is scientific notation for 0.0001.
    # It represents a relative tolerance of 0.01%
    # (or 0.0001 as a decimal) of the expected value.


def test_division_small(math):
    assert math.div(0.000_000_000_1, 0.000_000_000_2) == 0.5
    assert math.div(0.000_000_000_1, 2) == 0.000_000_000_2
    assert math.div(2, 0.000_000_000_1) == 20_000_000_000


def test_division_large(math):
    assert math.div(1_000_000_000, 2_000_000_000) == 0.5
    assert math.div(1_000_000_000, 2) == 500_000_000
    assert math.div(2, 1_000_000_000) == 0.000_000_002


# DIVISION TESTS END
# ABSOLUTE VALUE TESTS START

def test_absolute_value(math):
    assert math.abs(-5) == 5
    assert math.abs(5) == 5


def test_absolute_value_zero(math):
    assert math.abs(0) == 0
    assert math.abs(-0) == 0


def test_absolute_value_small(math):
    assert math.abs(0.000_000_000_1) == 0.000_000_000_1
    assert math.abs(-0.000_000_000_1) == 0.000_000_000_1


def test_absolute_value_large(math):
    assert math.abs(1_000_000_000) == 1_000_000_000
    assert math.abs(-1_000_000_000) == 1_000_000_000

# ABSOLUTE VALUE TESTS END
# FACTORIAL TESTS START

def test_factorial_zero(math):
    assert math.fac(0) == 1

def test_factorial_small_positive(math):
    assert math.fac(1) == 1
    assert math.fac(2) == 2
    assert math.fac(3) == 6
    assert math.fac(4) == 24
    assert math.fac(5) == 120
    assert math.fac(6) == 720
    assert math.fac(7) == 5040
    assert math.fac(8) == 40320
    assert math.fac(9) == 362880
    assert math.fac(10) == 3628800


def test_factorial_big_positive(math):
    assert math.fac(50) == 30414093201713378043612608166064768844377641568960512000000000000
    assert math.fac(74) == 330788544151938641225953028221253782145683251820934971170611926835411235700971565459250872320000000000000000
    assert math.fac(35) == 10333147966386144929666651337523200000000
    assert math.fac(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000


def test_factorial_negative(math):
    with pytest.raises(ValueError):
        math.fac(-6)
    with pytest.raises(ValueError):
        math.fac(-1)
    with pytest.raises(ValueError):
        math.fac(-10)
