from heapq import *
def dijkstra1(A, start):
    d = [float('+inf') for v in A]
    d[start] = 0
    path = [None]*n
    used = [False]*n
    min_d = 0
    while min_d < float('+inf'):
        current = start
        used[current] = True
        for neighbour in A[current]:
            l = d[current] + neighbour[1]
            if l < d[neighbour[0]]:
                d[neighbour[0]] = l
                path[neighbour[0]] = current
        min_d = float('+inf')
        for current in range(n):
            if not used[current] and d[current] < min_d:
                start = current
                min_d = d[current]
    return path

n, m, x, y = map(int, input().split())
a = [[] for i in range(n)]
for j in range(m):
    v1, v2, w = map(int, input().split())
    a[v1].append([v2, w])
    a[v2].append([v1, w])
p = dijkstra1(a, x)
p1 = []
i = y
while i is not None:
    p1.append(i)
    i = p[i]
p1 = p1[::-1]
print(*p1)
