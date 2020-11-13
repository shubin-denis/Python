# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw . Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return f'Предмет {self.title} - запуск отрисовки.'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки с помощью {self.title}а.'


class Handle(Stationery):
    def draw(self):
        return f'Отрисовано {self.title}ом.'


stationery = Stationery()
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

print(stationery.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
