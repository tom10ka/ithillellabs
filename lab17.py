def convert_number_in_list(value: int):
    if value > 1:
        user_list = [value]*10
        new_set = {char+n for char in user_list for n in range (0, 10)}
        new_list = list(new_set)
        return new_list
    else:
        raise ValueError

