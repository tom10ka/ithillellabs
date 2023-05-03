# очікуваний результат у вигляді: My name is David, I am 14 years old👣

smile_footprint = '\U0001F463'
user_name = input('Please, enter your name >>> ').capitalize().strip()
user_age = input('Please, enter your age >>> ').strip()
result = f'My name is {user_name}, I am {user_age}{smile_footprint}'
print(result)
