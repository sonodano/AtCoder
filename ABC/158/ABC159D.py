#%%
# TODO 要復習 よくわからんかった
s = input()
q = int(input())

for _ in range(q):
    t = list(input().split())
    if t[0] == '1':
        s = s[::-1]
    elif t[0] == '2':
        if t[1] == '1':
            s = t[2] + s
        else:
            s = s + t[2]

print(s)