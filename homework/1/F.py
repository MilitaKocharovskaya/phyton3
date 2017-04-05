def g(N):
    for i in range(N):
        st = input().split()
        for j in range(N):
            st[j] = int(st[j])
            if st[j] != 0:
                print(i,j,st[j])

N = int(input())
graph = g(N)