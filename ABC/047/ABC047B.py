#%%
W, H, N = map(int, input().split())


# x, y軸を作る
w = [1] * (W)
h = [1] * (H)

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        w[:x] = [0] * x
    elif a == 2:
        w[x:] = [0] * (H - x)
    elif a == 3:
        h[:y] = [0] * y
    elif a == 4:
        h[y:] = [0] * (H - y)

ans = sum(w) * sum(h)
print(ans)


#%%
