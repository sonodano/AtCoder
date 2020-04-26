#%%
x = int(input())

h = x // 100
r = x % 100

if r <= h*5:
    print(1)
else:
    print(0)
