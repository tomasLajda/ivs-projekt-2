"""
@file tests.py
@brief File containing math library functionality tests.

@author
- Matúš Csirik (xcsirim00)
- Tomáš Lajda (xlajdat00)
@date March 19, 2024
"""
import pytest
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
    assert math.add(0.000_000_000_1, 0.000_000_000_2) == 0.000_000_000_3 # 1-e12 + 2-e12 = 3-e12
    assert math.add(0.000_000_1, 0.000_000_2) == 0.000_000_3
    assert math.add(0.000_1, 0.000_2) == 0.000_3


def test_addition_large(math):
    assert math.add(1_000, 2_000) == 3_000
    assert math.add(1_000_000, 2_000_000) == 3_000_000
    assert math.add(1_000_000_000_000, 2_000_000_000_000) == 3_000_000_000_000 # 1+e12 + 2+e12 = 3+e12


def test_addition_small_negative(math):
    assert math.add(-0.000_000_000_1, -0.000_000_000_2) == -0.000_000_000_3 # -1-e12 + -2-e12 = -3-e12
    assert math.add(-0.000_000_1, -0.000_000_2) == -0.000_000_3
    assert math.add(-0.000_1, -0.000_2) == -0.000_3


def test_addition_large_negative(math):
    assert math.add(-1_000, -2_000) == -3_000
    assert math.add(-1_000_000, -2_000_000) == -3_000_000
    assert math.add(-1_000_000_000_000, -2_000_000_000_000) == -3_000_000_000_000 # -1+e12 + -2+e12 = -3+e12


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
    assert math.sub(0.000_000_000_1, 0.000_000_000_2) == -0.000_000_000_1 # 1-e12 - 2-e12 = -1-e12
    assert math.sub(0.000_000_1, 0.000_000_2) == -0.000_000_1
    assert math.sub(0.000_1, 0.000_2) == -0.000_1


def test_subtraction_large(math):
    assert math.sub(1_000, 2_000) == -1_000
    assert math.sub(1_000_000, 2_000_000) == -1_000_000
    assert math.sub(1_000_000_000_000, 2_000_000_000_000) == -1_000_000_000_000 # 1+e12 - 2+e12 = -1+e12


def test_subtraction_small_negative(math):
    assert math.sub(-0.000_000_000_1, -0.000_000_000_2) == 0.000_000_000_1 # -1-e12 - -2-e12 = 1-e12
    assert math.sub(-0.000_000_1, -0.000_000_2) == 0.000_000_1
    assert math.sub(-0.000_1, -0.000_2) == 0.000_1


def test_subtraction_large_negative(math):
    assert math.sub(-1_000, -2_000) == 1_000
    assert math.sub(-1_000_000, -2_000_000) == 1_000_000
    assert math.sub(-1_000_000_000_000, -2_000_000_000_000) == 1_000_000_000_000  # -1+e12 - -2+e12 = 1+e12

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
    assert math.mul(0.000_000_000_1, 0.000_000_000_2) == 0.000_000_000_000_000_000_02  # 1e-10 * 2e-10 = 2e-20
    assert math.mul(0.000_000_000_1, 2) == 0.000_000_000_2  # 1e-10 * 2 = 2e-10


def test_multiplication_large(math):
    assert math.mul(1_000_000_000_000, 2_000_000_000_000) == 2_000_000_000_000_000_000_000_000  # 1e+12 * 2e+12 = 2e+24
    assert math.mul(1_000_000_000_000, 2) == 2_000_000_000_000  # 1e+12 * 2 = 2e+12


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
    assert math.div(0.000_000_000_1, 0.000_000_000_2) == 0.5  # 1e-10 / 2e-10 = 0.5
    assert math.div(0.000_000_000_1, 2) == 0.000_000_000_2  # 1e-10 / 2 = 5e-10
    assert math.div(2, 0.000_000_000_1) == 20_000_000_000  # 2 / e-10 = 2e+11


def test_division_large(math):
    assert math.div(1_000_000_000, 2_000_000_000) == 0.5  # 1+e10 / 2+e10 = 0.5
    assert math.div(1_000_000_000, 2) == 500_000_000  # 1+e10 / 2 = 5+e9
    assert math.div(2, 1_000_000_000) == 0.000_000_002  # 1+e10 / 2 = 2e-9


# DIVISION TESTS END
# ABSOLUTE VALUE TESTS START

def test_absolute_value(math):
    assert math.abs(-5) == 5
    assert math.abs(5) == 5


def test_absolute_value_zero(math):
    assert math.abs(0) == 0
    assert math.abs(-0) == 0


def test_absolute_value_small(math):
    assert math.abs(0.000_000_000_1) == 0.000_000_000_1  # abs(1-e10) = 1-e10
    assert math.abs(-0.000_000_000_1) == 0.000_000_000_1  # abs(-1-e10) = 1-e10


def test_absolute_value_large(math):
    assert math.abs(1_000_000_000) == 1_000_000_000  # abs(1+e10) = 1+e10
    assert math.abs(-1_000_000_000) == 1_000_000_000  # abs(-1+e10) = 1+e10

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
    assert math.fac(7) == 5_040
    assert math.fac(8) == 40_320
    assert math.fac(9) == 362_880
    assert math.fac(10) == 3_628_800


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


# FACTORIAL TESTS END
# POW TESTS START
        

def test_pow_base_zero(math):
    assert math.pow(0, 1_000_000_000) == 0
    assert math.pow(0, 143) == 0
    with pytest.raises(ValueError):
        math.pow(0, -10)    


def test_pow_base_one(math):
    assert math.pow(1, 100) == 1
    assert math.pow(1, 10_000_000) == 1
    

def test_pow_of_positive(math):
    assert math.pow(2, 2) == 4
    assert math.pow(10, 2) == 100
    assert math.pow(43, 5) == 147_008_443
    assert math.pow(8, 6) == 262_144
    assert math.pow(-7, 5) == -16_807
    assert math.pow(-12, 12) == 8_916_100_448_256

def test_pow_of_negative_base(math):
    assert math.pow(-2, 3) == -8
    assert math.pow(-10, 2) == 100
    assert math.pow(-2, 4) == 16
    assert math.pow(-5, 5) == -3125

def test_pow_of_large_base_and_index(math):
    assert math.pow(1000, 1000) == 1.0e+3000
    assert math.pow(10, 10) == 10_000_000_000

def test_pow_decimal_numbers(math):
    assert math.pow(2.5, 2) == pytest.approx(6.25, rel=1e-3)  # 2.5^2 ≈ 6.25 (approx)
    assert math.pow(1.5, 3) == pytest.approx(3.375, rel=1e-3)  # 1.5^3 ≈ 3.375 (approx)
    assert math.pow(3.33, 2) == pytest.approx(11.0889, rel=1e-3)  # 3.33^2 = 11.0889 (approx)
    assert math.pow(10.5, 3) == pytest.approx(1157.625, rel=1e-3)  # 10.5^3 ≈ 1157.625 (approx)

def test_pow_large_decimal_numbers(math):
    assert math.pow(1.0001, 1000) == pytest.approx(2.71828036661, rel=1e-3)  # 1.0001^1000 ≈ 2.7183 (approx)
    assert math.pow(1.00001, 10_000) == pytest.approx(2.7182794155, rel=1e-3)  # 1.00001^10000 ≈ 2.7183 (approx)
    assert math.pow(1.000001, 1_000_000) == pytest.approx(2.7182818284, rel=1e-3)  # 1.000001^1000000 ≈ 2.7183 (approx)

def test_pow_decimal_index(math):
    with pytest.raises(TypeError):
        math.pow(2, 1.5)

def test_pow_negative_index_raises_error(math):
    with pytest.raises(TypeError):
        math.pow(2, -2)
        

# POW TESTS END
# SQR TESTS START