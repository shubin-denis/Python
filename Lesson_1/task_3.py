# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input('Введите целое число от 1 до 9: ')
number_2 = user_number + user_number
number_3 = number_2 + user_number
amount = int(user_number) + int(number_2) + int(number_3)

print(amount)
