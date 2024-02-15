"""
参数类的定义
"""
from abc import ABC, abstractmethod


class VariableABC(ABC):
    """
    抽象变量类, 数学中的变量, 类似于x, y
    """

    def __init__(self, char: str):
        """
        抽象变量类初始化
        :param char: 变量字符形式, 必须为字符, 限制为字母, 后续开发子类限制字符模式
        """
        self.char = char

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):  # 加
        pass

    @abstractmethod
    def __sub__(self, other):  # 减
        pass

    @abstractmethod
    def __mul__(self, other):  # 乘
        pass

    @abstractmethod
    def __truediv__(self, other):  # 除
        pass

    @abstractmethod
    def __neg__(self):  # 取负 用于直接创建 -对象
        pass


if __name__ == '__main__':
    pass
