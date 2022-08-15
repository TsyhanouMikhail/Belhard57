# from unittest import TestCase
import pytest


# class MyMath:
#     def__init__(self):
#     pass

def multiply(a, b):
    return a * b


# class Test(TestCase):
#
#     def test_multiply(self):
#         self.assertEqual(multiply(2, 4), 8)
#
#     def test_multiply2(self):
#         self.assertNotEqual(multiply(2, 4), 8)

@pytest.mark.parametrize(
    'a, b, c', [
        (2, 4, 8),
        (3, 5, 15),
        (12, 8, 96)
    ]
)
def test_multiply(a, b, c):
    assert multiply(a, b) == c

# def test_multiply2(a, b, c):
#     assert multiply(a, b) != c
