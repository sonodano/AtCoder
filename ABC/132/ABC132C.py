#%%
N = int(input())
ds = list(map(int, input().split()))

ds.sort()
print(ds[N//2] - ds[N//2 - 1])

