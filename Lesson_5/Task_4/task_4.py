# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.
rus_list = ['Один - 1\n', 'Два - 2\n', 'Три - 3\n', 'Четыре - 4']


with open('enum.txt', encoding='utf-8') as file:
    num_list = file.readlines()

# Вариант 1:

# with open('russian.txt', 'w', encoding='utf-8') as f:
#     for el in num_list:
#         print(el)
#         if '1' in el:
#             line = el.replace('One', 'Один')
#         if '2' in el:
#             line = el.replace('Two', 'Два')
#         if '3' in el:
#             line = el.replace('Three', 'Три')
#         if '4' in el:
#             line = el.replace('Four', 'Четыре')
#         f.write(line)


# Вариант 2:

with open('russian.txt', 'w', encoding='utf-8') as f:
    for i, element in enumerate(num_list):
        line = rus_list[i]

        f.write(line)


