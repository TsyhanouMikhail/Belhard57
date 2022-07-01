# Пользователь вводит 3 числа, сказать сколько из них положительных #
# и сколько отрицательных #

formula1: int
formula2: int
formula3: int

formula1 = 0
formula2 = 0
formula3 = 0

number1: float = input("Введите число 1: ")
number2: float = input("Введите число 2: ")
number3: float = input("Введите число 3: ")

print("Вы ввели числа: ", float(number1), float(number2), float(number3))

if float(number1) > 0:
   formula1 = formula1 + 1
elif float(number1) < 0:
    formula2 = formula2 + 1
elif float(number1) == 0:
    formula3 = formula3 + 1

if float(number2) > 0:
   formula1 = formula1 + 1
elif float(number2) < 0:
    formula2 = formula2 + 1
elif float(number2) == 0:
    formula3 = formula3 + 1

if float(number3) > 0:
   formula1 = formula1 + 1
elif float(number3) < 0:
    formula2 = formula2 + 1
elif float(number3) == 0:
    formula3 = formula3 + 1

print("Положительных чисел: ", formula1)
print("Отрицательных чисел: ", formula2)
print("Нулей: ", formula3)
