'''1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
      (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
      (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
      и отдельно вывести наименования предприятий, чья прибыль ниже среднего.'''

import collections

n = int(input('Введите количество предприятий: '))

company = collections.defaultdict()
comp_profit = []        # Словарь предприятий с доходностью выше среднего
comp_unprofit = []      # Словарь предприятий с доходностью ниже среднего
profit_all = 0          # Общая прибыль одного предприятия
quarter_all = 4         # Общее количество отчетных кварталов

for i in range(n):
    name = input(f'\nНазвание {i+1}-го предприятия: ')
    profit_year = 0                 # Прибыль одного предприятия за год
    for q in range(quarter_all):
        profit = float(input(f'Прибыль за {q+1}-й квартал: '))
        profit_year += profit
    company[name] = profit_year
    profit_all += profit_year
print(company)

profit_mid = profit_all / n         # Средняя прибыль всех предприятий

for i, item in company.items():
    if item >= profit_mid:
        comp_profit.append(i)
    else:
        comp_unprofit.append(i)


print(f'\nСредняя прибыль предприятий: {profit_mid}')
print(f'\nПрибыль выше среднего у {len(comp_profit)} компаний:')
for i in comp_profit:
    print(i)
print(f'\nПрибыль ниже среднего у {len(comp_unprofit)} компаний:')
for i in comp_unprofit:
    print(i)
