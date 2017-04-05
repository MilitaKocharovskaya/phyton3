def sort(vertex):
    if color[vertex] == 'GREY':
        return False
    if color[vertex] == 'BLACK':
        return True
    color[vertex] = 'GREY'
    for neighbour in G[vertex]:
        if not sort(neighbour):
            return False
    color[vertex] = 'BLACK'
    vsort.append(vertex)
    return True

vsort = []
v, e = map(int, input().split())
G = [[] for i in range(v)]
for i in range(e):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
color = [['WHITE'] for i in range(v)]
cycle = False
for V in range(v):
    if not sort(V):
        cycle = True
if cycle == True:
    print('NO')
else:
    vsort = vsort[::-1]
    print(*vsort)

