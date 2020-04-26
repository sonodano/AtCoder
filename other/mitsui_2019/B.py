#%%
import math
n = int(input())

x = int(n / 1.08)

# 小数点切り捨て処理が怖いから全部やったけど、一番上の条件だけで良い気がする
if math.floor(x*1.08) == n:
    print(x)
elif math.floor((x - 1) * 1.08) == n:
    print(x-1)
elif math.floor((x + 1) * 1.08) == n:
    print(x+1)
else:
    print(':(')

