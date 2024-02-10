from abc import ABC, abstractmethod


class FractionABC(object):
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
        self.symbol = 0
        if self.numerator <= 0:
            self.symbol += 1
            self.numerator = -self.numerator
        if self.denominator <= 0:
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



    def __str__(self):
        return f"({self.numerator}/{self.denominator})"


class RegularFraction(FractionABC):
    """
    正则分数类, 标准的分数, 正常情况
    """


if __name__ == '__main__':
    f = FractionABC(4, -2)
    print(f.int_value)