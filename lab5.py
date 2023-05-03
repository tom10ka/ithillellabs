user_name = input('Введіть ваше імя ').capitalize().strip('1234567890')
user_surname = input('Введіть ваше прізвище ').upper().strip('1234567890')
name_length = len(user_name)
template = 'Привіт, {user_name} {user_surname}, а ти знав, що твоє імя складається з {name_length} літер'
user_info = template.format(user_name=user_name, user_surname=user_surname, name_length=name_length)
template_new = user_info.replace('Привіт', 'Здарова')
point_4 = f'{template_new}?'
print(point_4)
