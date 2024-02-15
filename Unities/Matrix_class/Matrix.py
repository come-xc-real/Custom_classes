import copy


class Matrix:
    """
    矩阵类, 用于书写矩阵的相关方法和计算
    """
    def __init__(self, matrix_body: list):
        self.body = matrix_body
        self.clean_body = self._clean()

    def _clean(self):
        body = copy.deepcopy(self.body)     # 深度拷贝矩阵
        return
