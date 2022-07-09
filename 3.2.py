# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3 #

#m1
formula: float
number1: float = input("Введите число 1: ")

number2: float = input("Введите число 2: ")

number3: float = input("Введите число 3: ")

print("Вы ввели числа: ", float(number1), float(number2), float(number3))

formula = (float(number1) + float(number2) + float(number3))/3
#print("Среднее арифметическое ваших чисел: ", formula)
print("Среднее арифметическое ваших чисел: ", round(formula, 3))
