'''2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
      При этом каждое число представляется как массив, элементы которого это цифры числа.
      Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
      Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].'''

from collections import deque

hex1_str = input('Введите 1-ое шестнадцатеричное число: ')
hex2_str = input('Введите 2-ое шестнадцатеричное число: ')
hex1 = []
hex2 = []


# Перевод в САРS
for i in range(len(hex1_str)):
    hex1.append(hex1_str[i].upper())
for i in range(len(hex2_str)):
    hex2.append(hex2_str[i].upper())


# Определение бОльшего числа по длине
if len(hex1) >= len(hex2):
    hex1, hex2 = deque(hex1), deque(hex2)
else:
    hex1, hex2 = deque(hex2), deque(hex1)


# Сумма чисел
def sum_hex (hex1, hex2):
    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    sum_rez = deque()
    k = 0           # Счетчик переходящих разрядов

    if len(hex1) < len(hex2):
        hex1, hex2 = hex2, hex1

    for i in range(len(hex1)):
        if i in range(len(hex2)):
            rez = hex_num[hex1[len(hex1) - 1 - i]] + hex_num[hex2[len(hex2) - 1 - i]] + k
        else:
            rez = hex_num[hex1[len(hex1) - 1 - i]] + k
        k = 0
        if rez < 16:
            sum_rez.appendleft(hex_num[rez])
        else:
            sum_rez.appendleft(hex_num[rez - 16])
            k = 1
    if k == 1:
        sum_rez.appendleft('1')
    return sum_rez


# Произведение чисел
def mult_hex (hex1, hex2):

    mult_sum = deque()  # Вспомогательный словарь для хранения всех слагаемых при умножении

    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    # Формирование слагаемых

    if len(hex2) > 1:
        for i in range(len(hex2)):
            mult_hlp = deque()  # Вспомогательный словарь для формирования одного слагаемого
            k = 0                   # Счетчик переходящих разрядов
            for j in range(len(hex1)):
                rez =  hex_num[hex1[len(hex1) - 1 - j]] * hex_num[hex2[len(hex2) - 1 - i]] + k
                if rez < 16:
                    mult_hlp.appendleft(hex_num[rez])
                    k = 0
                else:
                    mult_hlp.appendleft(hex_num[rez % 16])
                    k = rez // 16
            if k > 0:
                mult_hlp.appendleft(hex_num[k])
            mult_sum.append(mult_hlp)
    else:
        k = 0
        mult_hlp = deque()  # Вспомогательный словарь для формирования одного слагаемого
        for j in range(len(hex1)):
            rez = hex_num[hex1[len(hex1) - 1 - j]] * hex_num[hex2[0]] + k
            if rez < 16:
                mult_hlp.appendleft(hex_num[rez])
                k = 0
            else:
                mult_hlp.appendleft(hex_num[rez % 16])
                k = rez // 16
        if k > 0:
            mult_hlp.appendleft(hex_num[k])
        mult_sum.append(mult_hlp)

    # Формирование общего результата (суммирование)
    if len(mult_sum) > 1:
        mult_rez = mult_sum[0]               # Окончательный результат
        for i in range(1, len(mult_sum)):
            for j in range(i):
                mult_sum[i].append('0')
            mult_rez = sum_hex(mult_rez, mult_sum[i])
    else:
        mult_rez = mult_sum[0]

    return mult_rez

print()
print(f'{hex1_str.upper()} + {hex2_str.upper()} =', ''.join(sum_hex(hex1, hex2)))
print()
print(f'{hex1_str.upper()} * {hex2_str.upper()} =', ''.join(mult_hex(hex1, hex2)))