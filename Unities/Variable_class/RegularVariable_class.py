from Unities.Variable_class.VariableABC_class import VariableABC


class RegularVariable(VariableABC):

    def __init__(self, char: str):
        super(RegularVariable, self).__init__(char=char)
        self.type = "RegularVariable"

    def __str__(self):
        return f"{self.char}"

    def __add__(self, other):
        return other.__add__(
            other=RegularVariable(char=self.char)
        )

    def __sub__(self, other):
        return other.__sub__(
            other=RegularVariable(char=self.char)
        )

    def __mul__(self, other):
        return other.__mul__(
            other=RegularVariable(char=self.char)
        )

    def __truediv__(self, other):
        from Unities.Variable_class.VarableFraction_class import VariableFraction
        return VariableFraction(
            numerator=-1,
            denominator=1,
            numerator_variable_list=[RegularVariable(char=self.char)],
            denominator_variable_list=[RegularVariable(char="")]
        )

    def __neg__(self):  # 取负 用于直接创建 -对象
        from Unities.Variable_class.VarableFraction_class import VariableFraction
        return VariableFraction(
            numerator=-1,
            denominator=1,
            numerator_variable_list=[RegularVariable(f"{self.char}")],
            denominator_variable_list=[RegularVariable("")]
        )


if __name__ == '__main__':
    rv_x = RegularVariable("x")
    rv_y = RegularVariable("y")
    print(rv_x)
