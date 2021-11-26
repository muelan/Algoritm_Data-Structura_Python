#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
#   Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
#   в последнюю ячейку строки. В конце следует вывести полученную матрицу.
m = 5
n = 4
rez = []
for i in range(m):
    line = input(f'Введите {i+1}-ю строку матрицы {m}x{n-1} (элементы через пробел): ')
    matr_str = line.split()
    summa = 0
    for j in range(n-1):
        summa += int(matr_str[j])
    if len(matr_str) < n:  # Проверка, если пользователь ввел бОльшее количество элементов строки
        matr_str.append(summa)
    else:
        matr_str[n - 1] = summa
    rez.append(matr_str)

for i in range(m):
    for j in range(n):
        print(f'{rez[i][j]}', end='\t')
    print()











