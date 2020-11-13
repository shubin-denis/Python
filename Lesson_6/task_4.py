# Реализуйте базовый класс Car . У данного класса должны быть следующие атрибуты: speed ,
# color , name , is_police (булево). А также методы: go , stop , turn(direction) , которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar , SportCar , WorkCar , PoliceCar . Добавьте в базовый класс метод
# show_speed , который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed . При значении скорости свыше 60
# ( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Сar started moving'

    def stop(self):
        return 'Сar stopped'

    def turn(self, direction):
        return f'Car turned {direction}'

    def show_speed(self):
        return f'Car speed - {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'The speed limit is exceeded'
        else:
            return f'Car speed - {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'The speed limit is exceeded'
        else:
            return f'Car speed - {self.speed}'


class PoliceCar(Car):
    pass


t_car = TownCar(60, 'red', 'Toyota')
s_car = SportCar(90, 'blue', 'Mersedes-Benz')
w_car = WorkCar(50, 'green', 'Ford')
p_car = PoliceCar(80, 'black', 'Chevrolet', True)

print(t_car.color)
print(s_car.name)
print(w_car.speed)
print(p_car.is_police)
print(t_car.go())
print(s_car.stop())
print(p_car.turn('left'))
print(t_car.show_speed())
print(w_car.show_speed())

