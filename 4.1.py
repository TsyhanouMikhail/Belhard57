# Заполнить список степенями числа 2 (от 2^1 до 2^n) #

stepen = int(input("Введите степень: "))
numbers = []
formula = 2

for i in range(stepen):
    numbers = numbers + [formula]
    formula *= 2

print(numbers)

