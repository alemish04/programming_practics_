"""
Имеется строка с названиями товаров вида «яблоки, груши, яблоки, киви, сливы, киви».
Товары перечислены через запятую, товары могут повторяться,
после запятой может стоять пробел. Выведите таблицу из двух колонок.
В левой колонке - название товара, в правой - количество названий этого товара, встречающихся в строке.
Таблицу надо упорядочить по уменьшению количества названий товара в строке.
"""
from prettytable import PrettyTable


def task11(a):
    dict_a = {}
    for i in a.split(", "):
        dict_a[i] = a.count(i)
    dict_a = {k: v for k, v in sorted(dict_a.items(), key=lambda item: item[1], reverse=True)}

    t = PrettyTable(['name', 'amount'])
    for key, val in dict_a.items():
        t.add_row([key, val])
    print(t)
    return dict_a


# print(task11("яблоки, груши, яблоки, киви, сливы, киви"))

def tests():
    try:
        assert task11("яблоки, груши, яблоки, киви, сливы, киви") == {'яблоки': 2, 'киви': 2, 'груши': 1, 'сливы': 1}
        print("всё ок")
    except AssertionError:
        print("error")

    try:
        assert task11("яблоки, вишни, яблоки, киви, сливы, киви") == {'яблоки': 2, 'киви': 2, 'груши': 1, 'сливы': 1}
        print("всё ок")
    except AssertionError:
        print("error")


tests()
