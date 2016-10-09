n = int(input())
s = input().split()
m = []
d = 0
m1 = 0
for i in range(n):
    s[i] = int(s[i])
for i in range(n):
    if s[i] == 5:
        m.append(1)
    else:
        m.append(-s[i]//5 + 1)
for i in range(n):
    m1 = m1 + m[i]
    if d > m1:
        d = m1
if d < 0:
    print(abs(d))
else:
    print(0)