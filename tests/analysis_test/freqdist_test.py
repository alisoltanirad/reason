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

def test_bad_error():
    with pytest.raises(TypeError):
        FreqDist(10)

def test_most_common(input_value):
    output = [('oh', 3), ('hey', 2)]
    assert FreqDist(input_value).most_common(2) == output

def test_most_common_bad_input(input_value):
    fd = FreqDist(input_value)
    with pytest.raises(TypeError):
        fd.most_common(1.5)

def test_getitem(input_value):
    assert FreqDist(input_value)['hey'] == 2

def test_setitem(input_value):
    fd = FreqDist(input_value)
    fd['hey'] = 5
    assert fd['hey'] == 5

def test_delitem(input_value):
    fd = FreqDist(input_value)
    del fd['hey']
    assert fd['hey'] == 0

def test_copy(input_value):
    fd1 = FreqDist(input_value)
    fd2 = fd1.copy()
    fd1['yeah'] = 4
    assert fd2.most_common() == [('oh', 3)]

def test_str_(input_value):
    output = "Frequency Distribution\n" \
             "Most-Common: [('oh', 3), ('hey', 2), ('yeah', 1)]"
    assert FreqDist(input_value).__str__() == output

def test_conditional():
    input_value = [('a', 'a'), ('a', 'b'), ('b', 'c'), ('a', 'b')]
    output = [(('a', 'b'), 2)]
    assert FreqDist(input_value).most_common() == output
