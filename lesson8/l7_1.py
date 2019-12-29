#1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям
# (по одному разу). Сколько рукопожатий было?
def create_graph(n):
    graph=[]
    for i in range(n):
        spam=[]
        for j in range(n):
            if i!=j:
                spam.append(1)
            else:
                spam.append(0)
        graph.append(spam)
    return graph
def shakes(graph):
    shakes=[]
    shakes_count=0
    for i in range(len(graph)):
        for n,shake in enumerate(graph[i]):
            if (not n in shakes) and shake==1:

                shakes_count+=1
        shakes.append(i)
    return shakes_count


n=int(input('Введите количество людей:'))
print(shakes(create_graph(n)))