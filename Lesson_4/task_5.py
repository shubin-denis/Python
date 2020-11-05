# 5)	Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат
# вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [num for num in range(100, 1001) if num % 2 == 0]


def get_multi(prev_digit, digit):
    return prev_digit * digit


result = reduce(get_multi, my_list)

print(result)
