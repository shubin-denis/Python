# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

user_seconds = int(input('Введите количество секунд: '))

hours = user_seconds // 3600
minutes = (user_seconds // 60) - (hours * 60)
seconds = user_seconds % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')
