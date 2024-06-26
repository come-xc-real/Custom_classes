import copy
from Unities.Fraction_class.RegularFraction_class import RegularFraction

"""
此文中的row是列的意思
"""


class Matrix:
    """
    矩阵类, 用于书写矩阵的相关方法和计算
    """

    def __init__(self, matrix_body: list, is_matrix_body_cleaned: bool = False):
        self.body = matrix_body
        self.body_cleaned = copy.deepcopy(self.body)  # 深度拷贝矩阵
        self.y_len = len(self.body)  # 矩阵的列长度
        self.x_len = len(self.body[0])  # 矩阵的行长度
        self.type = "Matrix"

        # 完成self.body_cleaned 的操作
        if not is_matrix_body_cleaned:
            self._clean()
        # 完成矩阵字符串的清理
        self._clean_body()

    def __add__(self, other):  # 加
        if other.type == "Matrix":
            if self.x_len == other.x_len and self.y_len == other.y_len:
                matrix_body = copy.deepcopy(self.body)
                for yi in range(len(matrix_body)):
                    for xi in range(len(matrix_body[yi])):
                        matrix_body[yi][xi] = other.body_cleaned[yi][xi] + self.body_cleaned[yi][xi]
                return Matrix(
                    matrix_body=matrix_body,
                    is_matrix_body_cleaned=True
                )
            else:
                raise "无法相加"


    def __sub__(self, other):  # 减
        if other.type == "Matrix":
            return self.__add__(-other)

    def __neg__(self):  # 取负 用于直接创建 -对象
        negative_matrix = copy.deepcopy(self.body_cleaned)
        for yi in range(self.y_len):
            for xi in range(self.x_len):
                negative_matrix[yi][xi] = -negative_matrix[yi][xi]
        return Matrix(
            matrix_body=negative_matrix,
            is_matrix_body_cleaned=True,
        )

    def _clean_xi_old(self, xi, power_of_10: int = 0):  # 旧的方案, 会出现一些小数乘以10变成无限循环小数, 所以废弃
        """
        对矩阵元素分数化
        :param xi: 初始值
        :param power_of_10: 应该除以的10的倍数
        :return: 一个分数
        """
        power_of_10 = power_of_10
        # 如果该位置的数为整数, 则将其替换为分母为1的分数
        # 如果不为整数, 则乘不断递归乘10, 直到为整数, 再除以一定数量的10的次方
        if (xi * (10 ** power_of_10)) % 1 == 0:
            return RegularFraction(
                numerator=int(xi),
                denominator=(10 ** power_of_10)
            )
        else:
            return self._clean_xi_old(xi * 10, power_of_10=power_of_10 + 1)

    def _clean_xi(self, xi):
        """
        对矩阵元素分数化
        :param xi: 初始值
        power_of_10: 应该除以的10的倍数
        :return: 一个分数
        """
        # 通过使用小数的字符串拆分为两部分, 完成拼接成为整数, 最后除以合适的10的倍数
        xi = str(xi)
        xi_list = xi.split(".")
        xi_all = ""
        for x_i in range(len(xi_list)):
            xi_all += xi_list[x_i]
        xi_all = int(xi_all)
        power_of_10 = 0
        if len(xi_list) == 2:
            power_of_10 = len(xi_list[-1])
        return RegularFraction(
            numerator=xi_all,
            denominator=10 ** power_of_10
        )

    def _clean(self):
        """
        完成矩阵元素全部分数化
        :return: 一个全部为分数的矩阵
        """
        for yi in range(len(self.body_cleaned)):
            for xi in range(len(self.body_cleaned[yi])):
                # 对矩阵元素分数化
                self.body_cleaned[yi][xi] = self._clean_xi(self.body_cleaned[yi][xi])

    def __str__(self):
        # 完成矩阵的显示
        return self.body_cleaned_str

    def _clean_body(self):
        # 完成矩阵的清理
        self.body_cleaned_str = ""  # 矩阵的字符串, 用以返回
        for yi in self.body_cleaned:
            yi_str = ""
            for xi in yi:
                yi_str += f"{str(xi)},"
            yi_str = f"[{yi_str}]\n"
            self.body_cleaned_str += yi_str  # 未清理
        self.body_cleaned_str = self._clean_body_str()  # 清理后

    def _clean_body_str(self) -> str:
        """
        用以将矩阵的字符串输出更加标准化
        :return: clean_res 返回一个清理好的字符串
        """
        body_yi_str_list = self.body_cleaned_str.split("\n")[:-1]  # 所有yi
        body_xi_str_list = []  # 所有xi
        for yi_i in range(len(body_yi_str_list)):
            body_xi_str_lst = body_yi_str_list[yi_i].split(",")
            body_xi_str_list.append(body_xi_str_lst)
        # 将xi以,对其
        body_xi_str_list_new = []  # 对其xi的列表
        for xi_after_zip in zip(*body_xi_str_list):
            body_xi_str_list_new.append([])
            xi_len_list = []
            for xi in xi_after_zip:
                xi_len_list.append(len(xi))
            xi_max_len = max(xi_len_list)  # 每一列元素长度
            for xi in xi_after_zip:
                if len(xi) < xi_max_len:
                    xi_res = xi + (" " * (xi_max_len - len(xi)))
                    body_xi_str_list_new[-1].append(xi_res)
                else:
                    xi_res = xi
                    body_xi_str_list_new[-1].append(xi_res)
        body_xi_str_list_new = list(zip(*body_xi_str_list_new))
        clean_res = ""
        for yi in body_xi_str_list_new:
            yi_str = ""
            for xi in yi:
                yi_str += f"{xi}, "
            clean_res += f"{yi_str}\n"
        return clean_res

    def minimalist_matrix_by_row(self, row_index_list=None):
        """
        行最简化矩阵
        :return: 一个新的矩阵类
        """
        minimalist_matrix_body = copy.deepcopy(self.body_cleaned)
        if row_index_list is None:
            # 初始化row_index_list
            row_index_list = list(range(min(self.x_len, self.y_len)))

        flg_list = []  # 用于存储第几列全是0
        for row_index in row_index_list:
            is_not_all_0 = False
            for y_i in range(len(minimalist_matrix_body)):
                if minimalist_matrix_body[y_i][row_index].numerator != 0:
                    is_not_all_0 = True
            flg_list.append(is_not_all_0)

        is_ok = True
        for flg in flg_list:
            if not flg:
                is_ok = False
        if not is_ok:
            raise "无法完成对应行的最简化"

        for row_index, y_i in zip(row_index_list, range(min(self.x_len, self.y_len))):
            if minimalist_matrix_body[y_i][row_index].numerator == 0:
                minimalist_matrix_body = self._make_sure_row_not_0(minimalist_matrix_body, row_index, y_i)

            minimalist_matrix_body[y_i] = [x_i / minimalist_matrix_body[y_i][row_index] for x_i in
                                           minimalist_matrix_body[y_i]]
            minimalist_matrix_body = self._make_other_row_0(minimalist_matrix_body, row_index, y_i)

            # # 此处写列转换
            # minimalist_matrix_body = self._make_other_line_0(minimalist_matrix_body, row_index, y_i)

        return Matrix(
            matrix_body=minimalist_matrix_body,
            is_matrix_body_cleaned=True,
        )

    def _make_sure_row_not_0(self, minimalist_matrix_body, row_index, y_i) -> list:
        for y_i_i in range(self.y_len):
            if minimalist_matrix_body[y_i_i][row_index].numerator != 0:
                minimalist_matrix_body[y_i] = [x_i + x_i_i for x_i, x_i_i in
                                               zip(minimalist_matrix_body[y_i], minimalist_matrix_body[y_i_i])]
                break
        return minimalist_matrix_body

    def _make_other_row_0(self, minimalist_matrix_body, row_index, y_i) -> list:
        for y_i_i in range(self.y_len):
            if y_i != y_i_i:
                if minimalist_matrix_body[y_i_i][row_index].numerator != 0:
                    minimalist_matrix_body[y_i_i] = [x_i_i - (x_i * minimalist_matrix_body[y_i_i][row_index]) for
                                                     x_i, x_i_i in
                                                     zip(minimalist_matrix_body[y_i], minimalist_matrix_body[y_i_i])]
        return minimalist_matrix_body

    # def _make_other_line_0(self, minimalist_matrix_body, row_index, y_i) -> list:
    #     minimalist_matrix_body = list(zip(*minimalist_matrix_body))
    #     for y_i_i in range(self.y_len):
    #         if y_i != y_i_i:
    #             if minimalist_matrix_body[y_i_i][row_index].numerator != 0:
    #                 minimalist_matrix_body[y_i_i] = [x_i_i - (x_i * x_i_i) for x_i, x_i_i in
    #                                                  zip(minimalist_matrix_body[y_i], minimalist_matrix_body[y_i_i])]
    #     minimalist_matrix_body = list(zip(*minimalist_matrix_body))
    #     return minimalist_matrix_body
    def matrix_transpose(self):
        """矩阵转置"""
        return Matrix(
            matrix_body=list(zip(*copy.deepcopy(self.body_cleaned))),
            is_matrix_body_cleaned=True,
        )


    def augmented_matrix(self, matrix_body):
        """添加增广矩阵"""
        augmented_matrix = copy.deepcopy(self.body_cleaned)
        if self.y_len != matrix_body.y_len:
            raise "不能做增广"
        for i in range(self.y_len):
            for j in range(matrix_body.x_len):
                augmented_matrix[i].append(matrix_body.body_cleaned[i][j])
        return Matrix(matrix_body=augmented_matrix, is_matrix_body_cleaned=True)

    def matrix_inversion(self):
        """逆矩阵"""
        identity_matrix = self.minimalist_matrix_by_row()
        augmented_matrix = self.augmented_matrix(matrix_body=identity_matrix)
        inversion_matrix = augmented_matrix.minimalist_matrix_by_row()
        inversion_matrix_body_list = [inversion_matrix.body_cleaned[i][self.y_len:] for i in range(self.y_len)]
        return Matrix(matrix_body=inversion_matrix_body_list, is_matrix_body_cleaned=True)

    def rotate_90(self):
        other_rotate_90 = []
        for xi in range(self.x_len):
            other_rotate_90.append([])
        for yi in range(self.y_len):
            for xi in range(self.x_len):
                other_rotate_90[xi].append(self.body_cleaned[yi][xi])
        return Matrix(
            matrix_body=copy.deepcopy(other_rotate_90),
            is_matrix_body_cleaned=True
        )

    def __mul__(self, other):
        if other.type == "Matrix":
            matrix_body_copy = []
            other_rotate_90 = other.rotate_90()
            for yi in range(self.y_len):
                matrix_body_copy.append([])
                for i in range(other_rotate_90.y_len):
                    matrix_body_copy[yi].append('')

            if self.x_len == other_rotate_90.x_len:
                from Unities.Fraction_class.RegularFraction_class import RegularFraction

                for x in range(len(matrix_body_copy)):
                    for y in range(len(matrix_body_copy[x])):
                        count = RegularFraction(0, 1)
                        for j in range( other_rotate_90.x_len):
                            count += self.body_cleaned[x][j] * other_rotate_90.body_cleaned[y][j]
                        matrix_body_copy[x][y] = count

            return Matrix(
                matrix_body=copy.deepcopy(matrix_body_copy),
                is_matrix_body_cleaned=True
            )








if __name__ == '__main__':
    # m_2 = Matrix([
    #     [1, 3, 5, 2.5, 4.004],
    #     [2, 3, 5.04, 6, 8],
    #     [1.0000001, 2, 3, 4, 5]
    # ])

    m_1 = Matrix([
        [1, 0, 0, ],
        [0, 1, 0, ],
        [0, 0, 1, ]
    ])
    m_2 = m_1.matrix_inversion()
    print(m_1)
    print(m_2)

    # m_1 = Matrix([
    #     [0, 3, 5, 2.5, 4.004],
    #     [1, 3, 5.04, 6, 8],
    #     [0, 2, 3, 4, 5]
    # ])
    # print(m_1)

    # print(m_2)
    # print(m_2 + m_1)
    # m_1_minimalist = m_1.minimalist_matrix_by_row(row_index_list=[0, 2, 1])
    # print(m_1_minimalist)
    # print(m_1)
    # m_1_transpose = m_1.matrix_transpose()
    # print(m_1_transpose)
    # m_1_negative = -m_1
    # print(m_1_negative)

    # for i in m.body_cleaned:
    #     for j in i:
    #         print(j)
    # print(4.004 * 1000)
    x_1 = Matrix([[1, 2],
                  [3, 4]])
    x_2 = Matrix([[1, 2, 5],
                  [3, 8, 7]])
    print(x_1 * x_2)
