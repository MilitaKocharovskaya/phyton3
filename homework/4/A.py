def bfs(graph, vertex):
    color[vertex] = 1
    Q = [vertex]
    while Q:
        current = Q.pop(0)
        for neighbour in graph[current]:
            if color[neighbour] == 0:
                pred[neighbour] = current
                Q.append(neighbour)
            if color[neighbour] == 1:
                pred[neighbour] == current
                return pred

def vos(P, b):


res = []
path = []
vgraph = []
P = []
v, e = map(int, input().split())
color = [0] * v
pred = [[] for i in range(v)]
G = [[]for i in range(v)]
for i in range(e):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    if v1 not in vgraph:
        vgraph.append(v1)
    if v2 not in vgraph:
        vgraph.append(v2)
vgraph.sort()
print(G)
for i in vgraph:
    P = bfs(G, i)
    color = [0] * v
for i in P:
    if i != []:
        a = i
        break
if P == []:
    print('YES')
else:
    print(vos(P, a))



