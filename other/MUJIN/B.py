#%%
import math
oa, ab, bc = map(int, input().split())
#%%
max_len = oa + ab + bc

if abs(ab - bc) < oa < (ab + bc):
    ans = math.pi * max_len ** 2
else:
    min_len = min([abs(eval('{}-{}+{}'.format(oa, ab, bc))),
                   abs(eval('{}+{}-{}'.format(oa, ab, bc))),
                   abs(eval('{}-{}-{}'.format(oa, ab, bc)))])
    ans = math.pi * (max_len ** 2 - min_len**2)

print(ans)