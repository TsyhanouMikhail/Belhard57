# *****1. Найти 2 5 значных делителя числа 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
from typing import List

vvodnoe_number = 8633
a = int(8634 / 2)
delitel: List = []
# polovina_number = int(15
for i in range(2, a):
    if vvodnoe_number % i == 0:
        delitel.append(i)
        # print(delitel)
        if len(delitel) == 3:
            break

if len(delitel) > 0:
    print("Искомые числа(о) это: ", delitel)
else:
    print("Нет решения.")
# Решил. RSA 100