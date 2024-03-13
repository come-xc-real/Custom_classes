import copy


class Polynomial:
    """多项式类"""

    def __init__(self, polynomial_body_list: list):
        self.polynomial_body_list = polynomial_body_list
        self.clean()
        self.str = self._get_str()
        self.type = "Polynomial"

    def clean(self):
        self._clean_polynomial_body_all_variable_fraction()
        self._clean_variable_in_variable_fraction()
        self._clean_polynomial()
        self._clean_all_numerator_0_polynomial_body()

    def _clean_all_numerator_0_polynomial_body(self):
        flg = False
        for i in range(len(self.polynomial_body_list)):
            if self.polynomial_body_list[i].numerator == 0:
                self.polynomial_body_list.remove(self.polynomial_body_list[i])
                flg = True
                break
        if flg:
            return self._clean_all_numerator_0_polynomial_body()

    def _clean_polynomial_body_all_variable_fraction(self):
        for i in range(len(self.polynomial_body_list)):
            if self.polynomial_body_list[i].type == "RegularFraction":
                from Unities.Variable_class.VarableFraction_class import VariableFraction
                from Unities.Variable_class.RegularVariable_class import RegularVariable
                self.polynomial_body_list[i] = VariableFraction(
                    numerator=self.polynomial_body_list[i].numerator,
                    denominator=self.polynomial_body_list[i].denominator,
                    numerator_variable_list=[RegularVariable("")],
                    denominator_variable_list=[RegularVariable("")]
                )
            elif self.polynomial_body_list[i].type == "RegularVariable":
                from Unities.Variable_class.VarableFraction_class import VariableFraction
                from Unities.Variable_class.RegularVariable_class import RegularVariable
                self.polynomial_body_list[i] = VariableFraction(
                    numerator=1,
                    denominator=1,
                    numerator_variable_list=[self.polynomial_body_list[i]],
                    denominator_variable_list=[RegularVariable("")]
                )

    def _clean_variable_in_variable_fraction(self):
        polynomial_body_list_new = []
        for i in range(len(self.polynomial_body_list)):
            if self.polynomial_body_list[i].type == "VariableFraction":
                numerator_variable_list_new = []
                variable_fraction_i = self.polynomial_body_list[i]
                for j in range(len(variable_fraction_i.numerator_variable_list)):
                    if variable_fraction_i.numerator_variable_list[j].char != "":
                        numerator_variable_list_new.append(variable_fraction_i.numerator_variable_list[j])
                if len(numerator_variable_list_new) == 0:
                    from Unities.Variable_class.RegularVariable_class import RegularVariable
                    numerator_variable_list_new.append(RegularVariable(char=""))
                denominator_variable_list_new = []
                for j in range(len(variable_fraction_i.denominator_variable_list)):
                    if variable_fraction_i.denominator_variable_list[j].char != "":
                        denominator_variable_list_new.append(variable_fraction_i.denominator_variable_list[j])
                if len(denominator_variable_list_new) == 0:
                    from Unities.Variable_class.RegularVariable_class import RegularVariable
                    denominator_variable_list_new.append(RegularVariable(char=""))
                from Unities.Variable_class.VarableFraction_class import VariableFraction
                polynomial_body_list_new.append(
                    VariableFraction(
                        numerator=variable_fraction_i.numerator,
                        denominator=variable_fraction_i.denominator,
                        numerator_variable_list=numerator_variable_list_new,
                        denominator_variable_list=denominator_variable_list_new
                    )
                )
            else:
                polynomial_body_list_new.append(self.polynomial_body_list[i])
        self.polynomial_body_list = polynomial_body_list_new

    def _clean_polynomial(self):
        flg = False
        for i in range(len(self.polynomial_body_list)):
            for j in range(len(self.polynomial_body_list)):
                if i != j and self.polynomial_body_list[i].type == "VariableFraction" \
                        and self.polynomial_body_list[j].type == "VariableFraction":
                    if len(self.polynomial_body_list[i].numerator_variable_list) \
                            == len(self.polynomial_body_list[j].numerator_variable_list) and \
                            len(self.polynomial_body_list[i].denominator_variable_list) \
                            == len(self.polynomial_body_list[i].denominator_variable_list):
                        list_0_n = [body_i.char for body_i in self.polynomial_body_list[i].numerator_variable_list]
                        list_0_d = [body_i.char for body_i in self.polynomial_body_list[i].denominator_variable_list]
                        list_1_n = [body_j.char for body_j in self.polynomial_body_list[j].numerator_variable_list]
                        list_1_d = [body_j.char for body_j in self.polynomial_body_list[j].denominator_variable_list]
                        if self._is_permutation(list_0_n, list_1_n) and self._is_permutation(list_0_d, list_1_d):
                            from Unities.Variable_class.VarableFraction_class import VariableFraction
                            from Unities.Fraction_class.RegularFraction_class import RegularFraction
                            self.polynomial_body_list[i] = VariableFraction(
                                numerator=(RegularFraction(
                                    numerator=self.polynomial_body_list[i].numerator,
                                    denominator=self.polynomial_body_list[i].denominator,
                                ) + RegularFraction(
                                    numerator=self.polynomial_body_list[j].numerator,
                                    denominator=self.polynomial_body_list[j].denominator,
                                )).numerator,
                                denominator=(RegularFraction(
                                    numerator=self.polynomial_body_list[i].numerator,
                                    denominator=self.polynomial_body_list[i].denominator,
                                ) + RegularFraction(
                                    numerator=self.polynomial_body_list[j].numerator,
                                    denominator=self.polynomial_body_list[j].denominator,
                                )).denominator,
                                numerator_variable_list=self.polynomial_body_list[i].numerator_variable_list,
                                denominator_variable_list=self.polynomial_body_list[i].denominator_variable_list
                            )
                            self.polynomial_body_list[j] = RegularFraction(0, 1)
                            flg = True
                            break
        if flg:
            self._clean_polynomial()

    def _is_permutation(self, list_0, list_1):
        list_0 = list_0.copy()
        list_1 = list_1.copy()
        flg = False
        if len(list_0) == 0 and len(list_1) == 0:
            return True
        if len(list_0) > 0:
            if list_0[-1] in list_1:
                list_1.remove(list_0[-1])
                list_0.remove(list_0[-1])
                flg = True
        if flg:
            return self._is_permutation(list_0, list_1)

        else:
            return False

    def _get_str(self):
        str_res = ""
        for monomial_i in self.polynomial_body_list:
            str_res += (" + " + str(monomial_i))
        return str_res

    def __str__(self):
        return f"({self.str})"

    def __add__(self, other):  # 加
        if other.type in ["RegularFraction", "RegularVariable", "VariableFraction"]:
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
        elif other.type == "PolynomialFraction":
            return other.__add__(
                other=Polynomial(
                    polynomial_body_list=self.polynomial_body_list
                )
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
        elif other.type in ["RegularFraction", "RegularVariable", "VariableFraction"]:
            from Unities.Variable_class.VarableFraction_class import VariableFraction
            return self.__mul__(
                other=Polynomial(
                    polynomial_body_list=[other]
                )
            )
        elif other.type == "PolynomialFraction":
            return other.__mul__(
                other=Polynomial(
                    polynomial_body_list=self.polynomial_body_list
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
            from Unities.Variable_class.PolynomialFraction_class import PolynomialFraction
            return PolynomialFraction(
                polynomial_numerator=Polynomial(
                    polynomial_body_list=self.polynomial_body_list
                ),
                polynomial_denominator=Polynomial(
                    polynomial_body_list=other.polynomial_body_list
                )
            )
        elif other.type == "PolynomialFraction":
            from Unities.Variable_class.PolynomialFraction_class import PolynomialFraction
            from Unities.Fraction_class.RegularFraction_class import RegularFraction
            return self.__mul__(
                other=(PolynomialFraction(
                    polynomial_numerator=Polynomial(
                        polynomial_body_list=[RegularFraction(1, 1)]
                    ),
                    polynomial_denominator=Polynomial(
                        polynomial_body_list=[RegularFraction(1, 1)]
                    )
                ) / other)
            )

    def __neg__(self):  # 取负 用于直接创建 -对象
        polynomial_body_list_new = copy.deepcopy(self.polynomial_body_list)
        for i in range(len(polynomial_body_list_new)):
            polynomial_body_list_new[i] = -polynomial_body_list_new[i]
        return Polynomial(
            polynomial_body_list=polynomial_body_list_new
        )


if __name__ == '__main__':
    from Unities.Variable_class.RegularVariable_class import RegularVariable
    from Unities.Variable_class.VarableFraction_class import VariableFraction

    x = RegularVariable("x")
    y = RegularVariable("y")
    n = RegularVariable("")
    vf0 = VariableFraction(1, 3, [x, x], [y, y])
    vf1 = VariableFraction(1, 2, [x, x], [y, y])
    p = vf1 + vf0 + x + y
    p_1 = vf1 + vf0 + x + y
    print(p + p_1)
