from reason.stem import RegexStemmer, regex_stem


def test_string_input():
    input_value = 'watched birds flying'
    output = ['watch', 'bird', 'fly']
    assert RegexStemmer().stem(input_value) == output

def test_list_input():
    input_value = ['watched', 'birds', 'flying']
    output = ['watch', 'bird', 'fly']
    assert RegexStemmer().stem(input_value) == output

def test_pattern():
    assert RegexStemmer('^(.*)(ason)$').stem('reason') == ['re']

def test_regex_stem():
    assert regex_stem('learning') == 'learn'
