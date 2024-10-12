# Fixture - concept in python
# you can use the fixture
# context to the test
# similar - pre condition, post condition
import pytest


# pre-condition
 # post condition


 # setup - before test case
 # teardown - after a test case

@pytest.fixture
def is_married():
    return True

def test_i_need_confirm(is_married): # passing the fixture as an argument
    assert is_married == True