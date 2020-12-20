from reason.analysis import FreqDist


def test_str_input():
    input = 'hey hey oh oh oh yeah'
    output = [('hey', 2), ('oh', 3), ('yeah', 1)]
    assert FreqDist(input).get_data() == output

def test_list_input():
    input = ['hey', 'hey', 'oh', 'oh', 'oh', 'yeah']
    output = [('hey', 2), ('oh', 3), ('yeah', 1)]
    assert FreqDist(input).get_data() == output

def test_most_common():
    input = ['hey', 'hey', 'oh', 'oh', 'oh', 'yeah']
    output = [('oh', 3), ('hey', 2)]
    assert FreqDist(input).most_common(2) == output

def test_key_value():
    input = ['hey', 'hey', 'oh', 'oh', 'oh', 'yeah']
    assert FreqDist(input)['hey'] == 2

def test_copy():
    input = ['hey', 'hey', 'oh', 'oh', 'oh', 'yeah']
    fd1 = FreqDist(input)
    fd2 = fd1.copy()
    fd1['yeah'] = 4
    assert fd2.most_common() == [('oh', 3)]
