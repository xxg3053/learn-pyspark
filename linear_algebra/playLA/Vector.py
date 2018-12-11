"""
自定义向量
"""
import math
from ._global import EPSILON

class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e**2 for e in self._values))

    def normalize(self):
        """返回向量的单位向量"""
        # 浮点数不应该使用==比较（self.norm() == 0）
        # print(EPSILON)
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error ! norm is zero.")
        # return Vector([e / self.norm() for e in self])
        # return 1 / self.norm() * Vector(self._values)
        return Vector(self._values) / self.norm()

    def __add__(self, other):
        """向量加法，返回结果向量"""
        assert len(self) == len(other),\
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a,b in zip(self, other)])

    def __sub__(self, other):
        """向量减法，返回结果向量"""
        assert len(self) == len(other), \
            "Error in subtracting. Length of vectors must be same."
        # return Vector([a - b for a,b in zip(self._values, other._values)]) # 重写了迭代器
        return Vector([a - b for a,b in zip(self, other)])

    def dot(self, other):
        """向量的点乘，返回结果标量"""
        assert len(self) == len(other),\
            "Error in dot product. Length of vectors must be same."
        return sum(a * b for a,b in zip(self, other))

    def __mul__(self, other):
        """向量乘法，返回结果向量： self * other"""
        return Vector([other * e for e in self])

    def __rmul__(self, other):
        """向量乘法，返回结果向量： other * self"""
        return self * other

    def __truediv__(self, other):
        """返回数量除法的结果向量：self / other"""
        return (1 / other) * self

    def __pos__(self):
        """向量取正的结果"""
        return 1 * self

    def __neg__(self):
        """向量取负的结果"""
        return -1 * self

    def __getitem__(self, index):
        """取向量第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __repr__(self):
        """返回一个可以用来表示对象的可打印字符串"""
        return "Vector({})".format(self._values)

    def __str__(self):
        """被打印的时候需要以字符串的形式输出的时候"""
        return "({})".format(", ".join(str(e) for e in self._values))