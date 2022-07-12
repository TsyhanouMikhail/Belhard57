# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
from typing import List

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7]
sdvig = int(input("Введи число сдвига: "))


def perenos(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

print(numbers)

perenos(numbers, sdvig)
print(numbers)


