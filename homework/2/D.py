n, m = map(int, input().split())
start = tuple(map(int, input().split()))
finish = tuple(map(int, input().split()))
field = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    row = input()
    for j in range(m):
        if row[j] == 'X':
            field[i][j] = -1
        else:
            field[i][j] = 0
si, sj = start
field[si][sj] = 0
queue = [(si, sj)]
while queue:
    ci, cj = queue.pop(0)
    if cj > 0 and field[ci][cj - 1] == 0:
        queue.append((ci, cj - 1))
        field[ci][cj - 1] = field[ci][cj] + 1
    if cj < m - 1 and field[ci][cj + 1] == 0:
        queue.append((ci, cj + 1))
        field[ci][cj + 1] = field[ci][cj] + 1
    if ci > 0 and field[ci - 1][cj] == 0:
        queue.append((ci - 1, cj))
        field[ci - 1][cj] = field[ci][cj] + 1
    if ci < n - 1 and field[ci + 1][cj] == 0:
        queue.append((ci + 1, cj))
        field[ci + 1][cj] = field[ci][cj] + 1
fi, fj = finish
if field[fi][fj] < 1:
    print('INF')
else:
    print(field[fi][fj])
