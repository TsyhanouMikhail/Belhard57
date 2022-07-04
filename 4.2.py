# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
from typing import List

data = {
    "fname": str(input("Введите имя: ")),
    "lname": str(input("Введите фамилию: "))

}
#print(data)

text = list(data.values())
print(text)
letters: List[str] = list(text)

# не работает разбивка на символы. может опять какой глюк. с Хелло ворд все работает.
# или недостаток серого вещества :-(

# text = "hello world"
# print(text)
# letters: List[str] = list(text)
# print(letters)

print(letters)
print(letters.count(input("Введите символ, который необходимо искать: ")))
