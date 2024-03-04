
class Polynomial:
    """多项式类"""
    def __init__(self, polynomial_body_list: list):
        self.polynomial_body_list = polynomial_body_list
        self.str = self._get_str()

    def _get_str(self):
        str_res = ""
        for monomial_i in self.polynomial_body_list:
            str_res += (" + " + str(monomial_i))
        return str_res

    def __str__(self):
        return f"({self.str})"


if __name__ == '__main__':
    p = Polynomial([1, 2, 3])
    print(p)
