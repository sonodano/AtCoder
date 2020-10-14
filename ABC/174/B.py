#%%
n, d = map(int, input().split())
ans = 0
d2 = d**2
for i in range(n):
    p, q = map(int, input().split())
    x2 = p**2 + q**2
    if x2 <= d2:
        ans += 1

print(ans)