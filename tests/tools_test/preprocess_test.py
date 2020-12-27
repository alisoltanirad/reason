import pytest

from reason import preprocess


def test_string_input():
    input_value = "What's up? I love using Reason library!"
    output = [
        ["what's", 'up', '?'], ['i', 'love', 'us', 'reason', 'librari', '!']
    ]
    assert preprocess(input_value) == output

def test_bad_input():
    with pytest.raises(TypeError):
        preprocess(1)
