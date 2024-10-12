import pytest

@pytest.fixture()
def sample_data1():
    data = [1,2,3,4,5]

@pytest.fixture()
def sample_data2():
    return True


def test_sample_data_1_2(sample_data1,sample_data2):
    print(sample_data1)
    print(sample_data2)