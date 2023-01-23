import pytest

from reason.tokenize import sent_tokenize as st


def test_string_input():
    input_value = "Hey, what's up? I love using Reason library!"
    output = ["Hey, what's up?", "I love using Reason library!"]
    assert st(input_value) == output


def test_list_input():
    input_value = [
        "Hey",
        ",",
        "what's",
        "up",
        "?",
        "I",
        "love",
        "using",
        "Reason",
        "library",
        "!",
    ]
    output = [
        ["Hey", ",", "what's", "up", "?"],
        ["I", "love", "using", "Reason", "library", "!"],
    ]
    assert st(input_value) == output


def test_bad_input():
    with pytest.raises(TypeError):
        st(1)
