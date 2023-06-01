import lab15

import pytest


def test_convert_in_tuple_str():
    test_value = 'acb'
    assert lab15.convert_in_tuple(test_value) == ('a', 'b', 'c')


def test_convert_in_tuple_list():
    test_value = ['a', 'c', 'b']
    assert lab15.convert_in_tuple(test_value) == ('a', 'b', 'c')


def test_convert_in_tuple_set():
    test_value = {'a', 'c', 'b'}
    assert lab15.convert_in_tuple(test_value) == ('a', 'b', 'c')


def test_convert_in_tuple_dict():
    test_value = {
        'c': 1,
        'a': 2,
        'b': 3,
    }
    assert lab15.convert_in_tuple(test_value) == ('a', 'b', 'c')


def test_convert_in_tuple_int():
    test_value = 1
    assert lab15.convert_in_tuple(test_value) == ()


def test_convert_in_tuple_wrong_type():
    test_value = ['a', 1, 'T', '!']
    with pytest.raises(TypeError):
        assert lab15.convert_in_tuple(test_value) == ()


def test_convert_in_tuple_wrong_value():
    test_value = False
    assert lab15.convert_in_tuple(test_value) == ()
