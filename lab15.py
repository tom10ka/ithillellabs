from typing import Any


def kilometers_in_miles(value: int | float) -> int | float:
    try:
        if value >= 0:
            reverse = value * 0.6217
            return reverse
        else:
            raise ValueError
    except TypeError:
        return 0


def convert_in_tuple(value: Any) -> tuple:
    type_value = type(value)
    if type_value is list:
        value_set = set(value)
        sorted_value_set = sorted(value_set)
        value_tuple = tuple(sorted_value_set)
        return value_tuple
    elif type_value is set:
        sorted_value = sorted(value)
        value_tuple = tuple(sorted_value)
        return value_tuple
    elif type_value is str:
        clean_list = []
        for character in value:
            clean_list.append(character)
        value_set = set(clean_list)
        sorted_value_set = sorted(value_set)
        value_tuple = tuple(sorted_value_set)
        return value_tuple
    elif type_value is dict:
        value_keys = value.keys()
        value_set = set(value_keys)
        sorted_value_set = sorted(value_set)
        value_tuple = tuple(sorted_value_set)
        return value_tuple
    else:
        return tuple()



valval = 'abc'
val = convert_in_tuple(valval)
print(val)