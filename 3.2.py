# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3 #

#m1
formula: float
number1: float = input("Введите число 1: ")

#if type(number1) == int or type(number1) == float:
 #   print("Ново или закройте программу.")
#else:
#    print("Неверный формат числа. Введите заново или закройте программу.")

#print("Неверный формат числа. Введите заново или закройте программу.")
#print(number1.isdigit())
#if True:
#    print("00")
#elif False:
#    print("55")
#else:
#    print("Неверный формат числа. Введите заново или закройте программу.")
number2: float = input("Введите число 2: ")

number3: float = input("Введите число 3: ")

print("Вы ввели числа: ", float(number1), float(number2), float(number3))

formula = (float(number1) + float(number2) + float(number3))/3
#print("Среднее арифметическое ваших чисел: ", formula)
print("Среднее арифметическое ваших чисел: ", round(formula, 3))
