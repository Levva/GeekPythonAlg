from collections import namedtuple
graph = [[1, 2], [0, 2, 3], [0, 1], [1]]

print(*graph, sep='\n')

print('*' * 50)

graph1 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1}
}

print(graph1)

if 3 in graph1[1]:
    print(True)

print('*' * 50)
Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph2 = []

graph2.append([Vertex(1, 2), Vertex(2, 3)])
graph2.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph2.append([Vertex(0, 3), Vertex(1, 2)])
graph2.append([Vertex(1, 1)])

print(*graph2, sep='\n')

for v in graph2[1]:
    if v.vertex == 3:
        print(True)


class Grapf:
    def __init__(self, vertex, edge, spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam
    