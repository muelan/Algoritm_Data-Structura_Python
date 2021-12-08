'''1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
      в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
      эффективным использованием памяти.

      Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной
      и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
      Также укажите в комментариях версию Python и разрядность вашей ОС.'''

import math

from memory_profiler import profile
#import memory_profiler


# Верхняя граница отрезка, на котором лежат i простых чисел. Используем i/ln(i).
def f_prime_n(i):
    prime_n = 0
    n = 2
    while prime_n <= i:
        prime_n = n/math.log(n)
        n += 1
    return n

@profile
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



@profile
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


@profile
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


test_in = 5000

#if __name__ == '__main__':
#    f_Eratosthenes(test_in)

#if __name__ == '__main__':
#    f_No_Eratosthenes_1(test_in)

if __name__ == '__main__':
    f_Eratosthenes_comby(test_in)


'''

ВАРИАНТ 1. РЕШЕТО ЭРАТОСФЕНА - 5000 чисел

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    24     19.7 MiB     19.7 MiB           1   @profile
    25                                         def f_Eratosthenes(i):
    26                                             #Поиск i-го простого числа по алгоритму «Решето Эратосфена»
    27                                         
    28     19.7 MiB      0.0 MiB           1       n = f_prime_n(i)
    29     20.1 MiB      0.4 MiB           1       a = [0] * n
    30                                         
    31                                             # заполнение массива чисел
    32     21.7 MiB      0.0 MiB       54535       for j in range(n):
    33     21.7 MiB      1.6 MiB       54534           a[j] = j
    34                                         
    35     21.7 MiB      0.0 MiB           1       a[1] = 0
    36     21.7 MiB      0.0 MiB           1       m = 2
    37     21.7 MiB      0.0 MiB       54533       while m < n:
    38     21.7 MiB      0.0 MiB       54532           if a[m] != 0:
    39     21.7 MiB      0.0 MiB        5548               j = m * 2
    40     21.7 MiB      0.0 MiB      142195               while j < n:
    41     21.7 MiB      0.0 MiB      136647                   a[j] = 0
    42     21.7 MiB      0.0 MiB      136647                   j = j + m
    43     21.7 MiB      0.0 MiB       54532           m += 1
    44                                         
    45                                             # Вывод массива
    46     21.7 MiB      0.0 MiB           1       b = []
    47     21.9 MiB      0.0 MiB       54535       for j in a:
    48     21.9 MiB      0.0 MiB       54534           if a[j] != 0:
    49     21.9 MiB      0.2 MiB        5548               b.append(a[j])
    50     21.4 MiB     -0.5 MiB           1       del a
    51     21.4 MiB      0.0 MiB           1       return b[i-1]



Process finished with exit code 0


'''


'''
ВАРИАНТ 2. БЕЗ РЕШЕТА ЭРАТОСФЕНА - 5000 чисел

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    55     19.7 MiB     19.7 MiB           1   @profile
    56                                         def f_No_Eratosthenes_1(i):
    57                                             #Поиск i-го простого числа без «Решета Эратосфена».
    58                                             #Проверка каждого числа и формирование отдельного массива простых чисел.
    59                                             
    60                                         
    61     19.7 MiB      0.0 MiB           1       a = [2]         # Массив простых чисел
    62     19.7 MiB      0.0 MiB           1       number = 3
    63                                         
    64     20.3 MiB   -571.3 MiB       48610       while len(a) < i:
    65     20.3 MiB   -571.3 MiB       48609           flag = False            # Признак простого числа
    66     20.3 MiB -198301.2 MiB    12639015           for j in a.copy():
    67     20.3 MiB -171455.6 MiB    12634016               if number % j != 0:
    68     20.3 MiB -170940.3 MiB    12590406                   flag = True
    69                                                     else:
    70     20.3 MiB   -515.3 MiB       43610                   flag = False
    71     20.3 MiB   -515.3 MiB       43610                   break
    72     20.3 MiB   -571.4 MiB       48609           if flag == True:
    73     20.3 MiB    -56.1 MiB        4999               a.append(number)
    74     20.3 MiB   -571.4 MiB       48609           number += 1
    75     20.3 MiB      0.0 MiB           1       return a[-1]



Process finished with exit code 0


'''



'''
ВАРИАНТ 3.  РЕШЕТО ЭРАТОСФЕНА (комбинированный метод) - 5000 чисел



Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    78     19.7 MiB     19.7 MiB           1   @profile
    79                                         def f_Eratosthenes_comby(i):
    80                                             Поиск i-го простого числа. Моё + «Решето Эратосфена».
    81                                             
    82                                         
    83     19.7 MiB      0.0 MiB           1       n = f_prime_n(i)
    84     20.1 MiB      0.4 MiB           1       a = [0] * n
    85                                         
    86                                             # заполнение массива чисел
    87     21.7 MiB      0.0 MiB       54535       for j in range(n):
    88     21.7 MiB      1.6 MiB       54534           a[j] = j
    89                                         
    90     21.7 MiB      0.0 MiB           1       a[1] = 0
    91     21.7 MiB      0.0 MiB           1       m = 2
    92     21.7 MiB      0.0 MiB       54535       for m in range(n):
    93     21.7 MiB      0.0 MiB       54534           if a[m] != 0:
    94     21.7 MiB      0.0 MiB        5548               j = m * 2       # Стандарт
    95     21.7 MiB      0.0 MiB        5548               j2 = m **2      # Добавлено обнуление квадратов простых чисел
    96     21.7 MiB      0.0 MiB        5548               j3 = m **3      # Добавлено обнуление кубов простых чисел
    97     21.7 MiB      0.0 MiB      142195               while j < n:
    98     21.7 MiB      0.0 MiB      136647                   a[j] = 0
    99     21.7 MiB      0.0 MiB      136647                   j = j + m
   100     21.7 MiB      0.0 MiB      107729               while j2 < n:
   101     21.7 MiB      0.0 MiB      102181                   a[j2] = 0
   102     21.7 MiB      0.0 MiB      102181                   j2 = j2 + m
   103     21.7 MiB      0.0 MiB       87683               while j3 < n:
   104     21.7 MiB      0.0 MiB       82135                   a[j3] = 0
   105     21.7 MiB      0.0 MiB       82135                   j3 = j3 + m
   106     21.7 MiB      0.0 MiB       54534           m += 1
   107     21.7 MiB      0.0 MiB           1       b = []
   108     21.8 MiB      0.0 MiB       54535       for j in a:
   109     21.8 MiB      0.0 MiB       54534           if a[j] != 0:
   110     21.8 MiB      0.1 MiB        5548               b.append(a[j])
   111     21.3 MiB     -0.5 MiB           1       del a
   112     21.3 MiB      0.0 MiB           1       return b[i - 1]



Process finished with exit code 0

'''