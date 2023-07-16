# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# first_element = int(input('Введите значение первого элемента: '))
# difference = int(input('Введите значение разности, d='))
# number_of_elements = int(input('Введите количество элементов: '))
# progressive_list = []
# for n in range(0, number_of_elements):
#     if n == 0:
#         el = 0 + (n - 1) * difference
#     else:
#         el = progressive_list[0] + (n - 1) * difference
#     progressive_list.append(el)
# print(progressive_list)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
down_limit = int(input('Введите значение нижнего порога: '))
top_limit = int(input('Введите значение верхнего порога: '))

number_of_elements = 20
random_numbers = []
indexs_elements = []
for i in range(0, number_of_elements):
    random_numbers.append(randint(0, 100))
print(random_numbers)
for index, value in enumerate(random_numbers):
    if down_limit <= value <= top_limit:
        indexs_elements.append(index)
print(indexs_elements)