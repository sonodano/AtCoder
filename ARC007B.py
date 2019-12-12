#%%
N, M = map(int, input().split())

cases = list(range(1, N+1))
cd = 0

for _ in range(M):
    d = int(input())
    try:
        idx = cases.index(d)
        cases[idx] = cd
    except:
        pass
    cd = d

for i in cases:
    print(i)
