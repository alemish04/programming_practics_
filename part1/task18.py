names = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября",
         "декабря"]
nums = [i for i in range(1, 13)]

dist_main = dict(zip(names, nums))


def task18(a):
    x = a.split()
    if (dist_main[x[1]]) > 9:
        month = str(dist_main[x[1]])
    else:
        month = "0" + str(dist_main[x[1]])
    return str(x[0]) + "." + month + "." + str(x[2])


#
# print(task18("1 апреля 2021"))


def tests():
    assert task18("1 апреля 2021") == "1.04.2021"
    assert task18("12 апреля 2022") == "12.04.2022"
    print("ок")


tests()
