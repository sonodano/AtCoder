#%%
from collections import Counter
n = int(input())
A = list(map(int, input().split()))

c = Counter(A)

ans = 0
for k in c.keys():
    tmp = c[k-1] + c[k] + c[k+1]
    ans = max(ans, tmp)

print(ans)