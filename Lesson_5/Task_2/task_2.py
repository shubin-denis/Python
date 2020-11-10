# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open('text.txt') as file:
    lines = file.readlines()
    for num, line in enumerate(lines, start=1):
        line_list = line.split()
        print(f'Количество слов в строке {num} - {len(line_list)}')

print(f'Количество строк в файле - {len(lines)}')
