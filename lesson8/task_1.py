# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.


import numpy as np

size = int(input('Сколько человек встретилсь? '))


def create_graph(values, size):
    upper = np.zeros((size, size))
    upper[np.triu_indices(size)] = values
    for i in range(size):
        for j in range(size):
            if i == j:
                upper[i, j] = 0
    return upper


def count_graph(graph):
    sum_matrix = int(np.sum(graph))
    return sum_matrix


g = create_graph(1, size)
print(f'Граф рукопожатий выглядит так: \n{g}')

result = count_graph(g)

print(f'Все было {result} рукопожатий')
