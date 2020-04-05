#%%
from collections import Counter
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n = int(input())
anas = [''.join(sorted(input())) for _ in range(n)]
c = Counter(anas)


cnt = 0
for v in c.values():
    if v < 2:
        continue
    else:
        cnt += cmb(v, 2)

print(cnt)
