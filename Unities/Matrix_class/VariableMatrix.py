from Unities.Matrix_class.Matrix import Matrix


class VariableMatrix(Matrix):
    def __init__(self, matrix_body: list, is_matrix_body_cleaned: bool = False):
        super().__init__(matrix_body, is_matrix_body_cleaned=is_matrix_body_cleaned)


if __name__ == '__main__':
    from Unities.Variable_class.VarableFraction_class import VariableFraction
    from Unities.Variable_class.RegularVariable_class import RegularVariable

    x = RegularVariable("x")
    y = RegularVariable("y")
    a_1 = VariableFraction(1, 1, [x], [y])
    print(a_1)
    vm = VariableMatrix([
        [a_1, a_1, a_1, a_1],
        [a_1, a_1, a_1, a_1]
    ], is_matrix_body_cleaned=True)
    print(vm - vm)
    print(vm.matrix_transpose())
