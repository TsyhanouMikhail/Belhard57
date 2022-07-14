# 1. Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или
# слово NO в противном случае.  Без использования оператора возведения в степень. Сделать с помощью рекурсии


number_1 = int(input("Введите чило для проверки: "))
x = 1
def proverka_number(numbers):
    x = 1
    if numbers == 1:
        pass
    elif numbers % 2 == 0:
        while x < numbers:
            x *= 2
        else:
            if x == numbers:
                print('YES')
            elif x > numbers:
                print('NO')
    else:
        print('NO')

proverka_number(number_1)
# print(number_1)
