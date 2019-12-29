# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


def simm_graph(n):
    return {i: {j for j in range(n) if i != j} for i in range(n)}


company = int(input('Введите кол-во друзей: '))
friends = simm_graph(company)

for k, v in friends.items():
    print(k, v)

shake_number = 0
for shakes in friends.values():
    shake_number += len(shakes)

print(f'{company} друзей пожали руки {int(shake_number / 2)} раз(а)')
