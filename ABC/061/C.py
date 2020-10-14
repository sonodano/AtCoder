#%%
from collections import defaultdict
n, k = map(int, input().split())

#%%
d = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split())
    d[a] += b

#%%
cnt = 0
for i in sorted(d.keys()):
    v = d[i]
    cnt += v
    if k <= cnt:
        ans = i
        break

print(ans)