#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# Заодно сделала минимум и максимум )))


a = float(input('Число 1: '))
b = float(input('Число 2: '))
c = float(input('Число 3: '))

if a <= b:
    if a <= c:
        if b <= c:
            mn = a
            md = b
            mx = c
        else:
            mn = a
            md = c
            mx = b
    else:
        mn = c
        md = a
        mx = b
else:
    if a <= c:
        mn = b
        md = a
        mx = c
    else:
        if b <= c:
            mn = b
            md = c
            mx = a
        else:
            mn = c
            md = b
            mx = a

print(f'Минимально число: {mn}')
print(f'Среднее число: {md}')
print(f'Максимальное число: {mx}')




