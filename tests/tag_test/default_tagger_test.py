from reason.tag import DefaultTagger


def test_string_input():
    input = 'reason'
    output = [('reason', 'word')]
    assert DefaultTagger('word').tag(input) == output

def test_list_input():
    input = ['reason']
    output = [('reason', 'word')]
    assert DefaultTagger('word').tag(input) == output
