from heapq import merge


def task7(a, b):
    return list(merge(a, b))

def task7_1(a):  # без встроенных методов

    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        task7_1(left)
        task7_1(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1

def tests():
    assert task7([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]# тест для первого варианта


    b = [1, 3, 5];    c = [2, 4];     a = b+c;     task7_1(a) # тест для второго варианта
    assert a == [1, 2, 3, 4, 5]
    print("ok")


tests()



