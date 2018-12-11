"""
numpy 向量的学习
"""

import numpy as np

if __name__ == '__main__':
    print(np.__version__)
    """
    为什么要使用numpy向量
    1. 自定义的数组可以存储不同的类型
    2. 更容易定义相关属性
    """

    vec = np.array([1, 2, 3])
    print(vec)
    # vec[0] = "abc"
    # vec[0] = 666
    # print(vec) # [666   2   3]

    # np.array的创建
    print(np.zeros(5)) # [0. 0. 0. 0. 0.]
    print(np.ones(5)) # [1. 1. 1. 1. 1.]
    print(np.full(5, 666)) # [666 666 666 666 666]

    # np.array的基本属性
    print("size =", vec.size) # 3
    print("size =", len(vec)) # 3
    print(vec[0]) # 1
    print(vec[-1]) # 3
    print(vec[0:2]) # [1 2]
    print(type(vec[0:2])) # <class 'numpy.ndarray'>

    # np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec, 2 * vec2))
    print("{} * {} = {}".format(vec, 2 , vec2 * 2))
    print("{} * {} = {}".format(vec, vec2, vec * vec2)) # [1 2 3] * [4 5 6] = [ 4 10 18] 逐个元素相乘，在几何上没有数学意义
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2))) # 向量的点乘 32
    # linalg 线性代数的缩写
    print(np.linalg.norm(vec)) # 向量的模(长度)
    print(vec / np.linalg.norm(vec)) # 单位向量
    print(np.linalg.norm(vec /np.linalg.norm(vec))) # 单位向量取模 1



