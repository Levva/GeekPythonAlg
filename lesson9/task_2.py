import heapq
from collections import Counter
from collections import namedtuple


# Класс для узла
class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, path):
        self.left.walk(code, path + '0')
        self.right.walk(code, path + '1')


# Класс для листьев
class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


# Кодирование по Хаффману
def search(str):
    heap_start = []
    for ch, freq in Counter(str).items():
        heap_start.append((freq, len(heap_start), Leaf(ch)))
    heapq.heapify(heap_start)
    count = len(heap_start)
    while len(heap_start) > 1:
        freq1, count1, left = heapq.heappop(heap_start)
        freq2, count2, right = heapq.heappop(heap_start)
        heapq.heappush(heap_start, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if heap_start:
        [(_freq, count3, root)] = heap_start
        root.walk(code, '')
    return code


str = 'Lorem ipsum dolor'
print(f'Звкодируем строку: /n{str}')

uniq = list(set(str))
count_uniq_unsorted = [0] * len(uniq)

# Определение весов для каждого символа (сколько раз встречается)
for i in range(len(uniq)):
    for item in str:
        if item == uniq[i]:
            count_uniq_unsorted[i] += 1

print(f'В строке встречаются символы:\n{uniq}\nв следующем количестве:\n{count_uniq_unsorted}')

table = search(str)
print('Результат кодирования строки:')
for i, item in table.items():
    print(f'"{i}" : {item}')