from reason.tag import DefaultTagger, LookupTagger


def test_backoff():
    input = 'a black cat'
    output = [('a', 'token'), ('black', 'color'), ('cat', 'animal')]
    lookup_data = {'cat': 'animal', 'black': 'color'}
    tagger = DefaultTagger('token')
    assert LookupTagger(lookup_data, backoff=tagger).tag(input) == output
