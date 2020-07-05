#%%
N, C, K = map(int, input().split())
T = [int(input()) for i in range(N)]

T.sort()

cnt = 0
ans = 1
time = T[0]
for i in range(N-1):
    cnt += 1
    if cnt == C or time + K < T[i+1]:
        ans += 1
        cnt = 0
        time = T[i + 1]

print(ans)