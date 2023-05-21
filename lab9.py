# 1
numbers_list = [1, 1.4, 12, 121.2]
new_numbers_list = []
for list_character in numbers_list:
    list_character = str(list_character * 2)
    new_numbers_list.append(list_character)
print(new_numbers_list)

# 2
new_surname = input('Write pupils surnames using space >>> ')
new_list = new_surname.split()
new_list_2 = []
for capital_letter in new_list:
    capital_letter = capital_letter.capitalize()
    new_list_2.append(capital_letter)
new_list_2 = sorted(new_list_2)
print(new_list_2)

# 3
letters_list = str(input('Write down letters and numbers order >>> '))
symbol = len(letters_list)
right_letters_string = ''
for symbol in letters_list:
    if symbol.isupper() == True:
        right_letters_string = right_letters_string + symbol
    else:
        continue
if len(right_letters_string) == 0:
    print('String is empty, there are no proper characters')
else:
    print(str(right_letters_string))

# 4
from decimal import Decimal

temperature_celcium = float(input('Write down todays temperature >>> '))
temperature_fahrenheit = (temperature_celcium * 9 / 5) + 32
temperature_fahrenheit = Decimal(str(temperature_fahrenheit)).quantize(Decimal("1.0"))
print(temperature_fahrenheit)
