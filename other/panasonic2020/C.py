#%%
a, b, c = map(int, input().split())

if  (c - a - b) >= 0 and 4 * a * b < (c - a - b)**2:
    print('Yes')
else:
    print('No')

#%%
# 普通にsqrtを使うと、誤差によって大小関係がおかしくなる。
# Decimalを使う. ちょっとおそい
from decimal import Decimal

a, b, c = map(int, input().split())
if Decimal(a).sqrt() + Decimal(b).sqrt() < Decimal(c).sqrt():
    print('Yes')
else:
    print('No')