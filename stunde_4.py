# переставить местами первое и последнее слово

# text: list[str] = input().split()
# text[0], text[-1] = text[-1], text[0]
# text: str = " ".join(text)
# print(text)
from typing import list #без импорта надо убрать лист


text: list[str] = input().split()
text[0], text[-1] = text[-1], text[0]
text: str = " ".join(text)
print(text)

text: str = input()
first = text[:text.find(" ")]
last = text[text.rfind(" ") + 1:]
center = text[text.find(" ") + 1: text.rfind(" ")]
text = last + " " + center + " " + first

print(text)