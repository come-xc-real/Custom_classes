import copy


class Polynomial:
    """多项式类"""

    def __init__(self, polynomial_body_list: list):
        self.polynomial_body_list = polynomial_body_list
        self.str = self._get_str()
        self.type = "Polynomial"

    def _get_str(self):
        str_res = ""
        for monomial_i in self.polynomial_body_list:
            str_res += (" + " + str(monomial_i))
        return str_res

    def __str__(self):
        return f"({self.str})"

    def __add__(self, other):  # 加
        if other.type == "RegularFraction" or "RegularVariable" or "VariableFraction":
            polynomial_body_list_new = copy.deepcopy(self.polynomial_body_list)
            polynomial_body_list_new.append(other)
            return Polynomial(
                polynomial_body_list=polynomial_body_list_new
            )

        elif other.type == "Polynomial":
            polynomial_body_list_new = copy.deepcopy(self.polynomial_body_list)
            for polynomial_body_i in other.polynomial_body_list:
                polynomial_body_list_new.append(polynomial_body_i)
            return Polynomial(
                polynomial_body_list=polynomial_body_list_new
            )

    def __sub__(self, other):  # 减
        # 加负other
        return self.__add__(-other)

    def __mul__(self, other):  # 乘
        if other.type == "Polynomial":
            polynomial_body_list_new = []
            polynomial_body_list = copy.deepcopy(self.polynomial_body_list)
            for polynomial_body_i in polynomial_body_list:
                for polynomial_body_j in other.polynomial_body_list:
                    polynomial_body_list_new.append(polynomial_body_i * polynomial_body_j)
            return Polynomial(
                polynomial_body_list=polynomial_body_list_new
            )
        elif other.type == "RegularFraction" or "RegularVariable" or "VariableFraction":
            from Unities.Variable_class.VarableFraction_class import VariableFraction
            return self.__mul__(
                other=Polynomial(
                    polynomial_body_list=[other]
                )
            )

    def __truediv__(self, other):  # 除
        # 乘 1/other
        if other.type == "RegularFraction":
            from Unities.Fraction_class.RegularFraction_class import RegularFraction
            return self.__mul__(
                RegularFraction(
                    numerator=other.denominator,
                    denominator=other.numerator
                )
            )
        elif other.type == "RegularVariable":
            from Unities.Variable_class.VarableFraction_class import VariableFraction
            from Unities.Variable_class.RegularVariable_class import RegularVariable
            return self.__mul__(
                other=VariableFraction(
                    numerator=1,
                    denominator=1,
                    numerator_variable_list=[RegularVariable("")],
                    denominator_variable_list=[other]
                )
            )
        elif other.type == "VariableFraction":
            from Unities.Variable_class.VarableFraction_class import VariableFraction
            return self.__mul__(
                VariableFraction(
                    numerator=other.denominator,
                    denominator=other.numerator,
                    numerator_variable_list=copy.deepcopy(other.denominator_variable_list),
                    denominator_variable_list=copy.deepcopy(other.numerator_variable_list)
                )
            )
        elif other.type == "Polynomial":
            pass


    def __neg__(self):  # 取负 用于直接创建 -对象
        polynomial_body_list_new = copy.deepcopy(self.polynomial_body_list)
        for i in range(len(polynomial_body_list_new)):
            polynomial_body_list_new[i] = -polynomial_body_list_new[i]
        return Polynomial(
                polynomial_body_list=polynomial_body_list_new
            )


if __name__ == '__main__':
    p = Polynomial([1, 2, 3])
    p_1 = Polynomial([2, 3, 5])
    print(p * p_1)
