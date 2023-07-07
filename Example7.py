# Задача 16
# n = int(input('Введите количество элементов в списке: '))
# list_with_numbers = input('Введите последовательность чисел через пробел: ').split()
# print(list_with_numbers)
# x = int(input('Введите искомое число: '))
# count = 0
# for digit in list_with_numbers:
#     if int(digit) == x:
#         count += 1
# print(f'Число {x} встречается {count} раз(а).')


# Задача 16
n = int(input('Введите количество элементов в списке: '))
list_with_numbers = input('Введите последовательность чисел через пробел: ').split()
print(list_with_numbers)
x = int(input('Введите число: '))
difference = 99999999999999999999
res = 0
for digit in list_with_numbers:
    if abs(x - int(digit)) < difference:
        difference = abs(x - int(digit))
        res = int(digit)
print(f'К числу {x} самое близкое {res}.')
