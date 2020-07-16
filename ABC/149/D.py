#%%
# DPでもとけるらしいが…？
n, k = map(int, input().split())
r, s, p = map(int, input().split())
T = input()

#%%
win = []
for t in T:
    if t == 'r':
        win.append('p')
    elif t == 'p':
        win.append('s')
    elif t == 's':
        win.append('r')


def score(rps):
    if rps == 'r':
        return r
    elif rps == 'p':
        return p
    elif rps == 's':
        return s

ans = 0
for i in range(n):
    if i - k < 0:
       ans += score(win[i])
    else:
        if win[i] == win[i-k]:
            win[i] = None
        else:
            ans += score(win[i])

print(ans)
