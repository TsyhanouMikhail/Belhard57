# *****1. Найти 2 5 значных делителя числа 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
from typing import List

vvodnoe_number = 888888888888888888888888888
# polovina_number = int(1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006140 / 2)
delitel: List = [str]
ii: str

for i in range(9999, 100000):
    if vvodnoe_number % i == 0:
        # ii = i
        # if len(str(ii)) == 5:
        delitel.append(i)
        print(delitel)

        if len(delitel) == 3:
            print(delitel)
            break
        else:
            pass
    else:
        pass

        # print("Нет решения.")
print("2 пятизначных числа это: ", delitel)
# Логика тут моя, а не гугла! закончил в 4:34

