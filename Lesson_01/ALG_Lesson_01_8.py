#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.


y = int(input('Введите год: '))

if y % 400 == 0:
    rez = f'{y} год - високосный.'
elif y % 100 == 0:
    rez = f'{y} год - не високосный.'
elif y % 4 == 0:
    rez = f'{y} год - високосный.'
else:
    rez = f'{y} год - не високосный.'

print(rez)




