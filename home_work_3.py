# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


pos_1 = Position('Иван', 'Семенов', 'Менеджер', 50000, 15000)
print('Имя Фамилия:', pos_1.get_full_name()+'\n'
      'Должность:', pos_1.position+'\n'
      'Оклад + премия:', pos_1.get_total_income())

print('-' * 28)

pos_2 = Position('Сергей', 'Бабушкин', 'Кассир', 30000, 5000)
print('Имя Фамилия:', pos_2.get_full_name()+'\n'
      'Должность:', pos_2.position+'\n'
      'Оклад + премия:', pos_2.get_total_income())


