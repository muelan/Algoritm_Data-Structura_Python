#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# Размерность 1xn и nx1 не учитывала
import random

print('Введите размерность массива:')
m = int(input('  - строк: '))
n = int(input('  - столбцов: '))
a = []      # Исходная матрица
arr_min = [0]*n  # Массив минимальных значений столбцов

for i in range(m):      # Формирование матрицы
    a.append(list(str(int(random.random() * 100))))
    for j in range(n-2):        # Выводит нормально, но  есть вопрос. Надо осудить.
       a[i].append(str(int(random.random() * 100)))
# Почему-то при выводе матрицы возникает ошибка, но не часто. Закономерности не увидела.



print(f'Исходная матрица:')
for i in range(m):
    for j in range(n):
        print(f'{a[i][j]}', end='\t')
    print()


# Массив минимальных значений столбцов

for j in range(n):  # Берем j-й столбец
    mn = int(a[0][j])
    #print(type(mn))
    #print('Старт mn = ', mn)
    for i in range(m):   # Пробегаем по нему
        if mn > int(a[i][j]):
            mn = int(a[i][j])
        #print(f'[{i}, {j}] {a[i][j]} mn = {mn}')
    arr_min[j] = mn
    #print('Финиш mn = ', mn)
    #print()
print(f'Массив минимальных значений: {arr_min}')

# Поиск максимального из минимальных
rez = arr_min[0]
for i in range(n):
    if arr_min[i] > rez:
        rez = arr_min[i]

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {rez}')




