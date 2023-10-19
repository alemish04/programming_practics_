"""
Введите целое число. Выведите его на экран и допишите к нему слова «рубль»,
«рубля» или «рублей» в зависимости от значения.
"""


def task15(a):
    ley_ = ["5", "6", "7", "8", "9", "0"]
    l = ["1"]
    lia = ["2", "3", "4"]

    if len(a) > 1:
        if a[-2] == "1":
            # print("рублей")
            return "рублей"

        elif a[-2] != "1" and a[-1] in ley_:
            return "рублей"
        elif a[-2] != "1" and a[-1] in l:
            return "рубль"
        elif a[-2] != "1" and a[-1] in lia:
            return "рубля"

    else:

        if a[-1] in ley_:
            return "рублей"
        elif a[-1] in l:
            return "рубль"
        elif a[-1] in lia:
            return "рубля"


# task15((input()))


def tests():
    assert task15("12") == "рублей"
    assert task15("22") == "рубля"
    assert task15("2") == "рубля"
    assert task15("102") == "рубля"
    print("ок")
tests()
