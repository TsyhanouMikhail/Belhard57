numbers = [1, 2, 3, 4]
i = 0
print(numbers)
while True:
    direction = int()
    if direction == ">":
        i += 1
    elif direction == "<":
        i -= 1

    if i == -1:
        i = len(numbers)-1
    elif i == len(numbers):
        i = 0
    print(numbers[i])


