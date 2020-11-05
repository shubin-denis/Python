# 1)	Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script_name, operating_time, salary, prize = argv


def get_wages(time, money, more_money):
    return (int(time) * int(money)) + int(more_money)


print(f'Заработная плата составит: {get_wages(operating_time, salary, prize)}')
