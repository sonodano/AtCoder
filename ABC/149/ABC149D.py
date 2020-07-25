#%%
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

#%%
ans = 0

def rps(t):
    if t == 'r':
        return P
    if t == 'p':
        return S
    if t == 's':
        return R

for n in range(N):
    if n < K:
        ans += rps(T[n])
        continue

    score_n = rps(T[n])
    if T[n] == T[n-K]:
        score_k = rps(T[])