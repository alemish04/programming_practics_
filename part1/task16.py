def task16(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


# print(task16(13, 12))


def tests():
    assert task16(13, 12) == 1
    assert task16(16, 12) == 4
    assert task16(120, 40) == 40
    print("ok")

tests()