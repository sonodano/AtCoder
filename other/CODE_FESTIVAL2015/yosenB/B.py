#%%
from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = Counter(a)

ans = c.most_common()[0]
if ans[1] > n/2:
    print(ans[0])
else:
    print('?')