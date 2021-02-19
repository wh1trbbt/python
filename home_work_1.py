# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами
# должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.


import time
from termcolor import cprint


def counter(sec):
    while sec:
        print(sec+1 - 1, end='\t')
        time.sleep(1)
        sec -= 1
    return print()


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        self.__color = '(☼)'
        cprint(self.__color, 'red', attrs=['bold'])
        counter(7)
        cprint(self.__color, 'yellow', attrs=['bold'])
        counter(2)
        cprint(self.__color, 'green', attrs=['bold'])
        counter(3)


traffic_1 = TrafficLight()
traffic_1.running()
