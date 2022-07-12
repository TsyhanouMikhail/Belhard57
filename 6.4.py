# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
from typing import List

ne_numbers: List[str] = [1, 2, "3", "Hello", 4, 5, "World", "Привет", 6, 7, 90]

print(ne_numbers)

def my_filter(ne_):
    if isinstance(ne_, str):
        return True
    else:
        return False

ne_numbers = filter(my_filter, ne_numbers)

print("Отфильтрованный список: ", list(ne_numbers))

