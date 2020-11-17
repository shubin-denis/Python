# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__() ), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

f_matrix = [[32, 26, 44], [12, 58, 34], [14, 25, 81]]
s_matrix = [[25, 31, 24], [14, 53, 38], [16, 44, 22]]


class Matrix:
    def __init__(self, my_list):
        self.matrix_list = my_list

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.matrix_list])

    def __add__(self, other):
        new_matrix = ''
        if len(self.matrix_list) == len(other):
            for el_1, el_2 in zip(self.matrix_list, other):
                # print(el_1)
                # print(el_2)
                if len(el_1) != len(el_2):
                    return 'Problems with shape'

                f_list = [num_1 + num_2 for num_1, num_2 in zip(el_1, el_2)]
                new_matrix += ' '.join([str(i) for i in f_list]) + '\n'
            return new_matrix
        else:
            return 'Problems with shape'


mat = Matrix(f_matrix)

print(mat)
print('\n')
print(mat + s_matrix)
