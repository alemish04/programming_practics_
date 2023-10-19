"""
Создайте 2 списка из 5 случайных целых чисел от 1 до 10. Найдите симметрическую разность
множеств, соответствующих спискам в выведете ее на печать.
"""
import random
from random import randint


def task13(a, b):
    print(a, b, a.symmetric_difference(b))

    return a.symmetric_difference(b)


a = set([random.randint(1, 10) for i in range(5)])  # значения могут повториться
b = set([random.randint(1, 10) for i in range(5)])  # значения могут повториться
while True:
    if len(a) < 5:
        a.add(random.randint(1, 10))
    elif len(b) < 5:
        b.add(random.randint(1, 10))
    else:
        break

# print(task13())


def tests():
    try:
        assert task13({1, 2, 7, 8, 10}, {2, 5, 7, 9, 10}) == {1, 5, 8, 9}
        print("всё ок")
    except AssertionError:
        print("error")

    try:
        assert task13({3, 4, 5, 6, 8}, {2, 3, 5, 8, 10}) == {2, 4, 6, 9}
        print("всё ок")
    except AssertionError:
        print("error")
tests()