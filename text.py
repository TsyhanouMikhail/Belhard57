# переставить местами первое и последнее слово

# text: list[str] = input().split()
# text[0], text[-1] = text[-1], text[0]
# text: str = " ".join(text)
# print(text)
from typing import List


text: List[str] = input().split()
text[0], text[-1] = text[-1], text[0]
text: str = " ".join(text)
print(text)


#from typing import List


text = "hello world"
print(text)
letters: List[str] = list(text)
print(letters)