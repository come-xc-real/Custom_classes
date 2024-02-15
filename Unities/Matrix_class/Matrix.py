import copy
from Unities.Fraction_class.RegularFraction_class import RegularFraction

class Matrix:
    """
    矩阵类, 用于书写矩阵的相关方法和计算
    """
    def __init__(self, matrix_body: list):
        self.body = matrix_body
        self.body_cleaned = copy.deepcopy(self.body)     # 深度拷贝矩阵

        # 完成self.body_cleaned 的操作
        self._clean()

    def _clean_xi_old(self, xi, power_of_10=0):  # 旧的方案, 会出现一些小数乘以10变成无限循环小数, 所以废弃
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
            return self._clean_xi_old(xi*10, power_of_10=power_of_10+1)

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


if __name__ == '__main__':
    m = Matrix([[1, 3, 5, 2.5, 4.004]])
    for i in m.body_cleaned:
        for j in i:
            print(j)
    # print(4.004 * 1000)