# https://atcoder.jp/contests/arc051/tasks/arc051_a
# アカウント: sonodano

#%%
x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

#%%
# 円のなかに四角が覆われしまうパターン
# 第一象限内
import math
# コメント: sqrtじゃなくて、両辺二乗して比較したほうがよい（計算誤差
if math.sqrt((x3 - x1)**2 + (y3 - y1)**2) <= r and\
        math.sqrt((x1 - x2)**2 + (y3 - y1)**2) <= r and \
        math.sqrt((x1 - x2) ** 2 + (y2 - y1) ** 2) <= r and \
        math.sqrt((x3 - x1)**2 + (y2 - y1)**2) <= r:
    print('YES')
    print('NO')
# 四角の中に円が覆われしまうパターン
elif (x1 + r) <= x3 and (x1 - r) >= x2 and (y1 + r) <= y3 and (y1 - r) >= y2:
    print('NO')
    print('YES')
else:
    print('YES')
    print('YES')