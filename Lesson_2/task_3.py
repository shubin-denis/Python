# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number_of_month = int(input('Введите номер месяца: '))
# 1) Решение через list

# list_of_seasons = ['зима', 'весна', 'лето', 'осень']
#
# if 0 < number_of_month <= 2 or 11 < number_of_month < 13:
#     print(f'Такой месяц относится к времени года "{list_of_seasons[0]}"')
# elif 3 <= number_of_month <= 5:
#     print(f'Такой месяц относится к времени года "{list_of_seasons[1]}"')
# elif 6 <= number_of_month <= 8:
#     print(f'Такой месяц относится к времени года "{list_of_seasons[2]}"')
# elif 9 <= number_of_month <= 11:
#     print(f'Такой месяц относится к времени года "{list_of_seasons[3]}"')
# else:
#     print('Такого месяца не существует!')

# Решение через dict

dict_of_seasons = {'зима': [1, 2, 12],
                   'весна': [3, 4, 5],
                   'лето': [6, 7, 8],
                   'осень': [9, 10, 11]
                   }
if number_of_month <= 0 or number_of_month > 12:
    print('Такого месяца не существует!')
else:
    for el, month in dict_of_seasons.items():
        month_list = list(month)
        i = 0
        while i < len(month_list):
            if number_of_month == month_list[i]:
                print(f'Такой месяц относится к времени года "{el}"')
            i += 1



