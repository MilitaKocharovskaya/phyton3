def zf(s):
     a = []
     if not s:
         return a
     i, l = 1, len(s)
     a.append(0)
     while i < l:
         left, right = 0, i
         while right < l and s[left] == s[right]:
             left += 1
             right += 1
         a.append(left)
         i += 1
     return a

s = input()
print(*zf(s))