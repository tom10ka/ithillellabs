# 1
numbers_list = [1, 1.4, 12, 121.2]
new_numbers_list = []
for list_character in numbers_list:
    list_character = str(list_character*2)
    new_numbers_list.append(list_character)
print(new_numbers_list)

# 2
surnames_list = []
new_surname = input('Write pupils surname, input "stop" when you finish >>> ').capitalize()
if new_surname != 'Stop':
    surnames_list.append(new_surname)
    for new_surname in surnames_list:
        if new_surname != 'Stop':
            new_surname = input('Write pupils surname >>> ').capitalize()
            surnames_list.append(new_surname)
        else:
            surnames_list.remove('Stop')
            surnames_list.sort()
            print(surnames_list)
            break
else:
    print('List is empty')

# 3
letters_list = str(input('Write down letters and numbers order >>> '))
letters_list_length = len(letters_list)
right_letters_list = ''
for letters_list_length in letters_list:
    if letters_list_length.isupper() == True:
        right_letters_list = right_letters_list + letters_list_length
    else:
        continue
if len(right_letters_list) == 0:
    print('String is empty, there are no proper characters')
else:
    print(str(right_letters_list))

# 4
from decimal import Decimal

temperature_celcium = float(input('Write down todays temperature >>> '))
temperature_fahrenheit = (temperature_celcium * 9 / 5) + 32
temperature_fahrenheit = Decimal(str(temperature_fahrenheit)).quantize(Decimal("1.0"))
print(temperature_fahrenheit)
