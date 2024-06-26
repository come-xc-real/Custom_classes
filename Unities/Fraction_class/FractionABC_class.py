"""
分数类的定义
"""

from abc import ABC, abstractmethod


class FractionABC(ABC):
    """
    抽象分数类, 用于无法判断类型时调用
    """
    def __init__(self, numerator: int, denominator: int):
        """
        抽象分数类初始化
        :param numerator: 分子
        :param denominator: 分母
        self.int_value: 整数值, 非整数为None
        self.value: 值, 有必要时参加计算
        """
        self.numerator = numerator
        self.denominator = denominator

        self.int_value = None
        self._verify_legitimacy()
        self._format()
        self.type = "Fraction"  # 分数类

        self.value = self.numerator / self.denominator

    def _verify_legitimacy(self):
        """
        验证合法性
        :return: None
        """
        if self.denominator == 0:
            raise "分母不能为0"



    def _format(self):
        """
        格式化
        :return: 返回一个整数类或者更改分子分母
        """

        # 符号统一为分子符号 part:1
        self.symbol = 0  # 此属性是一个整数类型, 用以确定整个分数的正负, 为偶数时为正
        if self.numerator < 0:
            self.symbol += 1
            self.numerator = -self.numerator
        if self.denominator < 0:
            self.symbol += 1
            self.denominator = -self.denominator

        # 同时除以公因数
        if self.numerator > 1:
            self._divide_common_factor()

        # 符号统一为分子符号 part:2
        if self.symbol % 2 != 0:
            self.numerator = -self.numerator

        # 如果可以是一个整数, 将 self.int_value 赋值
        if self.denominator == 1:
            self.int_value = self.numerator

        # 如果分子为0, 将分母变成1, 方便观看
        if self.numerator == 0:
            self.denominator = 1

    def _divide_common_factor(self):
        """
        同时除以公因数
        :return: flg 表示是否存在公因数
        """
        flg = False
        for i in range(2, self.numerator + 1):
            if self.numerator % i == 0:
                if self.denominator % i == 0:
                    self.numerator = int(self.numerator / i)
                    self.denominator = int(self.denominator / i)
                    flg = True
                    break
        if flg:
            return self._divide_common_factor()

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
    f = FractionABC(4, -2)
    print(f.int_value)