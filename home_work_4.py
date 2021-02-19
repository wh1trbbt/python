# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            return f'{self.name} {self.color} поехала, это полицейская машина'
        return f'{self.name} {self.color} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'повернула {direction}'

    def show_speed(self):
        return f'скорость {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'превышение скорости! {self.speed} км/ч'
        return f'скорость {self.speed} км/ч  в пределах разумной'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'превышение скорости!'
        return f'скорость {self.speed} км/ч в пределах разумной'


class PoliceCar(Car):
    pass


town = TownCar('Lincoln', 'Black', 70, False)
print(f'{town.go()}, {town.show_speed()}, {town.turn("направо")}, {town.stop()}')
sport = SportCar('Subaru', 'Grey', 240, False)
print(f'{sport.go()}, {sport.show_speed()}, {sport.turn("налево")}, {sport.stop()}')
work = WorkCar('Gazel', 'White', 40, False)
print(f'{work.go()}, {work.show_speed()}, {work.turn("налево, направо")}, {work.stop()}')
police = PoliceCar('Mercedes', 'Blue', 90, True)
print(f'{police.go()}, {police.show_speed()}, {police.turn("на месте")}, {police.stop()}')
