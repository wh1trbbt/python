# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.


seasons = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_1 = {1: 'Зимний месяц', 2: 'Весенний месяц', 3: 'Летний месяц', 4: 'Осенний месяц'}

month = 0
mode = 0

while True:
    mode = input('Введите ЛИСТ для работы через list / Введите СЛОВАРЬ для работы через dict / Q для выхода: ').upper()
    if mode == 'ЛИСТ':
        while True:
            try:
                while month < 1 or month > 12:
                    month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
            except ValueError:
                print('Не целое число или строка')
            else:
                if month <= 2 or month == 12:
                    print(seasons[0])
                elif month <= 5:
                    print(seasons[1])
                elif month <= 8:
                    print(seasons[2])
                else:
                    print(seasons[3])
                break
    elif mode == 'СЛОВАРЬ':
        while True:
            try:
                while month < 1 or month > 12:
                    month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
            except ValueError:
                print('Не целое число или строка')
            else:
                if month <= 2 or month == 12:
                    print(seasons_1[1])
                elif month <= 5:
                    print(seasons_1[2])
                elif month <= 8:
                    print(seasons_1[3])
                else:
                    print(seasons_1[4])
                break
    elif mode == 'Q':
        break
    else:
        print('Нужно выбрать режим работы!')
