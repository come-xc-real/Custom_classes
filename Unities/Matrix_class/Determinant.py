from Matrix import Matrix
from Unities.InverseNumber_class.InverseNumber_class import InverseNumber, FullyArrange
from Unities.Fraction_class.RegularFraction_class import RegularFraction


class Determinant:
    def __init__(self, matrix_body: list, is_matrix_body_cleaned: bool = False):
        if len(matrix_body) != len(matrix_body[0]):
            raise "该矩阵不是正方形的"
        if not is_matrix_body_cleaned:
            self.body = Matrix(matrix_body).body_cleaned
        else:
            self.body = matrix_body

        self.len = len(matrix_body)
        self.fully_arrange = FullyArrange(self.len).result
        self.value = RegularFraction(0, 1)
        self._get_value()

    def _get_value(self):
        for arrange in self.fully_arrange:
            inverse_number_i = InverseNumber(arrange=arrange).inverse_number
            if inverse_number_i % 2 == 0:
                res_i = RegularFraction(1, 1)
            else:
                res_i = RegularFraction(-1, 1)
            for x_i, y_i in zip(arrange, range(self.len)):
                res_i *= self.body[y_i][x_i]
            self.value += res_i

    def __str__(self):
        return str(Matrix(self.body, is_matrix_body_cleaned=True))


if __name__ == '__main__':
    m_1 = Determinant([
        [1, 3, -1, 2],
        [1, -5, 3, -4],
        [0, 2, 1, -1],
        [-5, 1, 3, -3]
    ])
    print(m_1)
    print(m_1.value)
