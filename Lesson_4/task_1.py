# 1)	Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script_name, operating_time, salary, prize = argv


def get_wages(time, money, more_money):
    return time * money + more_money


try:
    int(operating_time)
    int(salary)
    int(prize)
except ValueError:
    print('Введен неверный формат данных!')
else:
    print(f'Заработная плата составит: {get_wages(int(operating_time), int(salary), int(prize))}')


