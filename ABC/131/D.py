#%%
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

#%%
ab = sorted(ab, key=lambda x: x[1]) # 締め切りが近い順に並び替える
flag = True

cost = 0
for a, b in ab:
    cost += a
    if cost > b: # 締め切り時刻を超えたときに打ち切る
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')