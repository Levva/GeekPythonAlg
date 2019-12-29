# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search)

from collections import defaultdict
from random import randint


# генерируем случайный не ориентированный граф как defaultdict:
def graph_gen_rand_list(n):
    graph = defaultdict(list)
    print('Наш граф  - Вершина : [(ребро в вершину, стоимость ребра), ...] :')
    for i in range(n):
        for j in range(i + 1, n):
            if randint(0, 9) < 6:  # ребро между 2 вершинами генерируется с вероятностью 0.6
                tmp = randint(1, 10)  # стоимость ребра
                graph[i].extend([(j, tmp)])
                graph[j].extend([(i, tmp)])
        if len(graph[i]) == 0:  # исключим изолированные вершины
            while True:
                j = randint(0, n - 1)
                if j != i:
                    break
            tmp = randint(1, 10)
            graph[i].extend([(j, tmp)])
            graph[j].extend([(i, tmp)])
        print(i, ' : ', graph[i])
    return graph


# обходим рекурсивно
def dfs(graph, vertex_num, is_visited, path):
    is_visited[vertex_num] = True
    path.append(vertex_num)

    for i in graph[vertex_num]:
        if not is_visited[i[0]]:
            dfs(graph, i[0], is_visited, path)

    return path


print('*' * 100)
n = int(input('Введите число вершин: '))
graph = graph_gen_rand_list(n)
len_graph = len(graph)
path = []
is_visited = [False] * len_graph
# для простоты обходим с нулевой вершины. можно спросить с какой надо, если чо
dfs(graph, 0, is_visited, path)
print('*' * 100)
print(f'Порядок обхода графа: {path}')