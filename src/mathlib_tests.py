"""
@file mathlib_tests.py
@brief File containing math library functionality tests.

@author
- Matúš Csirik (xcsirim00)
- Tomáš Lajda (xlajdat00)
@date March 19, 2024
"""
import pytest
import mathlib


# ADDITION TESTS START

def test_addition():
    assert mathlib.add(1, 2) == 3


def test_addition_float():
    assert mathlib.add(0.1, 0.1) == 0.2
    assert mathlib.add(0.1, mathlib.add(0.1, 0.1)) == 0.3
    assert mathlib.add(mathlib.add(mathlib.add(0.1, 0.1), 0.1), 0.1) == 0.4
    assert mathlib.add(mathlib.add(mathlib.add(mathlib.add(0.1, 0.1), 0.1), 0.1), 0.1) == 0.5
    assert mathlib.add(mathlib.add(mathlib.add(mathlib.add(0.1, 0.1), 0.1), 0.1), 0.1) + mathlib.add(mathlib.add(mathlib.add(mathlib.add(0.1, 0.1), 0.1), 0.1), 0.1) == 1


def test_addition_negative():
    assert mathlib.add(-1, -2) == -3
    assert mathlib.add(-1, 2) == 1
    assert mathlib.add(1, -2) == -1


def test_addition_zero():
    assert mathlib.add(0, 0) == 0
    assert mathlib.add(-0, 0) == 0
    assert mathlib.add(0, -0) == 0
    assert mathlib.add(-0, -0) == 0
    assert mathlib.add(2, 0) == 2
    assert mathlib.add(0, 2) == 2
    assert mathlib.add(-2, 0) == -2
    assert mathlib.add(0, -2) == -2
    assert mathlib.add(2, -2) == 0
    assert mathlib.add(-2, 2) == 0


def test_addition_small():
    assert mathlib.add(0.000_000_000_1, 0.000_000_000_2) == 0.000_000_000_3  # 1-e12 + 2-e12 = 3-e12
    assert mathlib.add(0.000_000_1, 0.000_000_2) == 0.000_000_3
    assert mathlib.add(0.000_1, 0.000_2) == 0.000_3


def test_addition_large():
    assert mathlib.add(1_000, 2_000) == 3_000
    assert mathlib.add(1_000_000, 2_000_000) == 3_000_000
    assert mathlib.add(1_000_000_000_000, 2_000_000_000_000) == 3_000_000_000_000  # 1e12 + 2e12 = 3e12


def test_addition_small_negative():
    assert mathlib.add(-0.000_000_000_1, -0.000_000_000_2) == -0.000_000_000_3  # -1-e12 + -2-e12 = -3-e12
    assert mathlib.add(-0.000_000_1, -0.000_000_2) == -0.000_000_3
    assert mathlib.add(-0.000_1, -0.000_2) == -0.000_3


def test_addition_large_negative():
    assert mathlib.add(-1_000, -2_000) == -3_000
    assert mathlib.add(-1_000_000, -2_000_000) == -3_000_000
    assert mathlib.add(-1_000_000_000_000, -2_000_000_000_000) == -3_000_000_000_000  # -1e12 + -2e12 = -3e12


# ADDITION TESTS END
# SUBTRACTION TESTS START

def test_subtraction():
    assert mathlib.sub(1, 1) == 0


def test_subtraction_float():
    assert mathlib.sub(0, 0.1) == -0.1
    assert mathlib.sub(mathlib.sub(0, 0.1), 0.1) == -0.2
    assert mathlib.sub(mathlib.sub(mathlib.sub(0, 0.1), 0.1), 0.1) == -0.3
    assert mathlib.sub(mathlib.sub(mathlib.sub(mathlib.sub(0, 0.1), 0.1), 0.1), 0.1) == -0.4
    assert mathlib.sub(mathlib.sub(mathlib.sub(mathlib.sub(mathlib.sub(0, 0.1), 0.1), 0.1), 0.1), 0.1) == -0.5
    assert mathlib.sub(mathlib.sub(mathlib.sub(mathlib.sub(mathlib.sub(0, 0.1), 0.1), 0.1), 0.1), 0.1) + mathlib.sub(mathlib.sub(mathlib.sub(mathlib.sub(mathlib.sub(0, 0.1), 0.1), 0.1), 0.1), 0.1) == -1


def test_subtraction_negative():
    assert mathlib.sub(-1, -1) == 0
    assert mathlib.sub(-1, -2) == 1
    assert mathlib.sub(-1, 2) == -3
    assert mathlib.sub(1, -2) == 3


def test_subtraction_zero():
    assert mathlib.sub(0, 0) == 0
    assert mathlib.sub(-0, 0) == 0
    assert mathlib.sub(0, -0) == 0
    assert mathlib.sub(-0, -0) == 0
    assert mathlib.sub(2, 0) == 2
    assert mathlib.sub(0, 2) == -2
    assert mathlib.sub(-2, 0) == -2
    assert mathlib.sub(0, -2) == 2
    assert mathlib.sub(2, -2) == 4
    assert mathlib.sub(-2, 2) == -4
    assert mathlib.sub(2, 2) == 0


def test_subtraction_small():
    assert mathlib.sub(0.000_000_000_1, 0.000_000_000_2) == -0.000_000_000_1  # 1-e12 - 2-e12 = -1-e12
    assert mathlib.sub(0.000_000_1, 0.000_000_2) == -0.000_000_1
    assert mathlib.sub(0.000_1, 0.000_2) == -0.000_1


def test_subtraction_large():
    assert mathlib.sub(1_000, 2_000) == -1_000
    assert mathlib.sub(1_000_000, 2_000_000) == -1_000_000
    assert mathlib.sub(1_000_000_000_000, 2_000_000_000_000) == -1_000_000_000_000  # 1e12 - 2e12 = -1e12


def test_subtraction_small_negative():
    assert mathlib.sub(-0.000_000_000_1, -0.000_000_000_2) == 0.000_000_000_1  # -1-e12 - -2-e12 = 1-e12
    assert mathlib.sub(-0.000_000_1, -0.000_000_2) == 0.000_000_1
    assert mathlib.sub(-0.000_1, -0.000_2) == 0.000_1


def test_subtraction_large_negative():
    assert mathlib.sub(-1_000, -2_000) == 1_000
    assert mathlib.sub(-1_000_000, -2_000_000) == 1_000_000
    assert mathlib.sub(-1_000_000_000_000, -2_000_000_000_000) == 1_000_000_000_000  # -1e12 - -2e12 = 1e12


# SUBTRACTION TESTS END
# MULTIPLICATION TESTS START

def test_multiplication():
    assert mathlib.mul(5, 2) == 10;


def test_multiplication_zero():
    assert mathlib.mul(0, 1) == 0
    assert mathlib.mul(1, 0) == 0
    assert mathlib.mul(0, 0) == 0


def test_multiplication_negative():
    assert mathlib.mul(-1, 2) == -2
    assert mathlib.mul(1, -2) == -2
    assert mathlib.mul(-1, -2) == 2


def test_multiplication_float():
    assert mathlib.mul(1.1, 10) == 11
    assert mathlib.mul(1.1, 1) == 1.1
    assert mathlib.mul(0.5, 10) == 5


def test_multiplication_small():
    assert mathlib.mul(0.000_000_000_1, 0.000_000_000_2) == 0.000_000_000_000_000_000_02  # 1e-10 * 2e-10 = 2e-20
    assert mathlib.mul(0.000_000_000_1, 2) == 0.000_000_000_2  # 1e-10 * 2 = 2e-10


def test_multiplication_large():
    assert mathlib.mul(1_000_000_000_000,
                       2_000_000_000_000) == 2_000_000_000_000_000_000_000_000  # 1e12 * 2e12 = 2e24
    assert mathlib.mul(1_000_000_000_000, 2) == 2_000_000_000_000  # 1e12 * 2 = 2e12


# MULTIPLICATION TESTS END
# DIVISION TESTS START

def test_division():
    assert mathlib.div(4, 2) == 2


def test_division_zero():
    with pytest.raises(ValueError):
        mathlib.div(4, 0)


def test_division_negative():
    assert mathlib.div(2, -1) == -2
    assert mathlib.div(-2, 1) == -2
    assert mathlib.div(-2, -1) == 2


def test_division_float():
    assert mathlib.div(1, 2) == 0.5
    assert mathlib.div(1, 100) == 0.01


def test_division_periodic():
    assert mathlib.div(1, 3) == pytest.approx(0.3333333333333333, rel=1e-4)
    assert mathlib.div(2, 7) == pytest.approx(0.2857142857142857, rel=1e-4)
    assert mathlib.div(1, 6) == pytest.approx(0.16666666666666666, rel=1e-4)

def test_division_small():
    assert mathlib.div(0.000_000_000_1, 0.000_000_000_2) == 0.5  # 1e-10 / 2e-10 = 0.5
    assert mathlib.div(0.000_000_000_1, 2) == 0.000_000_000_05  # 1e-10 / 2 = 5e-10
    assert mathlib.div(2, 0.000_000_000_1) == 20_000_000_000  # 2 / e-10 = 2e11


def test_division_large():
    assert mathlib.div(1_000_000_000, 2_000_000_000) == 0.5  # 1e10 / 2e10 = 0.5
    assert mathlib.div(1_000_000_000, 2) == 500_000_000  # 1e10 / 2 = 5e9
    assert mathlib.div(2, 1_000_000_000) == 0.000_000_002  # 1e10 / 2 = 2e-9

# DIVISION TESTS END
# MODULUS TESTS START

def test_modulus():
    assert mathlib.mod(4, 2) == 0
    assert mathlib.mod(5, 2) == 1
    assert mathlib.mod(2, 5) == 2


def test_modulus_zero():
    with pytest.raises(ValueError):
        mathlib.mod(4, 0)


def test_modulus_negative():
    assert mathlib.mod(-11, 7) == 4
    assert mathlib.mod(-11, -7) == -4
    assert mathlib.mod(11, -7) == -4


def test_modulus_float():
    assert mathlib.mod(5.5, 5) == 0.5
    assert mathlib.mod(3.33, 1.11) == 0
    assert mathlib.mod(5, 5.5) == 5


def test_modulus_small():
    assert mathlib.mod(0.000_000_000_1, 0.000_000_000_2) == 0.000_000_000_1  # 1e-10 % 2e-10 = 1e-10

def test_modulus_large():
    assert mathlib.mod(1_000_000_000, 2_000_000_000) == 1_000_000_000  # 1e10 % 2e10 = 1e10


# MODULUS TESTS END
# ABSOLUTE VALUE TESTS START

def test_absolute_value():
    assert mathlib.abs(-5) == 5
    assert mathlib.abs(5) == 5


def test_absolute_value_zero():
    assert mathlib.abs(0) == 0
    assert mathlib.abs(-0) == 0


def test_absolute_value_small():
    assert mathlib.abs(0.000_000_000_1) == 0.000_000_000_1  # abs(1-e10) = 1-e10
    assert mathlib.abs(-0.000_000_000_1) == 0.000_000_000_1  # abs(-1-e10) = 1-e10


def test_absolute_value_large():
    assert mathlib.abs(1_000_000_000) == 1_000_000_000  # abs(1e10) = 1e10
    assert mathlib.abs(-1_000_000_000) == 1_000_000_000  # abs(-1e10) = 1e10

# ABSOLUTE VALUE TESTS END
# FACTORIAL TESTS START

def test_factorial_zero():
    assert mathlib.fac(0) == 1


def test_factorial_small_positive():
    assert mathlib.fac(1) == 1
    assert mathlib.fac(2) == 2
    assert mathlib.fac(3) == 6
    assert mathlib.fac(4) == 24
    assert mathlib.fac(5) == 120
    assert mathlib.fac(6) == 720
    assert mathlib.fac(7) == 5040
    assert mathlib.fac(8) == 40320
    assert mathlib.fac(9) == 362880
    assert mathlib.fac(10) == 3628800


def test_factorial_small_positive():
    assert mathlib.fac(1) == 1
    assert mathlib.fac(2) == 2
    assert mathlib.fac(3) == 6
    assert mathlib.fac(4) == 24
    assert mathlib.fac(5) == 120
    assert mathlib.fac(6) == 720
    assert mathlib.fac(7) == 5_040
    assert mathlib.fac(8) == 40_320
    assert mathlib.fac(9) == 362_880
    assert mathlib.fac(10) == 3_628_800


def test_factorial_big_positive():
    assert mathlib.fac(50) == 30414093201713378043612608166064768844377641568960512000000000000
    assert mathlib.fac(
        74) == 330788544151938641225953028221253782145683251820934971170611926835411235700971565459250872320000000000000000
    assert mathlib.fac(35) == 10333147966386144929666651337523200000000
    assert mathlib.fac(
        100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000


def test_factorial_negative():
    with pytest.raises(ValueError):
        mathlib.fac(-6)
    with pytest.raises(ValueError):
        mathlib.fac(-1)
    with pytest.raises(ValueError):
        mathlib.fac(-10)

# FACTORIAL TESTS END
# POW TESTS START

def test_pow_base_zero():
    assert mathlib.pow(0, 1_000_000_000) == 0
    assert mathlib.pow(0, 143) == 0
    with pytest.raises(ValueError):
        mathlib.pow(0, -10)


def test_pow_base_one():
    assert mathlib.pow(1, 100) == 1
    assert mathlib.pow(1, 10_000_000) == 1


def test_pow_of_positive():
    assert mathlib.pow(2, 2) == 4
    assert mathlib.pow(10, 2) == 100
    assert mathlib.pow(43, 5) == 147_008_443
    assert mathlib.pow(8, 6) == 262_144
    assert mathlib.pow(-7, 5) == -16_807
    assert mathlib.pow(-12, 12) == 8_916_100_448_256


def test_pow_of_negative_base():
    assert mathlib.pow(-2, 3) == -8
    assert mathlib.pow(-10, 2) == 100
    assert mathlib.pow(-2, 4) == 16
    assert mathlib.pow(-5, 5) == -3125


def test_pow_of_large_base_and_index():
    assert mathlib.pow(1_000, 1_000) == 1e3000
    assert mathlib.pow(10, 10) == 10_000_000_000


def test_pow_decimal_numbers():
    assert mathlib.pow(2.5, 2) == pytest.approx(6.25, rel=1e-3)  # 2.5^2 ≈ 6.25 (approx)
    assert mathlib.pow(1.5, 3) == pytest.approx(3.375, rel=1e-3)  # 1.5^3 ≈ 3.375 (approx)
    assert mathlib.pow(3.33, 2) == pytest.approx(11.0889, rel=1e-3)  # 3.33^2 = 11.0889 (approx)
    assert mathlib.pow(10.5, 3) == pytest.approx(1157.625, rel=1e-3)  # 10.5^3 ≈ 1157.625 (approx)


def test_pow_large_decimal_numbers():
    assert mathlib.pow(1.0001, 1000) == pytest.approx(1.1051709180756477, rel=1e-4)
    assert mathlib.pow(1.00001, 10000) == pytest.approx(1.1051709180756477, rel=1e-4)
    assert mathlib.pow(1.000001, 1000000) == pytest.approx(2.7182804690957534, rel=1e-4)


def test_pow_decimal_index():
    with pytest.raises(TypeError):
        mathlib.pow(2, 1.5)


def test_pow_negative_index_raises_error():
    with pytest.raises(TypeError):
        mathlib.pow(2, -2)

# POW TESTS END
# ROOT TESTS START

def test_root_integer_root():
    assert mathlib.root(4, 2) == 2
    assert mathlib.root(9, 2) == 3
    assert mathlib.root(16, 2) == 4


def test_root_negative_number_even_root():
    with pytest.raises(ValueError):
        mathlib.root(-4, 2)
    with pytest.raises(ValueError):
        mathlib.root(-128, 4)
    with pytest.raises(ValueError):
        mathlib.root(-1_024, 8)


def test_root_negative_number_decimal_root():
    assert mathlib.root(-8, 3) == -2
    assert mathlib.root(-27, 3) == -3
    assert mathlib.root(-64, 3) == -4


def test_root_large_number():
    assert mathlib.root(10000000, 2) == pytest.approx(3162.2776601683795, rel=1e-4)
    assert mathlib.root(1000000000, 3) == pytest.approx(1000.0, rel=1e-4)


def test_root_small_number():
    assert mathlib.root(0.0001, 2) == pytest.approx(0.01, rel=1e-4)
    assert mathlib.root(0.002, 3) == pytest.approx(0.1259921052362699, rel=1e-4)
# ROOT TESTS END

# End of matlib_tests.py