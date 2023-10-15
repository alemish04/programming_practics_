def task8(a):
    temp = list(a.strip().split())
    temp.sort()
    return temp, " ".join(temp)


def tests():  # тесты
    assert task8("llex   amex   amax  ") == (['amax', 'amex', 'llex'], 'amax amex llex')

    print("ok")


tests()
