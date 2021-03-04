# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class CheckZero:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def division_by_zero(a, b):
        try:
            return a / b
        except:
            return f'Деление на ноль'


print(CheckZero.division_by_zero(10, 2))
print(CheckZero.division_by_zero(10, 0))
