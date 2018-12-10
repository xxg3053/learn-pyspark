from linear_algebra.playLA.Vector import Vector

if __name__ == '__main__':
    v1 = Vector([1, 2, 3])
    print(v1) # (1, 2, 3)
    print(len(v1)) # 3
    print("v1[0] = {}, v1[1] = {}".format(v1[0], v1[1])) # v1[0] = 1, v1[1] = 2

    v2 = Vector([4, 3, 3])
    print("{} + {} = {}".format(v1, v2, v1 + v2))  # (1, 2, 3) + (4, 3, 3) = (5, 5, 6)
    print("{} - {} = {}".format(v1, v2, v1 - v2)) # (1, 2, 3) - (4, 3, 3) = (-3, -1, 0)

    print("{} * {} = {}".format(v1, 3, v1 * 3)) # (1, 2, 3) * 3 = (3, 6, 9)
    print("{} * {} = {}".format(3, v2, 3 * v2)) # 3 * (4, 3, 3) = (12, 9, 9)

    print("+{} = {}".format(v1, +v1))
    print("-{} = {}".format(v1, -v1))

    zero2 = Vector.zero(5)
    print(zero2) # (0, 0, 0, 0, 0)

    print("norm({}) = {}".format(v1, v1.norm())) # norm((1, 2, 3)) = 3.7416573867739413
    print("normalize {} is {}".format(v1, v1.normalize())) # normalize (1, 2, 3) is (0.2672612419124244, 0.5345224838248488, 0.8017837257372732)
    print(v1.normalize().norm()) # 1

    try:
        zero2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}.".format(zero2))

