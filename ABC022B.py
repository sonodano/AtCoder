#%%
N = int(input())

A = [int(input()) for _ in range(N)]

ans = N - len(set(A))
print(ans)