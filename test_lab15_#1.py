import lab15

import pytest


def test_kilometers_in_miles_int():
    value = 2
    assert lab15.kilometers_in_miles(value) == 1.2434


def test_kilometers_in_miles_float():
    value = 2.0
    assert lab15.kilometers_in_miles(value) == 1.2434


def test_kilometers_in_miles_negative_value():
    value = -2
    with pytest.raises(ValueError):
        assert lab15.kilometers_in_miles(value) == 0


def test_kilometers_in_miles_zero():
    value = 0
    assert lab15.kilometers_in_miles(value) == 0


def test_kilometers_in_miles_another_type():
    value = 'fewfsef'
    assert lab15.kilometers_in_miles(value) == 0
