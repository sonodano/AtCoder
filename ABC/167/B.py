#%%
a, b, c, k = map(int, input().split())

if k <= a:
    ans = k
else:
    if k <= a + b:
        ans = a
    else:
        ans = a - (k - (a + b))

print(ans)