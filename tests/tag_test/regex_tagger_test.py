from reason.tag import RegexTagger


def test_string_input():
    input_value = '10 tools'
    output = [('10', 'number'), ('tools', 'word')]
    patterns = {r'\d+': 'number', r'[a-z]+': 'word'}
    assert RegexTagger(patterns).tag(input_value) == output

def test_list_input():
    input_value = ['10', 'tools']
    output = [('10', 'number'), ('tools', 'word')]
    patterns = {r'\d+': 'number', r'[a-z]+': 'word'}
    assert RegexTagger(patterns).tag(input_value) == output
