#%%
N, M = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(M)]

ans = []
for n in range(1, N+1):
    count = 0
    for i in range(M):
        for j in range(2):
            if ab[i][j] == n:
                count += 1
    ans.append(count)


for a in ans:
    print(a)

#%% もうちょっとスマート
n, m = map(int, input().split())
ans = [0] * n
l = []
for i in range(m):
    a, b = map(int, input().split())
    l.append(a)
    l.append(b)

import collections

c = collections.Counter(l)

for k, v in c.items():
    ans[k - 1] += v

for i in ans:
    print(i)