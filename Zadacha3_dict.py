# Пользователь вводит число N.
# Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.


n = int(input('Введите количество друзей: '))

friends = {}
for i in range(1, n+1):
    name = input('Введите имя: ')
    i = name
    age = int(input('Введите возраст: '))
    friends[i] = age

print('\n', friends)

count = 0
summa = 0
for key in friends:
    count += 1
    summa += friends[key]

print('\nСреднее значение возраста друзей: ', summa/count)
print('\nСаммое длинное имя - ', max(friends))

