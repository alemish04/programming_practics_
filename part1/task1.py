"""
Введите строку, состоящую из 2 цифр. Преобразуйте ее в целое и вещественное число.
Выведите полученные 3 значения (строку, целое число, вещественное число)
на экран в одной строке через запятую, затем пропустите строку и вновь выведите
значения по одному на строке. Перед каждым значением выведите его тип.
"""


def task1(a):
    int_ = lambda x: int(x)
    float_ = lambda x: float(x)
    print(f"строка : {a}, целое : {int_(a)}, вещественное : {float_(a)}", end="\n\n")
    print(f"строка : {a}, \nцелое : {int_(a)}, \nвещественное : {float_(a)}")


task1(input("введите число : "))
