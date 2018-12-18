from linear_algebra.playLA.Vector import Vector


class Matrix:

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    @classmethod
    def zero(self, r, c):
        """返回一个r行c列的零矩阵"""
        return self([[0] * c for _ in range(r)])

    def __add__(self, other):
        assert self.shape() == other.shape(),\
            "Error in adding. Shape of matrix must be same."
        return Matrix([[a + b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])

    def __sub__(self, other):
        assert self.shape() == other.shape(), \
            "Error in subing. Shape of matrix must be same."
        return Matrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])

    def __mul__(self, k):
        """返回矩阵的数量乘结果：self * k"""
        return Matrix([[e * k for e in self.row_vector(i)] for i in range(self.row_num())])

    def __rmul__(self, k):
        """返回矩阵的数量乘结果： k * self """
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果矩阵：self / k"""
        return (1 / k) * self

    def __neg__(self):
        return -1 * self

    def row_vector(self, index):
        """返回矩阵第index个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵第index个列向量"""
        return Vector(row[index] for row in self._values)

    def __getitem__(self, pos):
        """返回矩阵pos位置的元素"""
        r, c = pos
        return self._values[r][c]


    def size(self):
        """返回矩阵的元素个数"""
        r, c = self.shape()
        return r * c

    def row_num(self):
        return self.shape()[0]

    __len__ = row_num

    def col_num(self):
        return self.shape()[1]

    def shape(self):
        """返回矩阵的形状：（行数， 列数）"""
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__
