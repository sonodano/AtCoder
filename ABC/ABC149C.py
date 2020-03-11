#%%
# 参考：http://szarny.hatenablog.com/entry/2017/09/21/232855#%E3%81%94%E3%82%8A%E6%8A%BC%E3%81%97%E5%88%A4%E5%AE%9A%E6%B3%95
X = int(input())

import math
def using_sqrt(x):
    n = 0
    for k in range(x, 1000000):
        factor = 0

        # 2以外の偶数は素数ではないので無視する
        if k % 2 == 0 and k != 2:
            continue

        # 繰り返しの上限を対象の平方根にする
        for divisor in range(2, math.floor(math.sqrt(k)) + 1):
            if k % divisor == 0:
                factor += 1

        if factor == 0:
            #n += 1
            ans = k
            break

    return ans

ans = using_sqrt(X)
print(ans)