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
w = [[[0] for j in range(v)] for i in range(v)]
result = {}
visited = [False] * v
for i in range(e):
    v1, v2, weight = map(int, input().split())
    w[v1][v2] = weight
    w[v2][v1] = weight
    G[v1].append(v2)
    G[v2].append(v1)
for i in range(v):
    d = hamilton(i)
    s = 0
    s += w[path[-1]][path[0]]
    for j in range(v-1):
        s += w[d[j]][d[j + 1]]
    result.update({s: d})
    visited = [False] * v
    path = []
k = min(result.keys())
print(k)
print(*result[k])