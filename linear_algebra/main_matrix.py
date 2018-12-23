from linear_algebra.playLA.Matrix import Matrix

if __name__ == '__main__':
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print("matrix.shape = {}".format(matrix.shape()))
    print("matrix.size = {}".format(matrix.size()))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print("add: {}".format(matrix + matrix2))
    print("subtract: {}".format(matrix - matrix2))
    print("scalar-mul: {}".format(matrix * 2))