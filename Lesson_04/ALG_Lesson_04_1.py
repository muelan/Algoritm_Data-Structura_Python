'''1. Проанализировать скорость и сложность одного любого алгоритма,
   разработанных в рамках домашнего задания первых трех уроков.
   Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

   2. Написать два алгоритма нахождения i-го по счёту простого числа.
   Без использования «Решета Эратосфена»;
   Используя алгоритм «Решето Эратосфена»
   Примечание ко всему домашнему заданию:
   Проанализировать скорость и сложность алгоритмов.
   Результаты анализа сохранить в виде комментариев в файле с кодом.'''

import timeit
import math
import cProfile


# Верхняя граница отрезка, на котором лежат i простых чисел. Используем i/ln(i).
def f_prime_n(i):
    prime_n = 0
    n = 2
    while prime_n <= i:
        prime_n = n/math.log(n)
        n += 1
    return n

def f_Eratosthenes(i):
    '''Поиск i-го простого числа по алгоритму «Решето Эратосфена»'''

    n = f_prime_n(i)
    a = [0] * n

    # заполнение массива чисел
    for j in range(n):
        a[j] = j

    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    # Вывод массива
    b = []
    for j in a:
        if a[j] != 0:
            b.append(a[j])
    del a
    return b[i-1]


def f_No_Eratosthenes_1(i):
    '''Поиск i-го простого числа без «Решета Эратосфена».
    Проверка каждого числа и формирование отдельного массива простых чисел.
    '''

    a = [2]         # Массив простых чисел
    number = 3

    while len(a) < i:
        flag = False            # Признак простого числа
        for j in a.copy():
            if number % j != 0:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            a.append(number)
        number += 1
    return a[-1]


def f_Eratosthenes_comby(i):
    '''Поиск i-го простого числа. Моё + «Решето Эратосфена».
    '''

    n = f_prime_n(i)
    a = [0] * n

    # заполнение массива чисел
    for j in range(n):
        a[j] = j

    a[1] = 0
    m = 2
    for m in range(n):
        if a[m] != 0:
            j = m * 2       # Стандарт
            j2 = m **2      # Добавлено обнуление квадратов простых чисел
            j3 = m **3      # Добавлено обнуление кубов простых чисел
            while j < n:
                a[j] = 0
                j = j + m
            while j2 < n:
                a[j2] = 0
                j2 = j2 + m
            while j3 < n:
                a[j3] = 0
                j3 = j3 + m
        m += 1
    b = []
    for j in a:
        if a[j] != 0:
            b.append(a[j])
    del a
    return b[i - 1]


# Анализ
for i in range(1, 5):
    test_in = 10**i
    print(f'{test_in}-ое простое число')
    print('Решето Эратосфена: ', timeit.timeit(f'f_Eratosthenes({test_in})', setup='from __main__ import f_Eratosthenes', number=1))
    print('Без решета Эратосфена : ', timeit.timeit(f'f_No_Eratosthenes_1({test_in})', setup='from __main__ import f_No_Eratosthenes_1', number=1))
    print('Решето Эратосфена КОМБИ: ', timeit.timeit(f'f_Eratosthenes_comby({test_in})', setup='from __main__ import f_Eratosthenes_comby', number=1))
    print()
