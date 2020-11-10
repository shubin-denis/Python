# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re
from functools import reduce


def my_func(prev_val, val):
    return prev_val + val


lesson_dict = {}
with open('lessons.txt', encoding='utf-8') as file:
    my_list = file.readlines()

    for el in my_list:
        change_el = el.replace('-', '').replace('\n', '')
        new_list = re.sub(r'\(.*?\)', '', change_el).split()
        lesson_hours = reduce(my_func, map(int, new_list[1:]))
        lesson_dict[new_list[0]] = lesson_hours
    print(lesson_dict)
