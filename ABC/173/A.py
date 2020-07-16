#%%
n = int(input())

if n % 1000 == 0:
    print(0)
else:
    ans = 1000 * (n // 1000 + 1) - n
    print(ans)