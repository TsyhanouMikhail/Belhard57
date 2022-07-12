# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

array = [1, 2, 18, 36, 189, 354, 57, 17, 158, 750]
i = 0
array_1 = []
for i, value in enumerate(array):
    if i < len(array):
        if value % 2 == 0:
            i += 1
            array_1.append(value)
        else:
            i += 1
for i, value in enumerate(array):
    if i < len(array):
        if value % 2 != 0:
            i += 1
            array_1.append(value)
        else:
            i += 1

print("Начальный список", array)
print("Отсортированный список", array_1)

###---  2 version ###

for i, value in enumerate(array):
    if i < len(array):
        if value % 2 == 0:
            i += 1
            array_1.append(value)
        else:
            i += 1
            array_2.append(value)

array_3 = array_1 + array_2
print("Начальный список", array)
print("Отсортированный список", array_3)



