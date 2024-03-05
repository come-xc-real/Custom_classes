import copy

from Unities.Fraction_class.RegularFraction_class import RegularFraction



class VariableFraction(RegularFraction):
    """含参分数类"""

    def __init__(self, numerator: int, denominator: int,
                 numerator_variable_list: list,
                 denominator_variable_list: list):
        super().__init__(numerator, denominator)
        self.numerator_variable_list = numerator_variable_list

        self.denominator_variable_list = denominator_variable_list
        self.type = "VariableFraction"

    def __str__(self):
        numerator_variable_str = ""
        for numerator_variable in self.numerator_variable_list:
            numerator_variable_str += str(numerator_variable)
        denominator_variable_str = ""
        for denominator_variable in self.denominator_variable_list:
            denominator_variable_str += str(denominator_variable)
        return f"({self.numerator}{numerator_variable_str}/{self.denominator}{denominator_variable_str})"

    def __add__(self, other):  # 加
        if other.type == "RegularVariable" or "VariableFraction" or "RegularFraction":
            from Unities.Variable_class.Polynomial_class import Polynomial
            # 返回多项式
            return Polynomial(
                polynomial_body_list=[
                    VariableFraction(
                        numerator=self.numerator,
                        denominator=self.denominator,
                        numerator_variable_list=copy.deepcopy(self.numerator_variable_list),
                        denominator_variable_list=copy.deepcopy(self.denominator_variable_list)
                    ),
                    other
                ]
            )
        elif other.type == "Polynomial":
            from Unities.Variable_class.Polynomial_class import Polynomial
            return other.__add__(
                other=VariableFraction(
                    numerator=self.numerator,
                    denominator=self.denominator,
                    numerator_variable_list=copy.deepcopy(self.numerator_variable_list),
                    denominator_variable_list=copy.deepcopy(self.denominator_variable_list)
                )
            )

    def __sub__(self, other):  # 减
        # 加负other
        return self.__add__(-other)

    def __mul__(self, other):  # 乘
        if other.type == "RegularFraction":
            # 如果是和一个简单分数相乘, 返回另一个带参分数
            return VariableFraction(
                numerator=self.numerator * other.numerator,
                denominator=self.denominator * other.denominator,
                numerator_variable_list=copy.deepcopy(self.numerator_variable_list),
                denominator_variable_list=copy.deepcopy(self.denominator_variable_list)
            )
        elif other.type == "RegularVariable":
            numerator_variable_list_new = list(copy.deepcopy(self.numerator_variable_list))
            numerator_variable_list_new.append(copy.deepcopy(other))
            return VariableFraction(
                numerator=self.numerator,
                denominator=self.denominator,
                numerator_variable_list=numerator_variable_list_new,
                denominator_variable_list=copy.deepcopy(self.denominator_variable_list)
            )
        elif other.type == "VariableFraction":
            numerator_variable_list_new = list(copy.deepcopy(self.numerator_variable_list))
            for numerator_variable in other.numerator_variable_list:
                numerator_variable_list_new.append(numerator_variable)
            denominator_variable_list_new = copy.deepcopy(self.denominator_variable_list)
            for denominator_variable in other.denominator_variable_list:
                denominator_variable_list_new.append(denominator_variable)
            return VariableFraction(
                numerator=self.numerator * other.numerator,
                denominator=self.denominator * other.denominator,
                numerator_variable_list=numerator_variable_list_new,
                denominator_variable_list=denominator_variable_list_new
            )
        elif other.type == "Polynomial":
            from Unities.Variable_class.Polynomial_class import Polynomial
            return other.__mul__(
                other=Polynomial(
                    polynomial_body_list=[
                        VariableFraction(
                            numerator=self.numerator,
                            denominator=self.denominator,
                            numerator_variable_list=copy.deepcopy(self.numerator_variable_list),
                            denominator_variable_list=copy.deepcopy(self.denominator_variable_list)
                        )
                    ]
                )
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
            denominator_variable_list_new = copy.deepcopy(self.denominator_variable_list)
            denominator_variable_list_new.append(other)
            return VariableFraction(
                numerator=self.numerator,
                denominator=self.denominator,
                numerator_variable_list=copy.deepcopy(self.numerator_variable_list),
                denominator_variable_list=denominator_variable_list_new
            )
        elif other.type == "VariableFraction":
            return self.__mul__(
                VariableFraction(
                    numerator=self.denominator,
                    denominator=self.numerator,
                    numerator_variable_list=copy.deepcopy(self.denominator_variable_list),
                    denominator_variable_list=copy.deepcopy(self.numerator_variable_list)
                )
            )
        elif other.type == "Polynomial":
            pass

    def __neg__(self):  # 取负 用于直接创建 -对象
        # 创建一个分子为相反数的分数类
        return VariableFraction(
            numerator=-self.numerator,
            denominator=self.denominator,
            numerator_variable_list=copy.deepcopy(self.numerator_variable_list),
            denominator_variable_list=copy.deepcopy(self.denominator_variable_list)
        )


if __name__ == '__main__':
    from Unities.Variable_class.RegularVariable_class import RegularVariable
    x = RegularVariable("x")
    y = RegularVariable("y")
    vf = VariableFraction(1, 3, [x, y], [y])
    vf_1 = VariableFraction(1, 3, [x, y], [y])
    print(vf)
    print(-vf)
    print(-vf_1)
    # print(vf * vf_1)
