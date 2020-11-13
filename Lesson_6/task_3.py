# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name ,
# surname , position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker .
# В классе Position реализовать методы получения полного имени сотрудника ( get_full_name ) и
# дохода с учетом премии ( get_total_income ). Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


# Либо можно сразу определить оклад и премию в __init__:
#         self._income_wage = income['wage']
#         self._income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income


# Тогда расчет будет таким:
#     def get_total_income(self):
#         total_income = self._income_wage + self._income_bonus
#         return total_income

worker_position = Position('Ivan', 'Ivanov', 'manager', {'wage': 25000, 'bonus': 15000})

f_name = worker_position.get_full_name()
t_income = worker_position.get_total_income()

print(f'Сотрудник {f_name} получил {t_income} рублей')
