"""
Реализуйте умножение двух матриц, записанных как список списков
(без использования специализированных библиотек).
При этом надо проверить, что размерности матриц таковы, что их можно умножать.
 Если не, то надо вывести сообщение об ошибке.
"""


def task9(A, B):
    if len(A[0]) == len(B):

        result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)] for row_a in A]
        # zip(*B) - столбцы матрицы 2
        # row_a - стороки матрицы 1

        return result
    else:
        return "ERROR"


A = [[5, 4], [2, 4], [4, 7]]

B = [[3, 2, 4], [4, 3, 6]]

print(task9(A, B))