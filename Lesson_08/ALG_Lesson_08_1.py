'''1. Определение количества различных подстрок с использованием хэш-функции.
      Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
      Требуется найти количество различных подстрок в этой строке.'''


# Работает с любым алфавитом

from itertools import permutations
import hashlib
import re



s = input('Введите строку маленькими латинскими буквами: ')
arr_str = []       # Массив для хранения подстрок
arr_hash = []      # Массив для хранения хеш

if re.search(r'^[a-z]+$', s):
    # Заполнение массива подстрок (комбинаторика - размещения)
    for i in range(1, len(s) + 1):
        for j in permutations(s, i):
            arr_str.append(''.join(j))
    print(f'\nМассив подстрок с повторениями:\n{arr_str}')
    print()

    # Заполнение массива хеш
    for i in range(len(arr_str)):
        arr_hash.append(hashlib.sha1(arr_str[i].encode('utf-8')).hexdigest())
    print(f'Количество всех подстрок: {len(arr_hash)}')

    count_sub = len(set(arr_hash))
    print(f'Количество уникальных подстрок: {count_sub}')

else:
    print('Ошибка ввода')





