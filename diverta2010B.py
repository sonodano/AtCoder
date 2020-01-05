#%%
R, G, B, N = map(int, input().split())

count = 0
ans = 0
for r in range(0, N+1, R):
    for g in range(0, N+1-r, G):
        rg = r + g
        if rg == N or (N - rg) % B == 0:
            ans += 1
            count = 0

print(ans)
