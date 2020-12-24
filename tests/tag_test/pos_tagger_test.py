from reason.tag import POSTagger


def test_string_input():
    input = '10 tools from the file'
    output = [('10', 'CD'), ('tools', 'NNS'), ('from', 'IN'), ('the', 'AT'),
              ('file', 'NN')]
    assert POSTagger().tag(input) == output

def test_list_input():
    input = ['10', 'tools', 'from', 'the', 'file']
    output = [('10', 'CD'), ('tools', 'NNS'), ('from', 'IN'), ('the', 'AT'),
              ('file', 'NN')]
    assert POSTagger().tag(input) == output
