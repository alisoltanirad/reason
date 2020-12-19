from reason.tokenize import sent_tokenize as st


def test_string():
    input = "Hey, what's up? I love using Reason library!"
    output = ["Hey, what's up?", 'I love using Reason library!']
    assert st(input) == output

def test_list():
    input = ['Hey', ',', "what's", 'up', '?', 'I', 'love', 'using', 'Reason',
             'library', '!']
    output = [['Hey', ',', "what's", 'up', '?'],
              ['I', 'love', 'using', 'Reason', 'library', '!']]
    assert st(input) == output
