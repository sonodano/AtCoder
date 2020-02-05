#%%
# TODO
# https://qiita.com/saba/items/affc94740aff117d2ca9
# 再帰で書く
D, G = 2, 700#map(int, input().split())
pc = [[3, 500], [5, 800]]#[list(map(int, input().split())) for _ in range(D)]

def dfs(i, sum, count, nokori):
    global ans
    if i == D:
        # G点に満たなければ、nokoriのうち一番大きいものを解く
        if sum < G:
            use = max(nokori)
            # 解く問題が問題数を超えないように注意
            # pythonの割り算の切り捨て→4 // 3、切り上げ→-(-4 // 3)
            print(pc[use - 1][0], -(-(G-sum) // (use*100)))
            n = min(pc[use - 1][0], -(-(G-sum) // (use*100))) # min(useで指定する問題数, 残り必要な点数/指定した問題の得点（切り上げ）)
            count += n
            sum += n * use * 100

        if sum >= G:
            ans = min(ans, count)

    else:
        # 総合スコア、解いた問題数、まだ解いていない問題を更新
        dfs(i + 1, sum, count, nokori)
        dfs(i + 1, sum + pc[i][0] * (i+1) * 100 + pc[i][1], count + pc[i][0], nokori - {i+1}) #←ここがわからん！

ans = float('inf')

dfs(0, 0, 0, set(range(1, D+1)))
print(ans)

#%%
print(set(range(1, D + 1)))