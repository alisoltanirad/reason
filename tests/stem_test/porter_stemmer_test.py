from reason.stem import PorterStemmer, porter_stem


def test_step1a_1():
    assert porter_stem('caresses') == 'caress'

def test_step1a_2():
    assert porter_stem('ties') == 'ti'

def test_step1a_3():
    assert porter_stem('caress') == 'caress'

def test_step1a_4():
    assert porter_stem('cats') == 'cat'

def test_step1b_1():
    assert porter_stem('feed') == 'feed'

def test_step1b_2():
    assert porter_stem('agreed') == 'agree'

def test_step1b_1():
    assert porter_stem('bled') == 'bled'

def test_step1b_1():
    assert porter_stem('plastered') == 'plaster'

def test_step1b_1():
    assert porter_stem('sing') == 'sing'

def test_step1b_1():
    assert porter_stem('motoring') == 'motor'

def test_step1b_1():
    assert porter_stem('conflated') == 'conflate'

def test_step1b_1():
    assert porter_stem('troubled') == 'trouble'

def test_step1b_1():
    assert porter_stem('sized') == 'size'

def test_step1b_1():
    assert porter_stem('tanned') == 'tan'

def test_step1b_1():
    assert porter_stem('falling') == 'fall'

def test_step1b_1():
    assert porter_stem('failing') == 'fail'

def test_step1b_1():
    assert porter_stem('filing') == 'file'
