from Unities.Variable_class.Polynomial_class import Polynomial


class PolynomialFraction:
    def __init__(self, polynomial_numerator: Polynomial, polynomial_denominator: Polynomial):
        self.polynomial_numerator = polynomial_numerator
        self.polynomial_denominator = polynomial_denominator
        self.type = "PolynomialFraction"
        self._clean()

    def _clean(self):
        self._clean_all_variable_in_denominator()

    def _clean_all_variable_in_denominator(self):
        """将多项式分数类的上下多项式中参数分数类的分母中的参数约掉"""
        flg = False
        from Unities.Variable_class.RegularVariable_class import RegularVariable
        variable_list = []
        for ni in range(len(self.polynomial_numerator.polynomial_body_list)):
            char_i = self.polynomial_numerator.polynomial_body_list[ni].denominator_variable_list[0].char
            if char_i != "":
                self.polynomial_numerator = self.polynomial_numerator * RegularVariable(f"{char_i}")
                self.polynomial_denominator = self.polynomial_denominator * RegularVariable(f"{char_i}")
                flg = True
                break
        if flg:
            return self._clean_all_variable_in_denominator()

    def __add__(self, other):
        if other.type == "PolynomialFraction":
            new_polynomial_numerator = (
                    (self.polynomial_numerator * other.polynomial_denominator) +
                    (self.polynomial_denominator * other.polynomial_numerator)
            )
            return PolynomialFraction(
                polynomial_numerator=new_polynomial_numerator,
                polynomial_denominator=self.polynomial_denominator * other.polynomial_denominator
            )
        elif other.type in ["RegularVariable", "VariableFraction", "RegularFraction", "Polynomial"]:
            from Unities.Fraction_class.RegularFraction_class import RegularFraction
            return self.__add__(PolynomialFraction(
                polynomial_numerator=Polynomial(
                    polynomial_body_list=[other]
                ),
                polynomial_denominator=Polynomial(
                    polynomial_body_list=[RegularFraction(1, 1)]
                )
            ))

    def __sub__(self, other):  # 减
        # 加负other
        return self.__add__(-other)

    def __neg__(self):  # 取负 用于直接创建 -对象
        return PolynomialFraction(
            polynomial_numerator=-self.polynomial_numerator,
            polynomial_denominator=self.polynomial_denominator
        )

    def __mul__(self, other):
        if other.type == "PolynomialFraction":
            return PolynomialFraction(
                polynomial_numerator=self.polynomial_numerator * other.polynomial_numerator,
                polynomial_denominator=self.polynomial_denominator * other.polynomial_denominator
            )
        elif other.type in ["RegularVariable", "VariableFraction", "RegularFraction", "Polynomial"]:
            from Unities.Fraction_class.RegularFraction_class import RegularFraction
            return self.__mul__(PolynomialFraction(
                polynomial_numerator=Polynomial(
                    polynomial_body_list=[other]
                ),
                polynomial_denominator=Polynomial(
                    polynomial_body_list=[RegularFraction(1, 1)]
                )
            ))

    def __truediv__(self, other):  # 除
        # 乘 1/other
        if other.type == "PolynomialFraction":
            return self.__mul__(
                other=PolynomialFraction(
                    polynomial_numerator=other.polynomial_denominator,
                    polynomial_denominator=other.polynomial_numerator
                )
            )
        elif other.type in ["RegularVariable", "VariableFraction", "RegularFraction", "Polynomial"]:
            from Unities.Fraction_class.RegularFraction_class import RegularFraction
            return self.__mul__(PolynomialFraction(
                polynomial_numerator=Polynomial(
                    polynomial_body_list=[RegularFraction(1, 1)]
                ),
                polynomial_denominator=Polynomial(
                    polynomial_body_list=[other]
                )
            ))

    def __str__(self):
        return f"{str(self.polynomial_numerator)}/{str(self.polynomial_denominator)}"


if __name__ == '__main__':
    from Unities.Variable_class.RegularVariable_class import RegularVariable
    from Unities.Variable_class.VarableFraction_class import VariableFraction

    x = RegularVariable("x")
    y = RegularVariable("y")
    n = RegularVariable("")
    vf0 = VariableFraction(1, 3, [x, x], [y, y])
    vf1 = VariableFraction(1, 2, [x, x], [y, y])
    p = vf1 + vf0 + x + y
    pf = PolynomialFraction(p, p)
    pf_1 = PolynomialFraction(p, p)
    # pf_2 = pf + pf_1
    # print(pf_2)
    print(pf)
    # print(pf + x)
    print(vf1 / pf)
