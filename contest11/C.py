def zf(s):
    c = []
    if not s:
        return c
    i, l = len(a), len(s)
    while i < l:
        left, right = 0, i
        while right < l and left < len(a) and s[left] == s[right]:
            left += 1
            right += 1
        c.append(left)
        i += 1
    return c

a = input()
b = input()
s = a + b
d = []
k = 0
z = zf(s)
for i in range(len(z)):
    if z[i] == len(a):
        d.append(i)
        k += 1
if k == 0:
    d = [-1]
print(*d)