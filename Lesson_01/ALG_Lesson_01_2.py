#2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

print('Результата операции "AND": ' + str(5 & 6))
print('Результата операции "OR": ' + str(5 | 6))
print('Результата операции "XOR": ' + str(5 ^ 6))
print('Результата операции "NOT 5": ' + str(~5))
print('Результата операции "NOT 6": ' + str(~6))
print('Результата операции "СДВИГ ВЛЕВО на 2": ' + str(5<<2))
print('Результата операции "СДВИГ ВПРАВО на 2": ' + str(5>>2))