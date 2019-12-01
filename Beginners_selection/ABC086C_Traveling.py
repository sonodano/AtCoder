#%%
import sys

N = int(input())

t0, x0, y0 = 0, 0, 0
for n in range(N):
    t, x, y = map(int, input().split())
    dt = t - t0
    l1 = abs(x - x0) + abs(y - y0)
    if (l1 > dt) or (dt % 2 != l1 %2):
        print('No')
        sys.exit(0)
    t0, x0, y0 = t, x, y

print('Yes')
