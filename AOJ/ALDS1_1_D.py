#%%
n = int(input())

min_r = int(input())
maxv = -float('inf')

for _ in range(n-1):
    r = int(input())
    maxv = max(maxv, r - min_r)
    min_r = min(min_r, r)

print(maxv)