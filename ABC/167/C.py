#%%
import itertools
n, m, x = map(int, input().split())
refs = [list(map(int, input().split())) for _ in range(n)]

#%%
# n個のbit組み合わせ
flag = True
for bits in itertools.product([1, 0], repeat=n):
    skill = [0] * m # スキルは毎回初期化して良い
    cost = 0
    if all(bits):
        for r in refs:
            skill = [x + y for (x, y) in zip(skill, r[1:])]
            cost += r[0]
        if any([i < x for i in skill]): # 全部足してもだめなとき
            flag = False
            break
        else:
            ans = cost # 最大のコスト

    else:
        for i, b in enumerate(bits):
            if b == 1:
                skill = [x + y for (x, y) in zip(skill, refs[i][1:])]
                cost += refs[i][0]
        if all([i >= x for i in skill]):
            ans = min(ans, cost)

if flag:
    print(ans)
else:
    print(-1)