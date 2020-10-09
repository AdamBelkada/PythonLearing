import pytest
def sum_fnc(num1, num2):
    """It returns sum of two numbers"""
    return num1 + num2

@pytest.fixture(scope='session') #in this scope = session, it will not close connection until the session is closed
def get_sum_test_data():
    return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]

@pytest.fixture(autouse=True)
def setup_and_teardown():
    print ('\nFetching data from db')   #this will execute before test
    yield                               #allows to execute the next statement after the test is done
    print ('\nSaving test run data in db')

def test_sum(get_sum_test_data):
    for data in get_sum_test_data:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]
        assert sum_fnc(num1, num2) == expected