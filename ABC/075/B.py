#%%
import itertools
h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]

#%%
mine = [['#' for _ in range(w)] for __ in range(h)]

def counter(i, j):
    if (0 <= i <= h-1) and (0 <= j <=w-1):
        if field[i][j] == '#':
            return 1
        else:
            return 0
    else:
        return 0

for i in range(h):
    for j in range(w):
        cnt = 0
        if field[i][j] == '#':
            mine[i][j] = '#'
        else:
            for k, l in itertools.product([i-1, i, i+1], [j-1, j, j+1]):
                cnt += counter(k, l)
            mine[i][j] = cnt

#%%
for m in mine:
    print(''.join(map(str, m)))
