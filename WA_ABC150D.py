#%%
# TODO
# とけませんでした
N, M = map(int, input().split())
a_list = list(set(list(map(int, input().split()))))
rem = [int(0.5 * a) for a in a_list]
#%%
import sys
for a in a_list:
    if a % 2 != 0:
        print(0)
        sys.exit()

#%%

#%%
ans = 0

#%%
from sympy.ntheory import modular
print(modular.crt(a_list, rem))
