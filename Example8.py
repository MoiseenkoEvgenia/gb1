"""задача 22"""
# n = int(input('Введите количество элементов в 1 списке: '))
# m = int(input('Введите количество элементов в 2 списке: '))
# n_list = input('Введите последовательность чисел в 1 списке через пробел: ').split()
# m_list = input('Введите последовательность чисел в 2 списке через пробел: ').split()
# i = 0
# while i < len(n_list):
#     if (n_list[i] in m_list):
#         i += 1
#     else:
#         n_list.remove(n_list[i])
#         i -= 1
# n_list = list(set(n_list))
# n_list.sort()
# m_list.sort()
# print(f'Встречающиеся в обоих списка числа в порядке возрастания {n_list}')


"""Задача 24"""
number_of_bushes = int(input('Введите количество кустов: '))
number_of_berries = input('Введите количество ягод на каждом кусте через пробел: ').split()
max_berries = 0
for index in range(0, len(number_of_berries)):
    current_berries = int(number_of_berries[index]) + int(number_of_berries[index-1]) + int(number_of_berries[index-2])
    if current_berries > max_berries:
        max_berries = current_berries
print(f'Максимально можно собрать {max_berries} ягод.')