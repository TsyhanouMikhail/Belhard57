# Сделать калькулятор: у пользователя спрашивается
# число, потом действие и второе число

number_1 = int(input("Введите число 1: "))

znak = input("Введите действие: ")

number_2 = int(input("Введите число 2: "))

if znak == "+":
    print("Результат: ", number_1 + number_2)
elif znak == "-":
    print("Результат: ", number_1 - number_2)
elif znak == "*":
    print("Результат: ", number_1 * number_2)
elif znak == "/":
    if number_2 == 0:
        print("На ноль делить нельзя ")
    else:
        print("Результат: ", number_1 / number_2)
else:
    print("Введены некорректные данные: ")


