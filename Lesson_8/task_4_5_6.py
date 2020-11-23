# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class Warehouse:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.product_dict = []

    def warehouse_deposit(self, *args):
        for val in args:
            self.product_dict.append(val)
        return self.product_dict


class Equipment:
    def __init__(self):
        self.name = ''
        self.price = ''
        self.quantity = ''
        self.product_list = {}

    def set_product(self):
        try:
            self.name = input('Введите название товара: ')
            self.price = int(input('Введите цену товара: '))
            self.quantity = int(input('Введите количество товара: '))
            unique = {'Product': self.name, 'Price': self.price, 'Quantity': self.quantity}
        except:
            return f'Ошибка ввода данных!'
        else:
            self.product_list.update(unique)
            return self.product_list


class Printer(Equipment):

    def __init__(self, view):
        super().__init__()
        self.view = view


class Scanner(Equipment):

    def __init__(self, model):
        super().__init__()
        self.model = model


class Xerox(Equipment):

    def __init__(self, color_type):
        super().__init__()
        self.color_type = color_type


xerox = Xerox('black')
printer = Printer('laser')
scanner = Scanner('color')
w = Warehouse(50, 12, 5)

print(w.warehouse_deposit(xerox.set_product(), printer.set_product(), scanner.set_product()))
