# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами #

text: str = input("Введите предложение: ")
print(text)

words = text.split()
words = "-".join(words)
print(words)

print(text.replace(" ", '-'))
