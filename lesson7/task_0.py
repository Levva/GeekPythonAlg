import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

# Сортировка пузырьком

n = 1

while n < len(array):
    for i in range(len(array) - n):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    n += 1
    print(array)

# print(array)

# Сортировка обмена
# def selection_sort(array):
#     for i in range(len(array)):
#         idx_min = i
#
#         for j in range(i + 1, len(array)):
#             if array[j] < array[idx_min]:
#                 idx_min = j
#
#         array[idx_min], array[i] = array[i], array[idx_min]
#
# selection_sort(array)

# Сортировка вставкой
# def insertion_sort(array):
#     for i in range(1, len(array)):
#         spam = array[i]
#         j = i
#         while array[j-1] > spam and j > 0:
#             array[j] = array[j-1]
#             j -= 1
#         array[j] = spam
#         print(array)
#
# insertion_sort(array)

# Сортировка Шелла
# def shell_sort(array):
#     assert len(array) < 4000, 'Массив слишком большой для данного вида сортировки'
#
#     def new_incrment(array):
#         inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
#
#         while len(array) <= inc[-1]:
#             inc.pop()
#
#         while len(inc) > 0:
#             yield inc.pop()
#
#     count = 0
#
#     for increment in new_incrment(array):
#         for i in range(increment, len(array)):
#             for j in range(i, increment-1, -increment):
#                 if array[j - increment] <= array[j]:
#                     break
#                 array[j], array[j-increment] = array[j-increment], array[j]
#                 count += 1
#                 # print(array)
#     print(count)
#
# shell_sort(array)

# # Сортировка Хоара
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = random.choice(array)
#     s_array = []
#     m_array = []
#     l_array = []
#
#     for item in array:
#         if item < pivot:
#             s_array.append(item)
#         elif item > pivot:
#             l_array.append(item)
#         elif item == pivot:
#             m_array.append(item)
#         else:
#             raise Exception('Случилось некоторое')
#     # print(s_array, m_array, l_array)
#     return quick_sort(s_array) + m_array + quick_sort(l_array)
#
# # array_new = quick_sort(array)
#
# def quick_sort_no_memory(array, fst, lst):
#     if fst >= lst:
#         return
#
#     pivot = array[random.randint(fst, lst)]
#     i,j = fst, lst
#
#     while i <= j:
#
#         while array[i] < pivot:
#             i += 1
#
#         while array[j] > pivot:
#             j -= 1
#
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#
#             i, j = i + 1, j - 1
#
#     quick_sort_no_memory(array, fst, j)
#     quick_sort_no_memory(array, i, lst)
#
#
# # array_new = quick_sort_no_memory(array, 0, len(array) - 1)
#
# def revers(array):
#     for i in range(len(array) // 2):
#         array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]
#
# revers(array)
#
#
# print('*' * 50)
#
# t = tuple(random.randint(0, 100) for _ in range(size))
# print(t)
#
# # t.sort()
#
# t = tuple(sorted(t, reverse = True))
# print(t)
# print(array)
