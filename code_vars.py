# Завершите функцию квадратной суммы, чтобы она возводила в квадрат каждое переданное ей число, а затем суммировала результаты.
# Например, for  [1, 2, 2] это должно возвращаться  , 9 потому что  1^2 + 2^2 + 2^2 = 9.
# def square_sum(numbers):
#     out = []
#     for i in numbers:
#         out.append(i ** 2)
#     return sum(out)


# def no_space(x):
#     return x.replace(' ' ,'')


# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
# def bool_to_word(boolean):
#     # TODO
#     if boolean:
#         return "Yes"
#     else:
#         return "No"


# DESCRIPTION:
# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.
# def positive_sum(arr):
#     # Your code here
#     arr_number = 0
#     for number in arr:
#         if number > 0:
#             arr_number += number
#         else:
#             pass
#     return arr_number


# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
# def quarter_of(month):
#     # your code here
#     data = {
#         1: 1,
#         2: 1,
#         3: 1,
#         4: 2,
#         5: 2,
#         6: 2,
#         7: 3,
#         8: 3,
#         9: 3,
#         10: 4,
#         11: 4,
#         12: 4,
#     }
#     month_qartet = data.get(month)
#     return month_qartet

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
# [10, 343445353, 3453445, 3453545353453] should return 3453455.
# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     numbers_new = numbers[0] + numbers[1]
#     return numbers_new
#     # your code here

# DESCRIPTION:
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
#
# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
# def make_negative( number ):
#     return -number if number>0 else number



