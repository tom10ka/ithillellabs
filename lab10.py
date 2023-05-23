#1
cities_visited = input('Write down cities visited last 10 years, use "space" between them >>> ')
cities_wished = input('Write down cities you wish to visit, use "space" between them >>> ')
cities_visited = cities_visited.lower().title()
cities_wished = cities_wished.lower().title()
cities_visited_list = cities_visited.split()
cities_wished_list = cities_wished.split()
cities_visited_set = set(cities_visited_list)
cities_wished_set = set(cities_wished_list)
cities_liked_list = list(cities_wished_set & cities_visited_set)
cities_liked_list_length = len(cities_liked_list)
if cities_liked_list_length > 0:
    cities_liked_string = ''
    for cities in cities_liked_list:
        if cities != cities_liked_list[-1]:
            cities_liked_string = cities_liked_string + f' {cities},'
        else:
            cities_liked_string = cities_liked_string + f' {cities_liked_list[-1]}.'
    template_for_print = f'It seems you liked a lot visiting{cities_liked_string}'
    print(template_for_print)
else:
    print('It seems that you are opened for new impressions')

#2
from pprint import pprint
students = {
  'Іван Петров': {
    'Пошта': 'Ivan@gmail.com',
    'Вік': 14,
    'Номер телефону': '+380987771221',
    'Середній бал': 95.8
  },
  'Женя Курич': {
    'Пошта': 'Geka@gmail.com',
    'Вік': 16,
    'Номер телефону': None,
    'Середній бал': 64.5
  },
  'Маша Кера': {
    'Пошта': 'Masha@gmail.com',
    'Вік': 18,
    'Номер телефону': '+380986671221',
    'Середній бал': 80
  },
}
students_number = len(students)
students_1 = students['Женя Курич']
students_1['Вік'] = 25
print(f'Number of students is {students_number}')
pprint(students)
