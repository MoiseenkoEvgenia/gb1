# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = input('Введите число: ')
# sum_of_digits = 0
# for num in number:
#     sum_of_digits += int(num)
# print(f'Сумма цифр в числе {number} равна {sum_of_digits}.')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# number_of_cranes = int(input('Введите количество журавликов: '))
# kates_cranes = round(number_of_cranes * 2 / 3)
# peter_cranes = round(kates_cranes / 2 / 2)
# sergey_cranes = round(peter_cranes)
# print(f'Петя - {peter_cranes}, Катя - {kates_cranes} и Сережа - {sergey_cranes} журавликов.')


# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет 
# с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

# number_of_ticket = input('Введите номер билета: ')
# sum_of_left_digits, sum_of_right_digits = 0, 0
# current_position_digit = 1
# for digit in number_of_ticket:
#     if current_position_digit <= len(number_of_ticket)/2:
#         sum_of_left_digits += int(digit)
#     if current_position_digit > len(number_of_ticket)/2:
#         sum_of_right_digits += int(digit)
#     current_position_digit +=1
# if sum_of_left_digits == sum_of_right_digits:
#     print(f'Да! Билет счастливый!')
# else:
#     print(f'Нет! Билет несчастливый!')