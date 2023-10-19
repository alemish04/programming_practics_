"""
Выведите значение заданного целого числа от 0 до 1000 прописью.
Например, «сто девяносто один» для числа 191, «одиннадцать» для числа 11.
"""
from num2words import num2words
def task17(a):


    number = a
    if 0 <= number <= 1000:
        res = num2words(number, lang='ru')
        return res
    else:
        return "Ошибка: Число должно быть от 0 до 1000"
# task17(int(input()))

def tests():
    assert task17(123)=="сто двадцать три"
    assert task17(998)=="девятьсот девяносто восемь"
    print("ок")


tests()

