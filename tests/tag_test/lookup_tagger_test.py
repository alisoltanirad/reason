from reason.tag import LookupTagger


def test_string_input():
    input = 'a black cat'
    output = [('a', ''), ('black', 'color'), ('cat', 'animal')]
    lookup_data = {'cat': 'animal', 'black': 'color'}
    assert LookupTagger(lookup_data).tag(input) == output

def test_list_input():
    input = ['a', 'black', 'cat']
    output = [('a', ''), ('black', 'color'), ('cat', 'animal')]
    lookup_data = {'cat': 'animal', 'black': 'color'}
    assert LookupTagger(lookup_data).tag(input) == output
