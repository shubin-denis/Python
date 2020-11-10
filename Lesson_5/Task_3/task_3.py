# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('personal.txt', 'r', encoding='utf-8') as file:
    personal = file.readlines()
    salaries = []
    for el in personal:
        person = el.strip('\n')
        person_list = person.split()
        salaries.append(float(person_list[1]))
        if float(person_list[1]) < 20000:
            print(f'Зарплата меньше 20000 - {person_list[0]}')

    print(f'Средняя величина дохода сотрудников: {round(sum(salaries) / len(salaries), 2)}')