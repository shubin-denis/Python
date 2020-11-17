# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда , которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм . У этих типов одежды существуют
# параметры: размер (для пальто ) и рост (для костюма ). Это могут быть обычные числа: V и
# H , соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param_1, param_2=None):
        self.param_1 = param_1
        self.param_2 = param_2

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param_1 / 6.5) + 0.5)


class Suit(Clothes):
    @property
    def calculate(self):
        return round(2 * self.param_1 + 0.3)


class TotalOutlay(Clothes):

    @property
    def calculate(self):
        return self.param_1 + self.param_2


coat = Coat(170)
suit = Suit(45)
t_outlay = TotalOutlay(coat.calculate, suit.calculate)

print(coat.calculate)
print(suit.calculate)
print(t_outlay.calculate)
