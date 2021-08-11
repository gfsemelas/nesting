from nesting import get_indices

def test_get_indices():
    test_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
    assert get_indices(test_list, 'hello') == [3, 1, 2, 0]