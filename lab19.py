import csv

with open(file='homework_file.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    names_list = []
    for row in list(reader):
        value = row.get('iso_country')
        if value == 'UA':
            airport_name = row.get('name')
            names_list.append(airport_name)
    new_str = ''
    for name in names_list:
        if name != names_list[-1]:
            new_str += f'{name}, '
        else:
            new_str += f'{name}.'
    print(new_str)
