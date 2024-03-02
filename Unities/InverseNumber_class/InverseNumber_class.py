import itertools


class InverseNumber:
    """逆序数"""
    def __init__(self, arrange: list):
        self.arrange = arrange
        self.inverse_number = 0
        self._get_value()

    def _get_value(self):
        for i in range(len(self.arrange)):
            for j in range(i, len(self.arrange)):
                if self.arrange[i] > self.arrange[j]:
                    self.inverse_number += 1


class FullyArrange:
    """全排列"""
    def __init__(self, count: int):
        self.count = count
        self.result = list(itertools.permutations(range(count)))


if __name__ == '__main__':
    # i_number = InverseNumber([4, 2, 3, 5, 1])
    # print(i_number.inverse_number)

    f_arrange = FullyArrange(4)
    print(f_arrange.result)

