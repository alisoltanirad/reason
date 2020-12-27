import pytest

from reason.stem import RegexStemmer, regex_stem


def test_string_input():
    input_value = 'watched birds flying'
    output = ['watch', 'bird', 'fly']
    assert RegexStemmer().stem(input_value) == output

def test_list_input():
    input_value = ['watched', 'birds', 'flying']
    output = ['watch', 'bird', 'fly']
    assert RegexStemmer().stem(input_value) == output

def test_bad_input():
    with pytest.raises(TypeError):
        RegexStemmer().stem(1)

def test_pattern():
    assert RegexStemmer('^(.*)(ason)$').stem('reason') == ['re']

def test_bad_pattern():
    with pytest.raises(TypeError):
        RegexStemmer(1)

def test_regex_stem():
    assert regex_stem('learning') == 'learn'

def test_regex_stem_bad_input():
    with pytest.raises(TypeError):
        regex_stem(['learning'])
