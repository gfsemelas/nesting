from nesting import replace_element

def test_replace_element():
    old_d = {'k1': [1, 2, 3, {'funny': ['oh', 'no', 'lie', {'destiny': [1, 2, 3, 'hello']}]}]}
    new_d = {'k1': [1, 2, 3, {'funny': ['oh', 'no', 'truth', {'destiny': [1, 2, 3, 'hello']}]}]}
    assert replace_element(old_d, 'mentira', 'verdad') == new_d