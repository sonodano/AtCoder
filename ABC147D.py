#%%
from itertools import combinations
N = input()
A = list(map(int, input().split()))

mod = 10e9+7
ans =sum([v[0]^v[1] for  v in combinations(A, 2)])
print(int(ans % mod))
