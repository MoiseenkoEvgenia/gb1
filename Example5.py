"""Задача 2: Найдите сумму цифр трехзначного числа."""
# number = input('Введите число: ')
# sum_of_digits = 0
# for num in number:
#     sum_of_digits += int(num)
# print(f'Сумма цифр в числе {number} равна {sum_of_digits}.')


"""Задача 4: Петя, Катя и Сережа делают из бумаги журавликов."""
# number_of_cranes = int(input('Введите количество журавликов: '))
# kates_cranes = round(number_of_cranes * 2 / 3)
# peter_cranes = round(kates_cranes / 2 / 2)
# sergey_cranes = round(peter_cranes)
# print(f'Петя - {peter_cranes}, Катя - {kates_cranes} и Сережа - {sergey_cranes} журавликов.')


"""Задача 6: Счастливый билет"""
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