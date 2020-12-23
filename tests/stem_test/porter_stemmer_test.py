from reason.stem import PorterStemmer, porter_stem


def test_step1a_1():
    assert porter_stem('caresses') == 'caress'

def test_step1a_2():
    assert porter_stem('ties') == 'ti'

def test_step1a_3():
    assert porter_stem('caress') == 'caress'

def test_step1a_4():
    assert porter_stem('cats') == 'cat'

