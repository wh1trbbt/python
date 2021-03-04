class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

    @property
    def dict(self):
        return self._dict


class Equipment:
    def __init__(self, name, model, year, price):
        self.name = name
        self.model = model
        self.year = year
        self.price = price
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'Название: {self.name} | Модель: {self.model} | Год: {self.year} | Цена: {self.price}\n'


class Printer(Equipment):
    def __init__(self, name, model, year, price):
        super().__init__(name, model, year, price)

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, model, year, price):
        super().__init__(name, model, year, price)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, model, year, price):
        super().__init__(name, model, year, price)

    def action(self):
        return 'Копирует'


warehouse = Warehouse()
printer = Printer('Brother', 1011, 2009, 15000)
warehouse.add_to(printer)
scaner = Scaner('Hp', 'Scanjet-200', 2015, 24000)
warehouse.add_to(scaner)
scaner = Scaner('Hp', 'Scanjet-300', 2017, 34000)
warehouse.add_to(scaner)
xerox = Xerox('Xerox', 'Phaser-3020', 2019, 7800)
warehouse.add_to(xerox)
print('Добавили на склад:\n')
print(f'{warehouse.dict}\n')
warehouse.extract('Scaner')
print('Забрали со склада: Scaner\n')
print(warehouse.dict)
