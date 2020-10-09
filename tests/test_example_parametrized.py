import pytest

def sum(num1,num2):
    print("it returns sum of two numbers")
    return num1+num2

@pytest.mark.parametrize('num1,num2,expected', [(3,5,8),(3,2,5)])
def test_sum(num1,num2,expected):
    assert sum(num1,num2)==expected
