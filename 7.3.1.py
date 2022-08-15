# 3. На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу
# размером n х m, заполнив ее по спирали числами от 1 до n x m. Спираль начинается в левом верхнем углу и
# закручивается по часовой стрелке.

# m = int(input("Введите ширину матрицы: "))
# n = int(input("Введите высоту матрицы: "))

N = 3
M = 4
A = []
for i in range(N):
    A.append([0]*M)
    # print(A)

for i in range(len(A)):         # len(A) - возвращает количество строк в матрице А
    for j in range(len(A[i])):  # len(A[i]) - возвращает количество элементов в строке i
        print(A[i][j], end = ' ')
    print()                     # делаем переход на новую строку
# print(A)




# matrix = [[0] * m for _ in range(n)]
# dx, dy, x, y = 0, 1, 0, 0
#
# for i in range(1, n * m + 1):
#     matrix[x][y] = i
#     if matrix[(x + dx) % n][(y + dy) % m]:
#         dx, dy = dy, -dx
#     x += dx
#     y += dy
# for line in matrix:
#     print(*(f'{i:<3}' for i in line), sep='')