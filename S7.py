# Описать класс student с атрибутами first_name: str, last_name: str, marks: list[int]
# реализовать магические методы сравненияю которые будут сравнивать на основании
# среднего фрифметического списка marks

from typing import List

class Student:
    def __init__(self, first_name: str, last_name: str, marks: List[int]) -> None:
        self.marks = marks
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def average(other) -> bool:
        """

        :param other:
        :return:
        """
        return

    def __eq__(self, other):
        return  (sum(self.marks) / len(self.marks)) == (sum(other.marks)) / len(other.marks)

    # def save_sum(self, marks):
    #     self.summa: float = sum(marks) / len(marks)

vasja = (vasja, pupkin, [5, 4, 5, 4])
print(marks)
