# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

number: int = int(input("Введите число: "))

number_1 = ""
while number > 0:
    number_1 = str(number % 2) + number_1
    number = number // 2

print("Твоя цифра в двоичном коде выглядит так: ", number_1)

def bin_to_dec(digit):
    dlina = len(digit)
    chislo_dec = 0
    for i in range(0, dlina):
        chislo_dec = chislo_dec + int(digit[i]) * (2 ** (dlina - i - 1))
    return chislo_dec
print("Двоичное целое число", number_1, "соответствует десятичному числу ", bin_to_dec(number_1))


