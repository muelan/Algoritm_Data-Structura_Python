'''1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
      заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
      Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).'''

import random
import timeit

# Обычный метод
def f_sort_p_1(arr):
    for k in range(1, n):
        for i in range(n - k):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# С использованием рекурсии
def f_sort_p_2(arr, k, j, n):
    if k >= n:
        return
    elif j >= n-k:
        k += 1
        j = 0
    if arr[j] < arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    f_sort_p_2(arr, k, j + 1, n)



n = int(input('Введите длину массива: '))
array = [random.randint(-100,100) for i in range(n)]
print(f'Исходный массив: {array}')


# Вариант 1
f_sort_p_1(array)
print()
print(f'Результат 1. Обычная сортировка: {array}')
print('Время выполнения: ', timeit.timeit(setup='from __main__ import f_sort_p_1', number=1))


# Вариант 2
k = 1
j = 0
f_sort_p_2(array, k, j, n)
print(f'Результат 2. Рекурсия: {array}')
print('Время выполнения: ', timeit.timeit(setup='from __main__ import f_sort_p_2', number=1))