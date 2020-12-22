from reason.stem import RegexStemmer, regex_stem


def test_string_input():
    input = 'Watched birds flying'
    output = ['Watch', 'bird', 'fly']
    assert RegexStemmer().stem(input) == output

def test_list_input():
    input = ['Watched', 'birds', 'flying']
    output = ['Watch', 'bird', 'fly']
    assert RegexStemmer().stem(input) == output

def test_pattern():
    assert RegexStemmer('^(.*)(ason)$').stem('reason') == ['re']

def test_regex_stem():
    assert regex_stem('learning') == 'learn'
