v, e = map(int, input().split())
w = [[0 for j in range(v)] for i in range(v)]
for i in range(e):
    v1, v2, weight = map(int, input().split())
    w[v1][v2] = weight
    w[v2][v1] = weight
print(w)
inf = 10**9
dist = [inf for i in range(v)]
dist[0] = 0
used = [[False]for i in range(v)]
used[0] = True
tree = []
tree_weight = 0
u = 0
for i in range(v):
    min_d = inf
    for j in range(v):
        if not used[j] and dist[j] < min_d:
            min_d = dist[j]
            u = j
    tree.append((i, u))
    tree_weight += w[i][u]
    used[u] = True
    for k in range(v):
        dist[k] = min(dist[k], w[u][k])
print(tree_weight)
for l in tree:
    print(tree)