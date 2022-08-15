# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами #

text: str = input("Введите предложение: ")
print("1", text)

words = text.split()
print("2", words)
words = "-".join(words)
print("3", words)

print("4", text.replace(" ", '-'))
