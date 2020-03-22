#%%
n, x = map(int, input().split())

if x <= n//2:
    ans = x - 1
else:
    ans = n - x

print(ans)