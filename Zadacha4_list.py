#Создайте пустой список и добавьте в него 10 случайных чисел и выведите их/
#Удалите все элементы из списка

import random
from random import randint


list1 = []
for i in range(10):
    list1.append(random.randint(1, 20))
print(list1)

list1.clear()
print(list1)