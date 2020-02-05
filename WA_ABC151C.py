#%%
# TODO: 問題文読み間違えた
N, M = map(int, input().split())

ac = 0
wa = 0

hist_ac = [0] * N
hist_wa = [0] * N
for _ in range(M):
    p, s = input().split()
    p = int(p) - 1
    if hist_ac[p] == 0:
        if s == 'AC':
            hist_ac[p] = 1
            ac += 1
            wa += hist_wa[p]
        else:
            hist_wa[p] += 1

print(ac, wa)
