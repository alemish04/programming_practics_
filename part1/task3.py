"""
По номеру года определите, является ли данный год високосным.
(год является високосным,
если его номер кратен 4, но не кратен 100, а также если он кратен 400).
"""


def task3(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        return True
    else:
        return False


# print(task3(int(input())))


def tests():  # тесты
    assert task3(1900) == False
    assert task3(1904) == True
    assert task3(1903) == False
    print("ok")


tests()



