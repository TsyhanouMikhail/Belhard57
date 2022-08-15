# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

array = [5, 10, 15, 20, 25]
array_1 = []
i = 0
for i, value in enumerate(array):
    if i < len(array) - 1:
        if i == 0:
            i_new = array[0] + array[-1]
            array_1.append(i_new)
            i += 1

        else:
            i_new = array[i - 1] + array[i + 1]
            array_1.append(i_new)
            i += 1

i_new = array[(i - 1)] + array[i] + array[0]
array_1.append(i_new)
print(array)
print(array_1)
