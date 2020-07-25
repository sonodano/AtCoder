#%%
import math
n, m = map(int, input().split())
R = 1000000007

if abs(n - m) >= 2:
    ans = 0
else:
    nf = math.factorial(n)
    mf = math.factorial(m)
    if n == m:
        ans = (nf * mf * 2) % R
    else:
        ans = (nf * mf) % R

print(ans)