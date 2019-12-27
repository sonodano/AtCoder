#%%
D, N = map(int, input().split())

if N == 100:
    N += 1
ans = 100**D * N
print(ans)