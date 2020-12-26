import pytest

from reason.analysis import FreqDist


@pytest.fixture
def input_value():
    value = 'hey hey oh oh oh yeah'
    return value


def test_str_input(input_value):
    output = [('hey', 2), ('oh', 3), ('yeah', 1)]
    assert FreqDist(input_value).get_data() == output

def test_list_input(input_value):
    output = [('hey', 2), ('oh', 3), ('yeah', 1)]
    assert FreqDist(input_value).get_data() == output

def test_most_common(input_value):
    output = [('oh', 3), ('hey', 2)]
    assert FreqDist(input_value).most_common(2) == output

def test_key_value(input_value):
    assert FreqDist(input_value)['hey'] == 2

def test_copy(input_value):
    fd1 = FreqDist(input_value)
    fd2 = fd1.copy()
    fd1['yeah'] = 4
    assert fd2.most_common() == [('oh', 3)]
