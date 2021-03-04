# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.


class Date:

    def __init__(self, date=str(input('Ввести дату в формате "Число-Месяц-Год": '))):
        self.date = date

    @classmethod
    def numbers(cls):
        date = list(map(int, cls().date.split('-')))
        day = date[0]
        month = date[1]
        year = date[2]
        if cls.validate(day, month, year):
            print(day, month, year)

    @staticmethod
    def validate(day, month, year):
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 2022:
            print(day, month, year)
        else:
            print('Ошибка')


Date.numbers()






