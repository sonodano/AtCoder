#%%
x, t = map(int, input().split())

ans = x - t
if ans <= 0:
    print(0)
else:
    print(ans)