def read_graph_as_list():
    n,m = map(int,input().split())
    graph = [[] for i in range(n)]
    for j in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def bfs(graph, start, vis = None):
    if vis is None:
        vis = set()
    vis.add(start)
    time = {start:0}
    Q = [start]
    while Q:
        current = Q.pop(0)
        for neighbour in graph[current]:
            if neighbour not in vis:
                vis.add(neighbour)
                Q.append(neighbour)
                print(current, neighbour)
                time[neighbour] = time[current] + 1
            else:
