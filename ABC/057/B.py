from scipy.spatial.distance import cdist
import numpy as np
#%%
# ずる
n, m = map(int, input().split())

st = [list(map(int, input().split())) for _ in range(n)]
cp = [list(map(int, input().split())) for _ in range(m)]

cd = cdist(st, cp, 'cityblock')
idxes = np.argmin(cd, axis=1)
for i in idxes:
    print(i+1)

#%%
# scipyなし
n, m = map(int, input().split())

st = [list(map(int, input().split())) for _ in range(n)]
cp = [list(map(int, input().split())) for _ in range(m)]

for s in st:
    mandist = float('inf')
    for i, c in enumerate(cp):
        d = abs(s[0] - c[0]) + abs(s[1] - c[1])
        if d < mandist:
            ans_check = i + 1
            mandist = d
    print(ans_check)