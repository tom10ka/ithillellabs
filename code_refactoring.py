# очікуваний результат у вигляді: My name is David, I am 14 years old👣

# example
# f = '\N{Footprints}'  # not informative naming, the correct code below
smile_footprint = '\U0001F463'
user_name = input().capitalize()
user_age = input('Please, enter your age >>> ')
result = f'My name is {user_name}, I am {user_age}{smile_footprint}'
print(result)
