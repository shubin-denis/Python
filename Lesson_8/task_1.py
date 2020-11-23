# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.
date = '15-12-2020'


class Date(object):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def extracting_number(cls, str_date):
        day, month, year = map(int, str_date.split('-'))
        date_1 = cls(day, month, year)
        return date_1

    @staticmethod
    def is_date_valid(str_date):
        day, month, year = map(int, str_date.split('-'))
        try:
            if month > 12 or year > 2022:
                raise ValueError
            return month, year
        except ValueError:
            return 'Invalid date'


date_num = Date.extracting_number(date)
print(date_num.day, date_num.month, date_num.year)
print((Date.is_date_valid(date)))
