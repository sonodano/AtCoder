#%%
N, A, B = map(int, input().split())

ans = (N - 2) * B - (N - 2) * A + 1
ans = max(ans, 0)
print(ans)