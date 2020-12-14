from reason.tokenize import word_tokenize as wt


def test_default_string():
    input = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    output = ['Hi', ':)', "I'm", 'testing', 'reason0.1.0', ',', '(', 'on', ':',
              '127.0.0.1', ')', '.', 'Cool', 'stuff', '...']
    assert wt(input) == output

def test_word():
    input = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    output = ['Hi', "I'm", 'testing', 'reason0.1.0', 'on', '127.0.0.1', 'Cool',
              'stuff']
    assert wt(input, 'word') == output

def test_alphanumeric():
    input = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    output = ['Hi', "I'm", 'testing', 'reason0.1.0', 'on', '127.0.0.1', 'Cool',
              'stuff']
    assert wt(input, 'alphanumeric') == output

def test_alpha():
    input = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    output = ['Hi', "I'm", 'testing', 'reason', 'on', 'Cool', 'stuff']
    assert wt(input, 'alpha') == output

def test_alpba_pure():
    input = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    output = ['Hi', 'I', 'm', 'testing', 'reason', 'on', 'Cool', 'stuff']
    assert wt(input, 'alpha-pure') == output

def test_numeric():
    input = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    output = ['0.1.0', '127.0.0.1']
    assert wt(input, 'numeric') == output

def test_numeric_pure():
    input = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    output = ['0', '1', '0', '127', '0', '0', '1']
    assert wt(input, 'numeric-pure') == output

def test_non_alphanumeric():
    input = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    output = [':)', "'", '.', '.', ',', '(', ':', '.', '.', '.', ')', '.',
              '...']
    assert wt(input, 'non-alphanumeric') == output

def test_ideogram():
    input = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    output = [':)']
    assert wt(input, 'ideogram') == output

def test_list_input():
    input = ["Hi:) I'm testing reason0.1.0,", "(on: 127.0.0.1). Cool stuff..."]
    output = ['Hi', ':)', "I'm", 'testing', 'reason0.1.0', ',', '(', 'on', ':',
              '127.0.0.1', ')', '.', 'Cool', 'stuff', '...']
    assert wt(input, 'default') == output