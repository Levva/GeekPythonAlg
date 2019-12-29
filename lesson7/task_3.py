import random


m = random.randint(0, 100)
size = 2 * m + 1
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


bubble_sort(array)

print(f'Медиана: {array[len(array) // 2 + 1]}')