# Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

number_1 = 5
number_2 = 12
print(number_1 * number_2)

name = 'Denis'
last_name = 'Shubin'
print(f'Меня зовут: {name} {last_name}')

answer_1 = input('Вы больше любите числа или строки: ')

if answer_1 == 'числа':
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    sum = first_number + second_number
    print(f'При сложении получится {sum}')
elif answer_1 == 'строки':
    str_1 = input('Введите первую строку: ')
    str_2 = input('Введите вторую строку: ')
    print('Давайте попробуем сконкатенировать строки: ')
    print(str_1 + ' ' + str_2)
else:
    print('У нас разные интересы!')
