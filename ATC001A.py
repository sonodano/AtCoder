#%%
# 深さ優先探索の練習問題
# TODO 要復習
# pythonだとデフォルトの再帰処理回数の上限に引っかかってしまうので変更（スタックを使えば回避できるらしい）
import sys
sys.setrecursionlimit(10000000)

H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

#%%
def dfs(y, x):
    d[y][x] = 1 # x, y地点は到達したので1にする.（行, 列） = （y軸方向, x軸方向）

    # 4方向をループ
    for a in actions:
        ny = y + a[0]
        nx = x + a[1]

        # 移動先（nx, ny）が街の範囲内か、行ったことがないか、塀ではないかを判定
        if 0 <= nx and nx < W and 0 <= ny and ny < H and d[ny][nx] == 0 and field[ny][nx] != '#':
            dfs(ny, nx)


# 到達したかどうかのマップ（0未到達, 1:到達）
d = [[0] * W for _ in range(H)]

# 移動方向
actions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 上下左右

# まずスタート位置を探す
for i in range(H):
    for j in range(W):
        if field[i][j] == 's':
            dfs(i, j) # スタートが見つかったらdfs開始

# 全部の探索が終わった後、ゴールに到達済みかどうかを判定
for i in range(H):
    for j in range(W):
        if field[i][j] == 'g' and d[i][j] == 1:
            print('Yes')
            sys.exit()

print('No')