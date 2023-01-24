from reason.tag import POSTagger


def test_string_input():
    input_value = "10 tools from the file."
    output = [
        ("10", "CD"),
        ("tools", "NNS"),
        ("from", "IN"),
        ("the", "AT"),
        ("file", "NN"),
        (".", "."),
    ]
    assert POSTagger().tag(input_value) == output


def test_list_input():
    input_value = ["10", "tools", "from", "the", "file", "."]
    output = [
        ("10", "CD"),
        ("tools", "NNS"),
        ("from", "IN"),
        ("the", "AT"),
        ("file", "NN"),
        (".", "."),
    ]
    assert POSTagger().tag(input_value) == output
