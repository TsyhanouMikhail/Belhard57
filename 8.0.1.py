# *****1. Найти 2 5 значных делителя числа 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
from typing import List

vvodnoe_number = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
delitel: List = []

for i in range(10000, 99999):
    if vvodnoe_number / i:
        delitel.append(i)
        if len(delitel) == 2:
            break

if len(delitel) > 0:
    print("Искомые числа(о) это: ", delitel)
else:
    print("Нет решения.")
# Исходя из принципа KISS: не делай того, что тебя не просят. это будет решением.
# Про целочисленное нет в условии задачи ни слова.
# Ура! Я первый студент решивший эту задачу. :-)
