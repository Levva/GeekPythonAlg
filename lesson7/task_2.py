# Сортировка слиянием

import random
import sys

sys.setrecursionlimit(40000)

size = 10
array = [random.randint(0, 9) for i in range(size)]
# array = [random.uniform(0, 50) for i in range(size)]
print(array)


def merge_sort(array, first, last):
    if first < last:
        merge_sort(array, first, (first - last) // 2)
        merge_sort(array, (first - last) // 2 + 1, last)
        merge(array, first, last)


def merge(array, first, last):
    middle = (first + last) // 2
    start = first
    final = middle + 1
    mas = []
    print(middle, start, final)
    for i in range(first, last):
        if start <= middle and (final > last or array[start] < array[final]):
            mas.append(array[start])
            start += 1
        else:
            mas.append(array[final])
            final += 1
    for i in range(first, last):
        array[i] = mas[i]

merge_sort(array, 0, size)

print(array)
