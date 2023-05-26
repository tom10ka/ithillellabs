import requests

url = 'https://dummyjson.com/users?limit=100'

response = requests.get(url)
data = response.json()
users = data['users']
brownheaded_number = 0
users_general_age = 0
users_from_lousville = []
for user in users:
    user_hair = user['hair']
    user_hair_color = user_hair.get('color', 0)
    user_address = user['address']
    user_city = user_address.get('city', 0)
    if user_city == 'Louisville':
        user_first_name = user.get('firstName', 'Noname')
        user_last_name = user.get('lastName', 'Nolastname')
        whole_name = f'{user_first_name} {user_last_name}'
        users_from_lousville.append(whole_name)
    if user_hair_color == 'Brown':
        brownheaded_number += 1
        user_age = user['age']
        users_general_age += user_age
if brownheaded_number > 0:
    average_age = users_general_age / brownheaded_number
    print(average_age)
else:
    print('There are no brownheaded persons')
users_from_lousville_number = len(users_from_lousville)
if users_from_lousville_number > 0:
    print(users_from_lousville)
else: 
    print('There are no humans from Louisville')
