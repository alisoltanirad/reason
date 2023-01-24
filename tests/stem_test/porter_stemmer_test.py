import pytest

from reason.stem import PorterStemmer, porter_stem
from reason.stem._porter import _PorterAlgorithm


def test_string_input():
    input_value = "watched birds flying"
    output = ["watch", "bird", "fly"]
    assert PorterStemmer().stem(input_value) == output


def test_list_input():
    input_value = ["watched", "birds", "flying"]
    output = ["watch", "bird", "fly"]
    assert PorterStemmer().stem(input_value) == output


def test_porter_stem():
    assert porter_stem("learning") == "learn"


def test_porter_stem_bad_input():
    with pytest.raises(TypeError):
        porter_stem(["learning"])


def test_step1a_1():
    assert _PorterAlgorithm("caresses").stem(1) == "caress"


def test_step1a_2():
    assert _PorterAlgorithm("ties").stem(1) == "ti"


def test_step1a_3():
    assert _PorterAlgorithm("caress").stem(1) == "caress"


def test_step1a_4():
    assert _PorterAlgorithm("cats").stem(1) == "cat"


def test_step1b_1():
    assert _PorterAlgorithm("feed").stem(1) == "feed"


def test_step1b_2():
    assert _PorterAlgorithm("agreed").stem(1) == "agree"


def test_step1b_3():
    assert _PorterAlgorithm("bled").stem(1) == "bled"


def test_step1b_4():
    assert _PorterAlgorithm("plastered").stem(1) == "plaster"


def test_step1b_5():
    assert _PorterAlgorithm("sing").stem(1) == "sing"


def test_step1b_6():
    assert _PorterAlgorithm("motoring").stem(1) == "motor"


def test_step1b_7():
    assert _PorterAlgorithm("conflated").stem(1) == "conflate"


def test_step1b_8():
    assert _PorterAlgorithm("troubled").stem(1) == "trouble"


def test_step1b_9():
    assert _PorterAlgorithm("sized").stem(1) == "size"


def test_step1b_10():
    assert _PorterAlgorithm("tanned").stem(1) == "tan"


def test_step1b_11():
    assert _PorterAlgorithm("falling").stem(1) == "fall"


def test_step1b_12():
    assert _PorterAlgorithm("failing").stem(1) == "fail"


def test_step1b_13():
    assert _PorterAlgorithm("filing").stem(1) == "file"


def test_step1c_1():
    assert _PorterAlgorithm("happy").stem(1) == "happi"


def test_step1c_2():
    assert _PorterAlgorithm("sky").stem(1) == "sky"


def test_step2_1():
    assert _PorterAlgorithm("relational").stem(2) == "relate"


def test_step2_2():
    assert _PorterAlgorithm("rational").stem(2) == "rational"


def test_step2_3():
    assert _PorterAlgorithm("conditional").stem(2) == "condition"


def test_step2_4():
    assert _PorterAlgorithm("valenci").stem(2) == "valence"


def test_step2_5():
    assert _PorterAlgorithm("hesitanci").stem(2) == "hesitance"


def test_step2_6():
    assert _PorterAlgorithm("digitizer").stem(2) == "digitize"


def test_step2_7():
    assert _PorterAlgorithm("conformabli").stem(2) == "conformable"


def test_step2_8():
    assert _PorterAlgorithm("radicalli").stem(2) == "radical"


def test_step2_9():
    assert _PorterAlgorithm("differentli").stem(2) == "different"


def test_step2_10():
    assert _PorterAlgorithm("vileli").stem(2) == "vile"


def test_step2_11():
    assert _PorterAlgorithm("analogousli").stem(2) == "analogous"


def test_step2_12():
    assert _PorterAlgorithm("vietnamization").stem(2) == "vietnamize"


def test_step2_13():
    assert _PorterAlgorithm("predication").stem(2) == "predicate"


def test_step2_14():
    assert _PorterAlgorithm("operator").stem(2) == "operate"


def test_step2_15():
    assert _PorterAlgorithm("feudalism").stem(2) == "feudal"


def test_step2_16():
    assert _PorterAlgorithm("decisiveness").stem(2) == "decisive"


def test_step2_17():
    assert _PorterAlgorithm("hopefulness").stem(2) == "hopeful"


def test_step2_18():
    assert _PorterAlgorithm("callousness").stem(2) == "callous"


def test_step2_19():
    assert _PorterAlgorithm("formaliti").stem(2) == "formal"


def test_step2_20():
    assert _PorterAlgorithm("sensitiviti").stem(2) == "sensitive"


def test_step2_21():
    assert _PorterAlgorithm("sensibiliti").stem(2) == "sensible"


def test_step3_1():
    assert _PorterAlgorithm("triplicate").stem(3) == "triplic"


def test_step3_2():
    assert _PorterAlgorithm("formative").stem(3) == "form"


def test_step3_3():
    assert _PorterAlgorithm("formalize").stem(3) == "formal"


def test_step3_4():
    assert _PorterAlgorithm("electriciti").stem(3) == "electric"


def test_step3_5():
    assert _PorterAlgorithm("electrical").stem(3) == "electric"


def test_step3_6():
    assert _PorterAlgorithm("hopeful").stem(3) == "hope"


def test_step3_7():
    assert _PorterAlgorithm("goodness").stem(3) == "good"


def test_step4_1():
    assert _PorterAlgorithm("revival").stem(4) == "reviv"


def test_step4_2():
    assert _PorterAlgorithm("allowance").stem(4) == "allow"


def test_step4_3():
    assert _PorterAlgorithm("inference").stem(4) == "infer"


def test_step4_4():
    assert _PorterAlgorithm("airliner").stem(4) == "airlin"


def test_step4_5():
    assert _PorterAlgorithm("gyroscopic").stem(4) == "gyroscop"


def test_step4_6():
    assert _PorterAlgorithm("adjustable").stem(4) == "adjust"


def test_step4_7():
    assert _PorterAlgorithm("defensible").stem(4) == "defens"


def test_step4_8():
    assert _PorterAlgorithm("irritant").stem(4) == "irrit"


def test_step4_9():
    assert _PorterAlgorithm("replacement").stem(4) == "replac"


def test_step4_10():
    assert _PorterAlgorithm("adjustment").stem(4) == "adjust"


def test_step4_11():
    assert _PorterAlgorithm("dependent").stem(4) == "depend"


def test_step4_12():
    assert _PorterAlgorithm("adoption").stem(4) == "adopt"


def test_step4_13():
    assert _PorterAlgorithm("homologou").stem(4) == "homolog"


def test_step4_14():
    assert _PorterAlgorithm("communism").stem(4) == "commun"


def test_step4_15():
    assert _PorterAlgorithm("activate").stem(4) == "activ"


def test_step4_16():
    assert _PorterAlgorithm("angulariti").stem(4) == "angular"


def test_step4_17():
    assert _PorterAlgorithm("homologous").stem(4) == "homolog"


def test_step4_18():
    assert _PorterAlgorithm("effective").stem(4) == "effect"


def test_step4_19():
    assert _PorterAlgorithm("bowdlerize").stem(4) == "bowdler"


def test_step5_1():
    assert _PorterAlgorithm("rate").stem(5) == "rate"


def test_step5_2():
    assert _PorterAlgorithm("probate").stem(5) == "probat"


def test_step5_3():
    assert _PorterAlgorithm("cease").stem(5) == "ceas"


def test_step5_4():
    assert _PorterAlgorithm("roll").stem(5) == "roll"


def test_step5_5():
    assert _PorterAlgorithm("controll").stem(5) == "control"


def test_is_consonant():
    assert _PorterAlgorithm("you")._is_consonant("you", 0) == True
