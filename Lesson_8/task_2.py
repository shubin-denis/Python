# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.

class OwnError(Exception):
    def __init__(self, text):
        self.text = text

    @staticmethod
    def divide_numbers():
        try:
            num_1 = int(input('Введите первое число: '))
            num_2 = int(input('Введите второе число: '))
            if num_2:
                return f'Ответ: {int(num_1 / num_2)}'
            else:
                raise OwnError('Делить на 0 нельзя')
        except OwnError as err:
            return err
        except ValueError:
            return 'Вы ввели не число!'


print(OwnError.divide_numbers())
