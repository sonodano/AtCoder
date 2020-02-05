#%%
N, S, T = map(int, input().split())
W = 0

ans = 0
for _ in range(N):
    W += int(input())
    if S <= W <=T:
        ans += 1

print(ans)
