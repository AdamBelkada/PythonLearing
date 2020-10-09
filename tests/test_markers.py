import pytest

def sum_fnc(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2
@pytest.mark.slow
def test_sum():
    assert sum_fnc(1, 2) == 3
def test_sum_output_type():
    assert type(sum_fnc(1, 2)) is int