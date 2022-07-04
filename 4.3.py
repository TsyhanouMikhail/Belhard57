# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

import collections

record = int(input("Введите число записей: "))

User = collections.defaultdict(list)
print(User)
for i in range(record):
    User[input("name: ")].append(input("email: "))

print(User)

User_1 = collections.defaultdict(list)
for i in range(record):
    User_1[i].append(i)

print(User_1)
chain = collections.ChainMap(User_1, User)
print(chain)
#не уверен, что правильно
