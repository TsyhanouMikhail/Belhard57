# 2. Вывести в порядке возрастания цифры, входящие в десятичную запись натурального числа N.
from typing import List, Any

number = input("Введите число для модификации: ")
number_list: List[int] = []
i = 1

for i in range(0, len(number), 1):
    number_po_porjadku = int(number[i: i+1: 1])
    # print(number_po_porjadku)
    number_list.append(number_po_porjadku)


number_list.sort()
print(number_list)

