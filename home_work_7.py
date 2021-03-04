# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ClxNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}j'

    def __mul__(self, other):
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a}j'

    def __str__(self):
        return f'{self.a} + {self.b}j'


clx_1 = ClxNumber(-1, -2)
clx_2 = ClxNumber(3, 4)
print(clx_1)
print(clx_2)
print(clx_1 + clx_2)
print(clx_1 * clx_2)

