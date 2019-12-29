import random

size = 10
array = [random.randint(0, 9) for i in range(size)]
# array = [random.uniform(0, 50) for i in range(size)]
print(array)

def merde_sort(array):
    n = len(array)
    if n < 2:
        return array

    l = merde_sort(array[:n//2])
    r = merde_sort(array[n//2:n])

    i = 0
    j = 0
    res = []

    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j += 1
        elif not j < len(r):
            res.append(l[i])
            i += 1
        elif l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    return res

res = merde_sort(array)

print(res)