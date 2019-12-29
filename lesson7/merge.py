import random

array = [random.randint(0, 10) for i in range(10)]
print(array)

def sort_merge(array):
    if len(array) < 2:
        return array
    left = sort_merge(array[:len(array) // 2])
    right = sort_merge(array[len(array) // 2:])
    print(left)
    print(right)
    merge(left, right)

def merge(left, right):
    res = []
    while len(left) > 1 and len(right) > 1:
        print()
        if left[0] >= right[0]:
            res.append(left[0])
            left = left[1:]
            print(res)
        else:
            res.append(right[0])
            right = right[1:]
            print(res)
    if len(left) < 2:
        res += left
    if len(right) < 2:
        res += right
    print(res)
sort_merge(array)