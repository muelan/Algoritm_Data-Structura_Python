#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.



# Если минимальный (максимальный) элемент дублируется, то берется первый.

import random

n = int(input('Введите размерность массива: '))
a = [0] * n
for i in range(n):
    a[i] = random.randint(1,100)

print(f'Исходный массив: {a}')

i_min = 0
i_max = 0
for i in range(n):
    if a[i] < a[i_min]:
        i_min = i
    if a[i] > a[i_max]:
        i_max = i

tmp = a[i_max]
a[i_max] = a[i_min]
a[i_min] = tmp


print(f'Измененный массив: {a}')









