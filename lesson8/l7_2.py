#2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.
from collections import deque
graph=[[0,2,1,3,0,0],
       [2,0,0,0,0,2],
       [1,0,0,1,2,0],
       [3,0,1,0,1,0],
       [0,0,2,1,0,1],
       [0,2,0,0,1,0]]
def dej(graph,start):
    cost=[float('inf')]*len(graph)
    parents=[-1]*len(graph)
    cost[start]=0
    is_visited=[False]*len(graph)
    min_cost=0
    start_for_path=start
    while min_cost<float('inf'):
        is_visited[start]=True
        for i,vex in enumerate(graph[start]):
            if vex!=0 and not is_visited[i]:
                if cost[i]>cost[start]+vex:
                    cost[i] = cost[start] + vex
                    parents[i]=start
        min_cost=float('inf')
        for i in range(len(graph)):
            if min_cost>cost[i] and not is_visited[i]:
                min_cost=cost[i]
                start=i
    parents_list=[]
    for i in range(len(parents)):
        if parents[i]<0:
            parents_list.append([])

        else:
            j=i
            spam=deque([i])
            while parents[j]!=start_for_path:
                spam.appendleft(parents[j])
                j=parents[j]
            spam.appendleft(parents[j])
            parents_list.append(spam)
    return cost,parents_list
print(dej(graph,0))