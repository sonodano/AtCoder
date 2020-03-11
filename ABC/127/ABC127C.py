#%%
N, M = map(int, input().split())

maxL = 0
minR = float('inf')
for _ in range(M):
    l, r = map(int, input().split())
    maxL = max(maxL, l)
    minR = min(minR, r)


ans = minR - maxL + 1
ans = max(ans, 0)
print(ans)
