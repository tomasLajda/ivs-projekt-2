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

# ADDITION TESTS START
def test_addition():
    assert mymathlib.add(1, 2) == 3

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

def test_factorial_small_positive(math):
    assert mymathlib.fac(1) == 1
    assert mymathlib.fac(2) == 2
    assert mymathlib.fac(3) == 6
    assert mymathlib.fac(4) == 24
    assert mymathlib.fac(5) == 120
    assert mymathlib.fac(6) == 720
    assert mymathlib.fac(7) == 5_040
    assert mymathlib.fac(8) == 40_320
    assert mymathlib.fac(9) == 362_880
    assert mymathlib.fac(10) == 3_628_800


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

# FACTORIAL TESTS END
# POW TESTS START
        

def test_pow_base_zero():
    assert mymathlib.pow(0, 1_000_000_000) == 0
    assert mymathlib.pow(0, 143) == 0
    with pytest.raises(ValueError):
        mymathlib.pow(0, -10)


def test_pow_base_one():
    assert mymathlib.pow(1, 100) == 1
    assert mymathlib.pow(1, 10_000_000) == 1
    

def test_pow_of_positive():
    assert mymathlib.pow(2, 2) == 4
    assert mymathlib.pow(10, 2) == 100
    assert mymathlib.pow(43, 5) == 147_008_443
    assert mymathlib.pow(8, 6) == 262_144
    assert mymathlib.pow(-7, 5) == -16_807
    assert mymathlib.pow(-12, 12) == 8_916_100_448_256


def test_pow_of_negative_base():
    assert mymathlib.pow(-2, 3) == -8
    assert mymathlib.pow(-10, 2) == 100
    assert mymathlib.pow(-2, 4) == 16
    assert mymathlib.pow(-5, 5) == -3125


def test_pow_of_large_base_and_index():
    assert mymathlib.pow(1_000, 1_000) == 1.0e+3000
    assert mymathlib.pow(10, 10) == 10_000_000_000


def test_pow_decimal_numbers():
    assert mymathlib.pow(2.5, 2) == pytest.approx(6.25, rel=1e-3)  # 2.5^2 ≈ 6.25 (approx)
    assert mymathlib.pow(1.5, 3) == pytest.approx(3.375, rel=1e-3)  # 1.5^3 ≈ 3.375 (approx)
    assert mymathlib.pow(3.33, 2) == pytest.approx(11.088_9, rel=1e-3)  # 3.33^2 = 11.0889 (approx)
    assert mymathlib.pow(10.5, 3) == pytest.approx(1_157.625, rel=1e-3)  # 10.5^3 ≈ 1157.625 (approx)


def test_pow_large_decimal_numbers():
    assert mymathlib.pow(1.000_1, 1000) == pytest.approx(1.105_165_392_6, rel=1e-3)  # 1.0001^1000 ≈ 1.105 (approx)
    assert mymathlib.pow(1.000_01, 10_000) == pytest.approx(1.105_170_365_4, rel=1e-3)  # 1.00001^10000 ≈ 1.105 (approx)
    assert mymathlib.pow(1.000_001, 1_000_000) == pytest.approx(2.718_280_469_0, rel=1e-3)  # 1.000001^1000000 ≈ 2.718 (approx)


def test_pow_decimal_index():
    with pytest.raises(TypeError):
        mymathlib.pow(2, 1.5)


def test_pow_negative_index_raises_error():
    with pytest.raises(TypeError):
        mymathlib.pow(2, -2)
        

# POW TESTS END
# SQR TESTS START
        
def test_sqr_integer_root(math):
    assert mymathlib.sqr(4, 2) == 2
    assert mymathlib.sqr(9, 2) == 3
    assert mymathlib.sqr(16, 2) == 4


def test_sqr_negative_number_even_root(math):
    with pytest.raises(ValueError):
        mymathlib.sqr(-4, 2)
    with pytest.raises(ValueError):
        mymathlib.sqr(-128, 4)
    with pytest.raises(ValueError):
        mymathlib.sqr(-1_024, 8)


def test_sqr_negative_number_decimal_root():
    assert mymathlib.sqr(-8, 3) == -2
    assert mymathlib.sqr(-27, 3) == -3
    assert mymathlib.sqr(-64, 3) == -4


def test_sqr_large_number():
    assert mymathlib.sqr(10_000_000, 2) == pytest.approx(3_162.277_660_168_3, rel=1e-3)  # sqr(10_000_000, 2) ≈ 3_162.277(approx)
    assert mymathlib.sqr(1_000_000_000, 3) == pytest.approx(999.999_999_999_9, rel=1e-3)  # sqr(1_000_000_000, 3) ≈ 999.999 (approx)


def test_sqr_small_number():
    assert mymathlib.sqr(0.000_1, 2) == pytest.approx(0.01, rel=1e-3)  # sqr(0.0001, 2) ≈ 0.01 (approx)
    assert mymathlib.sqr(0.002, 3) == pytest.approx(0.125_992_104_9, rel=1e-3)  # sqr(0.001, 3) ≈ 0.125 (approx)


# SQR TESTS END
