# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

data = {
    "fname": str(input("Введите имя: ")),
    "lname": str(input("Введите фамилию: "))

}

text = list(data.values())

text: str = "".join(text)

letters: str = list(text)

print(letters.count(input("Введите символ, который необходимо искать: ")))
