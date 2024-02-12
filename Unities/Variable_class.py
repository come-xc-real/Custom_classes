"""
参数类的定义
"""

class VariableABC(object):
    """
    抽象变量类, 数学中的变量, 类似于x, y
    """
    def __init__(self, char: str):
        """
        抽象变量类初始化
        :param char: 变量字符形式, 必须为字符, 限制为字母, 后续开发子类限制字符模式
        """
        self.char = char

    def __str__(self):
        return f"({self.char})"




if __name__ == '__main__':
    v = VariableABC("x")
    print(v)