import pytest

from reason.tokenize import word_tokenize as wt


@pytest.fixture
def input_value():
    input_value = "Hi:) I'm testing reason0.1.0, (on: 127.0.0.1). Cool stuff..."
    return input_value


def test_default_string(input_value):
    output = [
        "Hi",
        ":)",
        "I'm",
        "testing",
        "reason0.1.0",
        ",",
        "(",
        "on",
        ":",
        "127.0.0.1",
        ")",
        ".",
        "Cool",
        "stuff",
        "...",
    ]
    assert wt(input_value) == output


def test_word(input_value):
    output = ["Hi", "I'm", "testing", "reason0.1.0", "on", "127.0.0.1", "Cool", "stuff"]
    assert wt(input_value, "word") == output


def test_alphanumeric(input_value):
    output = ["Hi", "I'm", "testing", "reason0.1.0", "on", "127.0.0.1", "Cool", "stuff"]
    assert wt(input_value, "alphanumeric") == output


def test_alpha(input_value):
    output = ["Hi", "I'm", "testing", "reason", "on", "Cool", "stuff"]
    assert wt(input_value, "alpha") == output


def test_alpba_pure(input_value):
    output = ["Hi", "I", "m", "testing", "reason", "on", "Cool", "stuff"]
    assert wt(input_value, "alpha-pure") == output


def test_numeric(input_value):
    output = ["0.1.0", "127.0.0.1"]
    assert wt(input_value, "numeric") == output


def test_numeric_pure(input_value):
    output = ["0", "1", "0", "127", "0", "0", "1"]
    assert wt(input_value, "numeric-pure") == output


def test_non_alphanumeric(input_value):
    output = [":)", "'", ".", ".", ",", "(", ":", ".", ".", ".", ")", ".", "..."]
    assert wt(input_value, "non-alphanumeric") == output


def test_ideogram(input_value):
    output = [":)"]
    assert wt(input_value, "ideogram") == output


def test_list_input(input_value):
    output = [
        "Hi",
        ":)",
        "I'm",
        "testing",
        "reason0.1.0",
        ",",
        "(",
        "on",
        ":",
        "127.0.0.1",
        ")",
        ".",
        "Cool",
        "stuff",
        "...",
    ]
    assert wt([input_value], "default") == output


def test_bad_input():
    with pytest.raises(TypeError):
        wt(1)


def test_custom_pattern():
    assert wt("10", r"\d") == ["1", "0"]


def test_custom_pattern_bad_input():
    with pytest.raises(TypeError):
        wt("10", 1)
