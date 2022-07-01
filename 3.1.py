# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами #

text: str = input("Введите предложение: ")
print(text)

words = text.split()
#print(words)
words = "-".join(words)
print(words)

print(text.replace(" ", '-'))
