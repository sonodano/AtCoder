#%%
S = input()

#%% コードが汚いぜよ...
n = len(S)
ans = [0] * n
r = 0 # ...RL|の数
l = 0 # RL|L...の数
flag_L = False
for i, s in enumerate(S):
    if (flag_L is False) and (s == 'R'): # Rの数を数えていくとき
        r += 1
    elif (flag_L is False) and (s == 'L'): # ...RRL に達したとき
        r += 1
        idx = i
        ans[idx] += r - r // 2
        ans[idx-1] += r // 2
        r = 0
        flag_L = True
    elif (flag_L is True) and (s == 'L'): # RL|LL....のとき
        l += 1
        if i == n-1: # 終端は必ずL
            ans[idx] += l//2
            ans[idx-1] += l - l//2
    else: # RL|L...L|Rに達したとき
        ans[idx] += l // 2 # idxは先に必ず決まる
        ans[idx-1] += l - l//2
        r += 1
        l = 0
        flag_L = False

print(' '.join(map(str, ans)))

#%%
# きれいなコード https://qiita.com/Kept1994/items/e9179d1dd7c6455d6883
# ランレングス圧縮を使う
from itertools import groupby

# ランレングス圧縮.  groupbyを使うと楽に書ける
def rfe_tuple(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, str(len(list(v)))))
    return res

n = len(S)
now = 0
compressed = rfe_tuple(S)
ans = [0] * n
for lr, i in compressed:
    i = int(i)
    if lr == 'R':
        now += 1
        ans[now-1] += i - i // 2
        ans[now] += i // 2
    else:
        ans[now-1] += i // 2
        ans[now] += i - i // 2
        now += i

print(' '.join(map(str, ans)))
