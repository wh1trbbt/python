# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class NotNumber(ValueError):
    pass


my_list = []

while True:
    try:
        value = input('Ввести число, для выхода ввести q: ')
        if value == 'q':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as e:
        print(e, 'не число')

print(my_list)
