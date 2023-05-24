﻿"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку 
здійснюється за механізмом 
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення, 
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
from pprint import pprint

student = {
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
# ваш код нижче
student_names = student['Іван Петров'].keys()
new_student_dict = dict.fromkeys(student_names)
new_student_email = input('Write down your email >>> ')
new_student_age = int(input('Write down your age >>> '))
new_student_cellphone = input('Write down your cellphone number >>> ')
new_student_points = float(input('Write down your average points >>> '))
if new_student_points == int(new_student_points):
    new_student_points = int(new_student_points)
elif type(new_student_points) == float:
    new_student_points = float(new_student_points)
else:
    print('Wrong type of average points, try int or float type')
if 18 < new_student_age < 40:
    new_student_dict['Пошта'] = new_student_email
    new_student_dict['Вік'] = new_student_age
    new_student_dict['Номер телефону'] = new_student_cellphone
    new_student_dict['Середній бал'] = new_student_points
    student['Сергій Іванов'] = new_student_dict
else:
    print('Entry age is between 18 and 40, so we cant add you, try again ')
for students_name in student:
    cellphone_check = student[students_name]['Номер телефону']
    if cellphone_check is None or cellphone_check == '':
        parent_number = input(f'Please, write down parent number for {students_name} >>> ')
        student[students_name]['Номер телефону'] = parent_number
    else:
        pass
pprint(student)
number_of_students = len(student.keys())
whole_points = 0
point = 0
great_students_list = []
for student_point in student:
    point = student[student_point]['Середній бал']
    whole_points += float(point)
    if float(point) > 90:
        great_students_list.append(student_point)
    else:
        pass
average_class_point = whole_points / number_of_students
great_students_string = ''
if len(great_students_list) > 1:
    for great_student in great_students_list:
        if great_student == great_students_list[-1]:
            great_students_string += f' {great_student}.'
        else:
            great_students_string += f' {great_student},'
    print(f'The best pupils in class are{great_students_string}')
elif len(great_students_list) == 1:
    print(f'The best pupil is {great_students_list[0]}')
else:
    print('There is no pupils with point higher than 90')
print(f'Average class point is {average_class_point}')
