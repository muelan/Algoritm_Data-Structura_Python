'''2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
      на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.'''

import random

n = int(input('Введите длину массива: '))
array = [round(random.uniform(0, 49.99), 2) for i in range(n)]

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

print(f'Исходный массив: {array}')

print(f'Отсортированный массив: {merge_sort(array)}')
