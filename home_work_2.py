# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task_2.txt', 'r', encoding='utf-8') as f:
    string = 0
    for line in f:
        string += 1

print(f'В файле task_2.txt {string} строк')

with open('task_2.txt', 'r', encoding='utf-8') as f:
    i = 1
    for line in f:
        print(f'В {i}-й строке {len(line.split())} слов(а)')
        i += 1
