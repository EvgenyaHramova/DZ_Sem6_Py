# Пользователь вводит число N. 
# Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.



n = int(input('Введите количество друзей: '))
friends = {}

for i in range(1, n+1):
    name = input('Введите имя: ')
    i = name
    age = int(input('Введите возраст: '))
    friends[i] = age

print('\n', friends)

print('\nМладшего из друзей зовут ', min(friends, key=friends.get))
