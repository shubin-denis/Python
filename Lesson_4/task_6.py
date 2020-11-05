# 6)	Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle

# a) count()

for num in count(4, 2):
    if num > 20:
        break
    print(num)

# b) cycle()

polys = ['triangle', 'square', 'pentagon', 'rectangle']
count = 0

for value in cycle(polys):
    if count > 11:
        break
    print(value)
    count += 1
