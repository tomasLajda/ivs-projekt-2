"""
@file tests.py
@brief File containing math library functionality tests.

@author
- Matúš Csirik (xcsirim00)
- Tomáš Lajda (xlajdat00)
@date March 19, 2024
"""
import pytest
import mymathlib  # temp name

def test_addition():
    assert mymathlib.add(1, 2) == 3


# ADDITION TESTS START
def test_addition_float():
    assert mymathlib.add(0.1, 0.1) == 0.2
    assert mymathlib.add(0.1, mymathlib.add(0.1, 0.1)) == 0.3


def test_addition_negative():
    assert mymathlib.add(-1, -2) == -3
    assert mymathlib.add(-1, 2) == 1
    assert mymathlib.add(1, -2) == -1


def test_addition_zero():
    assert mymathlib.add(0, 0) == 0
    assert mymathlib.add(-0, 0) == 0
    assert mymathlib.add(0, -0) == 0
    assert mymathlib.add(-0, -0) == 0
    assert mymathlib.add(2, 0) == 2
    assert mymathlib.add(0, 2) == 2
    assert mymathlib.add(-2, 0) == -2
    assert mymathlib.add(0, -2) == -2
    assert mymathlib.add(2, -2) == 0
    assert mymathlib.add(-2, 2) == 0


def test_addition_small():
    assert mymathlib.add(0.000_000_000_1, 0.000_000_000_2) == 0.000_000_000_3 # 1-e12 + 2-e12 = 3-e12
    assert mymathlib.add(0.000_000_1, 0.000_000_2) == 0.000_000_3
    assert mymathlib.add(0.000_1, 0.000_2) == 0.000_3


def test_addition_large():
    assert mymathlib.add(1_000, 2_000) == 3_000
    assert mymathlib.add(1_000_000, 2_000_000) == 3_000_000
    assert mymathlib.add(1_000_000_000_000, 2_000_000_000_000) == 3_000_000_000_000 # 1+e12 + 2+e12 = 3+e12


def test_addition_small_negative():
    assert mymathlib.add(-0.000_000_000_1, -0.000_000_000_2) == -0.000_000_000_3 # -1-e12 + -2-e12 = -3-e12
    assert mymathlib.add(-0.000_000_1, -0.000_000_2) == -0.000_000_3
    assert mymathlib.add(-0.000_1, -0.000_2) == -0.000_3


def test_addition_large_negative():
    assert mymathlib.add(-1_000, -2_000) == -3_000
    assert mymathlib.add(-1_000_000, -2_000_000) == -3_000_000
    assert mymathlib.add(-1_000_000_000_000, -2_000_000_000_000) == -3_000_000_000_000 # -1+e12 + -2+e12 = -3+e12


# ADDITION TESTS END
# SUBTRACTION TESTS START
def test_subtraction():
    assert mymathlib.sub(1, 1) == 0


def test_subtraction_float():
    assert mymathlib.sub(0.1, 2) == -1.9
    assert mymathlib.sub(mymathlib.sub(mymathlib.sub(
        mymathlib.sub(mymathlib.sub(mymathlib.sub(mymathlib.sub(mymathlib.sub(mymathlib.sub(mymathlib.sub(1, 0, 1), 0, 1), 0, 1), 0, 1), 0, 1), 0, 1), 0,
                 1), 0, 1), 0, 1), 0, 1) == 0


def test_subtraction_negative():
    assert mymathlib.sub(-1, -1) == 0
    assert mymathlib.sub(-1, -2) == 1
    assert mymathlib.sub(-1, 2) == -3
    assert mymathlib.sub(1, -2) == 3


def test_subtraction_zero():
    assert mymathlib.sub(0, 0) == 0
    assert mymathlib.sub(-0, 0) == 0
    assert mymathlib.sub(0, -0) == 0
    assert mymathlib.sub(-0, -0) == 0
    assert mymathlib.sub(2, 0) == 2
    assert mymathlib.sub(0, 2) == -2
    assert mymathlib.sub(-2, 0) == -2
    assert mymathlib.sub(0, -2) == 2
    assert mymathlib.sub(2, -2) == 4
    assert mymathlib.sub(-2, 2) == -4
    assert mymathlib.sub(2, 2) == 0


def test_subtraction_small():
    assert mymathlib.sub(0.000_000_000_1, 0.000_000_000_2) == -0.000_000_000_1 # 1-e12 - 2-e12 = -1-e12
    assert mymathlib.sub(0.000_000_1, 0.000_000_2) == -0.000_000_1
    assert mymathlib.sub(0.000_1, 0.000_2) == -0.000_1


def test_subtraction_large():
    assert mymathlib.sub(1_000, 2_000) == -1_000
    assert mymathlib.sub(1_000_000, 2_000_000) == -1_000_000
    assert mymathlib.sub(1_000_000_000_000, 2_000_000_000_000) == -1_000_000_000_000 # 1+e12 - 2+e12 = -1+e12


def test_subtraction_small_negative():
    assert mymathlib.sub(-0.000_000_000_1, -0.000_000_000_2) == 0.000_000_000_1 # -1-e12 - -2-e12 = 1-e12
    assert mymathlib.sub(-0.000_000_1, -0.000_000_2) == 0.000_000_1
    assert mymathlib.sub(-0.000_1, -0.000_2) == 0.000_1


def test_subtraction_large_negative():
    assert mymathlib.sub(-1_000, -2_000) == 1_000
    assert mymathlib.sub(-1_000_000, -2_000_000) == 1_000_000
    assert mymathlib.sub(-1_000_000_000_000, -2_000_000_000_000) == 1_000_000_000_000  # -1+e12 - -2+e12 = 1+e12

# SUBTRACTION TESTS END
# MULTIPLICATION TESTS START

def test_multiplication():
    assert mymathlib.mul(5, 2) == 10;


def test_multiplication_zero():
    assert mymathlib.mul(0, 1) == 0
    assert mymathlib.mul(1, 0) == 0
    assert mymathlib.mul(0, 0) == 0


def test_multiplication_negative():
    assert mymathlib.mul(-1, 2) == -2
    assert mymathlib.mul(1, -2) == -2
    assert mymathlib.mul(-1, -2) == 2


def test_multiplication_float():
    assert mymathlib.mul(1.1 * 10) == 11
    assert mymathlib.mul(1.1 * 1) == 1.1
    assert mymathlib.mul(0.5 * 10) == 5


def test_multiplication_small():
    assert mymathlib.mul(0.000_000_000_1, 0.000_000_000_2) == 0.000_000_000_000_000_000_02  # 1e-10 * 2e-10 = 2e-20
    assert mymathlib.mul(0.000_000_000_1, 2) == 0.000_000_000_2  # 1e-10 * 2 = 2e-10


def test_multiplication_large():
    assert mymathlib.mul(1_000_000_000_000, 2_000_000_000_000) == 2_000_000_000_000_000_000_000_000  # 1e+12 * 2e+12 = 2e+24
    assert mymathlib.mul(1_000_000_000_000, 2) == 2_000_000_000_000  # 1e+12 * 2 = 2e+12


# MULTIPLICATION TESTS END
# DIVISION TESTS START

def test_division():
    assert mymathlib.div(4, 2) == 2


def test_division_zero():
    with pytest.raises(ValueError):
        mymathlib.div(4, 0)


def test_division_negative():
    assert mymathlib.div(2, -1) == -1
    assert mymathlib.div(-2, 1) == -1
    assert mymathlib.div(-2, -1) == 1


def test_division_float():
    assert mymathlib.div(1, 2) == 0.5
    assert mymathlib.div(1, 100) == 0.01
    assert mymathlib.div(3, 90) == 0.05


def test_division_periodic():
    assert mymathlib.div(1, 3) == pytest.approx(0.3333, rel=1e-4)
    assert mymathlib.div(2, 7) == pytest.approx(0.2857, rel=1e-4)
    assert mymathlib.div(1, 6) == pytest.approx(0.1667, rel=1e-4)
    # 1e-4 is scientific notation for 0.0001.
    # It represents a relative tolerance of 0.01%
    # (or 0.0001 as a decimal) of the expected value.


def test_division_small():
    assert mymathlib.div(0.000_000_000_1, 0.000_000_000_2) == 0.5  # 1e-10 / 2e-10 = 0.5
    assert mymathlib.div(0.000_000_000_1, 2) == 0.000_000_000_2  # 1e-10 / 2 = 5e-10
    assert mymathlib.div(2, 0.000_000_000_1) == 20_000_000_000  # 2 / e-10 = 2e+11


def test_division_large():
    assert mymathlib.div(1_000_000_000, 2_000_000_000) == 0.5  # 1+e10 / 2+e10 = 0.5
    assert mymathlib.div(1_000_000_000, 2) == 500_000_000  # 1+e10 / 2 = 5+e9
    assert mymathlib.div(2, 1_000_000_000) == 0.000_000_002  # 1+e10 / 2 = 2e-9


# DIVISION TESTS END
# ABSOLUTE VALUE TESTS START

def test_absolute_value():
    assert mymathlib.abs(-5) == 5
    assert mymathlib.abs(5) == 5


def test_absolute_value_zero():
    assert mymathlib.abs(0) == 0
    assert mymathlib.abs(-0) == 0


def test_absolute_value_small():
    assert mymathlib.abs(0.000_000_000_1) == 0.000_000_000_1  # abs(1-e10) = 1-e10
    assert mymathlib.abs(-0.000_000_000_1) == 0.000_000_000_1  # abs(-1-e10) = 1-e10


def test_absolute_value_large():
    assert mymathlib.abs(1_000_000_000) == 1_000_000_000  # abs(1+e10) = 1+e10
    assert mymathlib.abs(-1_000_000_000) == 1_000_000_000  # abs(-1+e10) = 1+e10

# ABSOLUTE VALUE TESTS END
# FACTORIAL TESTS START

def test_factorial_zero():
    assert mymathlib.fac(0) == 1

def test_factorial_small_positive():
    assert mymathlib.fac(1) == 1
    assert mymathlib.fac(2) == 2
    assert mymathlib.fac(3) == 6
    assert mymathlib.fac(4) == 24
    assert mymathlib.fac(5) == 120
    assert mymathlib.fac(6) == 720
    assert mymathlib.fac(7) == 5040
    assert mymathlib.fac(8) == 40320
    assert mymathlib.fac(9) == 362880
    assert mymathlib.fac(10) == 3628800


def test_factorial_big_positive():
    assert mymathlib.fac(50) == 30414093201713378043612608166064768844377641568960512000000000000
    assert mymathlib.fac(74) == 330788544151938641225953028221253782145683251820934971170611926835411235700971565459250872320000000000000000
    assert mymathlib.fac(35) == 10333147966386144929666651337523200000000
    assert mymathlib.fac(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000


def test_factorial_negative():
    with pytest.raises(ValueError):
        mymathlib.fac(-6)
    with pytest.raises(ValueError):
        mymathlib.fac(-1)
    with pytest.raises(ValueError):
        mymathlib.fac(-10)
