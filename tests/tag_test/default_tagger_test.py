from reason.tag import DefaultTagger


def test_string_input():
    input_value = 'reason'
    output = [('reason', 'word')]
    assert DefaultTagger('word').tag(input_value) == output

def test_list_input():
    input_value = ['reason']
    output = [('reason', 'word')]
    assert DefaultTagger('word').tag(input_value) == output
