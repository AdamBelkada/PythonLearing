import pytest

def sum(num1,num2):
    print("it returns sum of two numbers")
    return num1+num2

def test_sum():
    assert sum(1,2)==4

def test_sum_output_int():
    assert type(sum(1,2)) is int