# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

user_seconds = int(input('Введите количество секунд: '))

hours = user_seconds // 3600
minutes_on_hours = hours * 60
minutes = (user_seconds // 60) - minutes_on_hours
seconds_sum = (hours * 3600) + (minutes * 60)
seconds = user_seconds % seconds_sum

print(f'{hours}:{minutes}:{seconds}')
