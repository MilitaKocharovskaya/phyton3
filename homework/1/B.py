def read_graph_as_lists():
    N = int(input())
    M = int(input())
    graph = [[] for i in range(N)]
    for edge in range (M):
        a,b = [int(x) for x in input().split()]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def dfs(vertex, graph, used=set()):
    used.add(vertex)
    for neighbour in graph [vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)

graph = read_graph_as_lists()
used = set()
number_of_components = 0
for vertex in range(len(graph)):
    if vertex not in used:
        dfs(vertex, graph, used)
        number_of_components += 1
print(number_of_components)