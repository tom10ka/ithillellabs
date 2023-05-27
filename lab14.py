def anecdote_number(number: int | float) -> str :
    if number == 1:
        anecdote = 'Мяч ще летів у вікно директора, а діти вже грали в хованки...'
    elif number == 2:
        anecdote = 'Все-таки є щось підозріле в назві газети "Рибак рибака"...'
    else:
        anecdote = 'Вночі прийшов кіт і скромно ліг у мене в ногах. А під ранок в ногах у кота спав вже я.'
    return anecdote


number = float(input('Write down number >>> '))
chosen_anecdote = anecdote_number(number)
print(chosen_anecdote)


def rectangle_perimeter(length: float | int, width: float | int) -> float | int:
    perimeter = length * width
    return perimeter


rectangle_length = float(input('Write down rectangle length >>> '))
rectangle_width = float(input('Write down rectangle width >>> '))
your_perimeter = rectangle_perimeter(rectangle_length, rectangle_width)
print(f'Perimeter of your rectangle is {your_perimeter}')


def letter_deleter(user_string: str) -> str:
    clean_string = ''
    for letter in user_string:
        if letter.lower() != 'ї' and letter.lower() != 'ж':
            clean_string += letter
    return clean_string


user_string = input('Write down sentence to clean, use ukrainian >>> ')
result = letter_deleter(user_string)
print(f'Your cleaned string is {result}')


def letter_deleter(user_string: str, deleted_symbols: set) -> str:
    clean_string = ''
    for letter in user_string:
        if letter.lower() in deleted_symbols:
            pass
        else:
            clean_string += letter
    return clean_string


string_1 = input('Write down first word/sentence >>> ')
string_2 = input('Write down second word/sentence >>>')
string_2 = string_2.lower()
unique_symbols_string_2 = set(string_2)
result = letter_deleter(string_1, unique_symbols_string_2)
print(f'Your cleaned string is {result}')
