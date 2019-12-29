# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).


import random

def graph(n):
    return {i: {j for j in range(random.randint(i, n)) if i != j} for i in range(n)}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


vertex_number = 6
a = graph(vertex_number)

for k, v in a.items():
    print(k, v)

# print(a)

for i in range(vertex_number):
    print(f'из вершины {i} можно достичь вершин {dfs(a, i)}')
