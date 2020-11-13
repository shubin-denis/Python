# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = 'Green'

    def run(self, daemon=10):
        try:
            while daemon:
                print(self.__color)
                if self.__color == 'Yellow':
                    sleep(2)
                    self.__color = 'Green'
                elif self.__color == 'Green':
                    sleep(5)
                    self.__color = 'Red'
                elif self.__color == 'Red':
                    sleep(7)
                    self.__color = 'Yellow'
                else:
                    raise ValueError
                daemon -= 1
        except ValueError:
            print('Broken trafficLight')


t_light = TrafficLight()
t_light.run()
