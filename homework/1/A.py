def read_graph_as_lists(N,M):
    graph = [[] for i in range(N)]
    for edge in range (M):
        a,b = [int(x) for x in input().split()]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def chet(graph, N):
    l = 1
    for i in range(N):
        k = 0
        for j in graph[i]:
            k += 1
        if k %2 != 0:
            l = 0
    return l

def dfs(vertex, graph, used=set()):
    used.add(vertex)
    for neighbour in graph [vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)

N = int(input())
M = int(input())
graph = read_graph_as_lists(N,M)
used = set()
number_of_components = 0
for vertex in range(len(graph)):
    if vertex not in used:
        dfs(vertex, graph, used)
        number_of_components += 1
n = chet(graph, N)
if (number_of_components == 1) and (n == 1):
    print('YES')
else:
    print('NO')
