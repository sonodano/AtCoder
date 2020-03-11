#%%
# 深さ優先探索の例題
# TODO: 要復習
# https://qiita.com/drken/items/e77685614f3c6bf86f44#%E4%BE%8B%E9%A1%8C-2-1-1%E9%83%A8%E5%88%86%E5%92%8C%E5%95%8F%E9%A1%8C
N = int(input())
t = [int(input()) for _ in range(N)]

def dfs(i, a, b):
    global ans
    if i == N: # 全部の肉を乗せ終わったら
        ans = min(ans, max(a, b)) # 現在のansと, 探索してきたa, bのうち大きい方との最小値で更新
    else:
        dfs(i+1, a + t[i], b) # aの肉焼き器に乗せる場合
        dfs(i+1, a, b + t[i]) # bの肉焼き器に乗せる場合

ans = float('inf')
dfs(0, 0, 0)
print(ans)

#%%
# bit全探索
# 再帰よりやっぱbitの方がわかりやすい…
N = int(input())
t = [int(input()) for _ in range(N)]
ans = float('inf')

for bit in range(1 << N):
    a = 0
    b = 0
    for i in range(N):
        # フラグが立っていればaに、たってなければbに乗せる
        if bit & (1 << i):
            a += t[i]
        else:
            b += t[i]
    ans = min(ans, max(a, b))

print(ans)