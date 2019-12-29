# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

import random
from collections import deque


def graph(n):
    return {i:
                {j: random.randint(1, 10) for j in range(random.randint(i, n)) if i != j}
            for i in range(n)}


def dijkstra(graph, start, finish, visited=[], distances={}, parents={}):
    if start == finish:
        path = deque()
        pred = finish

        while pred != None:
            path.appendleft(pred)
            pred = parents.get(pred, None)
        # не понял почему работет только принт.
        # При сохранении вывода в переменную функция возвращает None
        # Если есть идеи почему - напишите в комментарии к ДЗ.
        print(
            f'кратчайший путь: {list(path)} '
            f'стоимость = {distances[finish]}'
        )

    else:
        if not visited:
            distances[start] = 0

        for neighbor in graph[start]:
            if neighbor not in visited:
                new_distance = distances[start] + graph[start][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    parents[neighbor] = start
        visited.append(start)

        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, finish, visited, distances, parents)


g = graph(10)

for k, v in g.items():
    print(k, v)

# еще одна проблема функции dijkstra граф из функции не итерируется...
# Если есть идеи почему - напишите в комментарии к ДЗ
# Поэтому старт и финиш придется вводить руками
# for k in g.keys():
#    dijkstra(g, k, len(g))

dijkstra(g, 0, 9)

# Обрботчик исключений писать не стал,
# если некоторые вершины графа изолированы, может вернуть ошибку.
