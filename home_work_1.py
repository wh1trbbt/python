# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open('task_1.txt', 'w', encoding='utf-8') as f:
    content = True
    while content:
        content = input('Введите что-нибудь, если ввести пустую строку, ввод закончится: ')
        f.writelines(f'{content}\n')
        if not content:
            break

with open('task_1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end="")
