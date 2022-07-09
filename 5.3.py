# Вывести четные числа от 2 до N по 5 в строку
N: int = int(input())
# c = 0
# for i in range(2, N+1, 2):
#     if c < 5:
#         print(i, end=" ")
#         c += 1
#     else:
#         c = 1
#         print()
#         print(i, end=" ")

#555
for i in range(2, N+1, 10):
    for j in range(i, i+9, 2):
        if j > N:
            break
        print(j, end=" ")
    print()

