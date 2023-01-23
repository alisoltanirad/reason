import pytest

from reason.tag import LookupTagger


def test_string_input():
    input_value = "a black cat"
    output = [("a", ""), ("black", "color"), ("cat", "animal")]
    lookup_data = {"cat": "animal", "black": "color"}
    assert LookupTagger(lookup_data).tag(input_value) == output


def test_list_input():
    input_value = ["a", "black", "cat"]
    output = [("a", ""), ("black", "color"), ("cat", "animal")]
    lookup_data = {"cat": "animal", "black": "color"}
    assert LookupTagger(lookup_data).tag(input_value) == output


def test_bad_input():
    with pytest.raises(TypeError):
        LookupTagger(["x", "token"])
