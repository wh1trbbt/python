# 5. Запросите у пользователя значения выручки и издержек фирмы.

money = int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))

# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки) Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке)
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

profit = money - cost

if money - cost > 0:
    rent = profit / money * 100
    print(f'Фирма работает с рентабельностью {rent:.2f} %')
    worker = int(input('Введите количество сотрудников: '))
    workerProfit = profit / worker
    print(f'прибыль фирмы в расчете на одного сотрудника: {workerProfit:.2f}')
else:
    print('Фирма работает в убыток')
