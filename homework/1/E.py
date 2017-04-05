def read_graph_as_lists(N,M):
    graph = [[] for i in range(N)]
    for edge in range (M):
        a,b = [int(x) for x in input().split()]
        graph[a].append(b)
    return graph

def dfs(vertex, graph, used=set()):
    used.add(vertex)
    for neighbour in graph [vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)
    order.append(vertex)

def turn1(graph):
    graph_new = [[] for i in range(N)]
    for i in range(N):
        for j in graph [i]:
            graph_new[j].append(i)
    return graph_new

def turn2(order):
    order_new = [0]*len(order)
    for i in range (len(order)):
        order_new [len(order)-i-1] = order[i]
    return order_new

def no_orient_to_orient (graph,N):
    graph_no_orient = [[] for i in range(N)]
    for i in range(N):
        for j in graph[i]:
            graph_no_orient[j].append(i)
            graph_no_orient[i].append(j)
    return graph_no_orient


N = int(input())
M = int(input())
graph = read_graph_as_lists(N,M)
used = set()
l = 0
order = []
for vertex in range(len(graph)):
    if vertex not in used:
        dfs(vertex, graph, used)
graph_new = turn1(graph)
order_new = turn2(order)
used_new = set()
for vertex in order_new:
    if vertex not in used_new:
        dfs(vertex, graph_new, used_new)
        l += 1
graph_no_orient = no_orient_to_orient(graph,N)
used = set()
number_of_components = 0
for vertex in range(len(graph_no_orient)):
    if vertex not in used:
        dfs(vertex, graph_no_orient, used)
        number_of_components += 1
print(number_of_components,l)