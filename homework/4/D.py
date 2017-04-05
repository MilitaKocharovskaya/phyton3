def hamilton(current):
    path.append(current)
    if len(path) == v:
        if path[-1] in G[path[0]]:
            return path
        else:
            path.pop()
            return False
    visited[current] = True
    for next in range(v):
        if next in G[current] and not visited[next]:
            if hamilton(next):
                return path
    visited[current] = False
    path.pop()
    return False

path = []
v, e = map(int, input().split())
G = [[] for i in range(v)]
visited = [False]*v
for i in range(e):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)
print(*hamilton(0))