#%%
#K, S = 5, 15
K, S = map(int, input().split())

ans = 0
for x in range(K+1):
    for y in range(K+1):
            z = S - x - y
            if K >= S - x - y and z >= 0:
                ans += 1

print(ans)