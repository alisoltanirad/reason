from reason.tokenize import sent_tokenize as st


def test_string():
    input_value = "Hey, what's up? I love using Reason library!"
    output = ["Hey, what's up?", 'I love using Reason library!']
    assert st(input_value) == output

def test_list():
    input_value = ['Hey', ',', "what's", 'up', '?', 'I', 'love', 'using', 'Reason',
             'library', '!']
    output = [['Hey', ',', "what's", 'up', '?'],
              ['I', 'love', 'using', 'Reason', 'library', '!']]
    assert st(input_value) == output
