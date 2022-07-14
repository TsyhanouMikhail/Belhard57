# 2. Дано число, определить является ли оно простым

number_1 = int(input("Введите чило для проверки \"на простату :-)\": "))

def pereshet(number):
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

print(pereshet(number_1))



# from typing import List
# array: List[int] = []
# number_1 = int(input("Введите чило для проверки: "))
#
# for i in range(number_1 - 1):
#     if (number_1 < 2):
#         pass
#     else:
#         array.append(i + 2)
#
# print(array)
#
# for i, value in enumerate(array):
#     if value >= 2 and :
#         print(array)
#         print(i)
#         if value == (i + 2):
#             array.pop(i)
#     else:
#         print("iii")
#
# # print(number_1)
# print(array)