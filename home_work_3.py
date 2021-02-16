# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('task_3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        managers = line.split()
        manager = managers[0]
        money = float(managers[1])
        result = []
        if money < 20000:
            result.append(f'{manager}: {money}')
            print(result)

with open('task_3.txt', 'r', encoding='utf-8') as f:
    values = [float(line.split()[1]) for line in f]

with open('task_3.txt', 'r', encoding='utf-8') as f:
    string = 0
    for line in f:
        string += 1

print(f'Средняя велечина дохода всех сотрудников: {sum(values)/string}')



