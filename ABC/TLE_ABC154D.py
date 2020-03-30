#%%
# TODO 愚直にforループを回してTLEした
#  区間和を高速に求める方法を知らなかった
#  累積和を使うらしい
# https://qiita.com/drken/items/18b3b3db5735241465ef
# https://paiza.hatenablog.com/entry/2015/01/21/%E3%80%90%E7%B4%AF%E7%A9%8D%E5%92%8C%E3%80%81%E3%81%97%E3%82%83%E3%81%8F%E3%81%A8%E3%82%8A%E6%B3%95%E3%80%91%E5%88%9D%E7%B4%9A%E8%80%85%E3%81%A7%E3%82%82%E8%A7%A3%E3%82%8B%E3%82%A2%E3%83%AB%E3%82%B4

import numpy as np

N, K = map(int, input().split())
E = list(map(lambda x: (int(x)+1)/2, input().split()))
E_cumsum = np.cumsum(E)

ans = E_cumsum[K-1]
for i in range(0, N-K):
    e = E_cumsum[i+K] - E_cumsum[i]
    ans = max(ans, e)
print(ans)

