from Unities.Fraction_class.FractionABC_class import FractionABC
from Unities.Variable_class.Polynomial_class import Polynomial
from Unities.Variable_class.RegularVariable_class import RegularVariable


class RegularFraction(FractionABC):
    """
    正则分数类, 标准的分数, 正常情况
    """

    def __init__(self, numerator: int, denominator: int):
        super().__init__(numerator, denominator)
        self.type = "RegularFraction"

    def __str__(self):
        return f"({self.numerator}/{self.denominator})"

    def __add__(self, other):  # 加
        if other.type == "RegularFraction":
            # 如果是和一个简单分数相加, 返回另一个分数
            return RegularFraction(
                numerator=(
                        + (self.numerator * other.denominator)
                        + (self.denominator * other.numerator)
                ),
                denominator=(self.denominator * other.denominator)
            )
        # 由于无法完成int + Fraction 所以此处有一定问题
        elif type(other) == int:
            # 如果和整数相加, 将整数转换成底数为1的分数
            return self.__add__(other=RegularFraction(other, 1))

        elif other.type == "RegularVariable":
            # 返回多项式
            return Polynomial(
                polynomial_body_list=[
                    RegularFraction(numerator=self.numerator, denominator=self.denominator),
                    other
                ]
            )

    def __sub__(self, other):  # 减
        # 加负other
        return self.__add__(-other)

    def __mul__(self, other):  # 乘
        if other.type == "RegularFraction":
            # 如果是和一个简单分数相乘, 返回另一个分数
            return RegularFraction(
                numerator=(self.numerator * other.numerator),
                denominator=(self.denominator * other.denominator)
            )
        elif other.type == "RegularVariable":
            from Unities.Variable_class.VarableFraction_class import VariableFraction
            return VariableFraction(
                numerator=self.numerator,
                denominator=self.denominator,
                numerator_variable_list=[other],
                denominator_variable_list=[RegularVariable("")]
            )

    def __truediv__(self, other):  # 除
        # 乘 1/other
        if other.type == "RegularFraction":
            return self.__mul__(
                RegularFraction(
                    numerator=other.denominator,
                    denominator=other.numerator
                )
            )
        elif other.type == "RegularVariable":
            from Unities.Variable_class.VarableFraction_class import VariableFraction
            return VariableFraction(
                numerator=self.numerator,
                denominator=self.denominator,
                numerator_variable_list=[RegularVariable("")],
                denominator_variable_list=[other]
            )

    def __neg__(self):  # 取负 用于直接创建 -对象
        # 创建一个分子为相反数的分数类
        return RegularFraction(
            numerator=-self.numerator,
            denominator=self.denominator
        )


if __name__ == '__main__':
    rf_1 = RegularFraction(7, 3)
    rf_2 = RegularFraction(7, 3)
    # print(rf_1 / rf_2)
    x = RegularVariable("x")
    print(rf_1 / x)
