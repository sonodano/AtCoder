#%%
import numpy as np
import itertools

h, w, k = map(int, input().split())
field = [list(input()) for _ in range(h)]
npfield = np.array(field)
#%%
ans = 0
for i in itertools.product([False, True], repeat=h):
    for j in itertools.product([False, True], repeat=w):
        cnt = np.count_nonzero(npfield[np.ix_(i, j)] == '#')
        if cnt == k:
            ans += 1

print(ans)