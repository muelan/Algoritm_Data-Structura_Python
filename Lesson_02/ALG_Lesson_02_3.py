#1. 2. Посчитать четные и нечетные цифры введенного натурального числа.
#   Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = abs(int(input('Введите натуральное число: ')))
number_new = 0
flag = True      # счетчик цифр в number

while flag:
    if number // 10 >=1:                    # Проверка максимального разряда
        m = number % 10
        number = number // 10
        number_new = number_new * 10 + m
    else:
        m = number % 10
        number_new = number_new * 10 + m
        flag = False
        
print(f'Перевернутое число: {number_new}')