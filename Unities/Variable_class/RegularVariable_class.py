from Unities.Variable_class.VariableABC_class import VariableABC


class RegularVariable(VariableABC):

    def __init__(self, char: str):
        super(RegularVariable, self).__init__(char=char)
        self.type = "RegularVariable"

    def __str__(self):
        return f"{self.char}"

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass


if __name__ == '__main__':
    rv_x = RegularVariable("x")
    rv_y = RegularVariable("y")
    print(rv_x)
