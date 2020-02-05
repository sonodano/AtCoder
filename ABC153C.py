#%%
N, K = map(int, input().split())
H = list(map(int, input().split()))


H.sort()
if len(H) <= K:
    ans = 0
elif K == 0:
    ans = sum(H)
else:
    H = H[:-K]
    ans = sum(H)

print(ans)