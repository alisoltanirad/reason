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

def test_step1b_3():
    assert porter_stem('bled') == 'bled'

def test_step1b_4():
    assert porter_stem('plastered') == 'plaster'

def test_step1b_5():
    assert porter_stem('sing') == 'sing'

def test_step1b_6():
    assert porter_stem('motoring') == 'motor'

def test_step1b_7():
    assert porter_stem('conflated') == 'conflate'

def test_step1b_8():
    assert porter_stem('troubled') == 'trouble'

def test_step1b_9():
    assert porter_stem('sized') == 'size'

def test_step1b_10():
    assert porter_stem('tanned') == 'tan'

def test_step1b_11():
    assert porter_stem('falling') == 'fall'

def test_step1b_12():
    assert porter_stem('failing') == 'fail'

def test_step1b_13():
    assert porter_stem('filing') == 'file'

def test_step1c_1():
    assert porter_stem('happy') == 'happi'

def test_step1c_2():
    assert porter_stem('sky') == 'sky'

def test_step2_1():
    assert porter_stem('relational') == 'relate'

def test_step2_2():
    assert porter_stem('rational') == 'rational'

def test_step2_3():
    assert porter_stem('conditional') == 'condition'

def test_step2_4():
    assert porter_stem('valenci') == 'valence'

def test_step2_5():
    assert porter_stem('hesitanci') == 'hesitance'

def test_step2_6():
    assert porter_stem('digitizer') == 'digitize'

def test_step2_7():
    assert porter_stem('conformabli') == 'conformable'

def test_step2_8():
    assert porter_stem('radicalli') == 'radical'

def test_step2_9():
    assert porter_stem('differentli') == 'different'

def test_step2_10():
    assert porter_stem('vileli') == 'vile'

def test_step2_11():
    assert porter_stem('analogousli') == 'analogous'

def test_step2_12():
    assert porter_stem('vietnamization') == 'vietnamize'

def test_step2_13():
    assert porter_stem('predication') == 'predicate'

def test_step2_14():
    assert porter_stem('operator') == 'operate'

def test_step2_15():
    assert porter_stem('feudalism') == 'feudal'

def test_step2_16():
    assert porter_stem('decisiveness') == 'decisive'

def test_step2_17():
    assert porter_stem('hopefulness') == 'hopeful'

def test_step2_18():
    assert porter_stem('callousness') == 'callous'

def test_step2_19():
    assert porter_stem('formaliti') == 'formal'

def test_step2_20():
    assert porter_stem('sensitiviti') == 'sensitive'

def test_step2_21():
    assert porter_stem('sensibiliti') == 'sensible'
