# Сортировка пузырьком


import random

size = 10
array = [random.randint(-100, 100) for i in range(size)]
print(array)


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


bubble_sort(array)
print(array)
