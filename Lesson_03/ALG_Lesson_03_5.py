#5. В массиве найти максимальный отрицательный элемент.
#   Вывести на экран его значение и позицию в массиве.


import random

n = int(input('Введите размерность массива: '))
a = [0] * n
for i in range(n):
    a[i] = int(random.random() * 100 - 50)
print(f'Исходный массив: {a}')

num = 0
num_i = 0
for i in range(n):
    if a[i] < 0:
        num = a[i]

if num != 0:
    for i in range(n):
        if a[i] < 0 and a[i] > num:
            num = a[i]
            num_i = i
    print(f'Максимальный отрицательный элемент {num}, позиция {num_i+1}.')  # Позиция считается с 1
else:
    print('Отрицательных элементов нет.')






