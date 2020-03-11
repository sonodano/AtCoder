#%%
r, D, x = map(int, input().split())


for _ in range(10):
    xn = r * x - D
    print(xn)
    x = xn