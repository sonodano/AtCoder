#%%
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

#%%
d = defaultdict(lambda: 0)
for key in A:
    d[key] += 1

#%%
# それぞれのkeyのnC2
cmb = dict()
cmb2 = dict()
for k in d.keys():
    cmb[k] = d[k] * (d[k] - 1) // 2
    cmb2[k] = (d[k] - 1) * (d[k] - 2) // 2

#%%
ans_d = dict()
s = sum(cmb.values())
for k in d.keys():
    ans_d[k] = s - cmb[k] + cmb2[k]
# わざわざこんなことしなくても、n*(n-1)//2 - (n-1)*(n-2)//2 = n - 1 でした
#%%
for a in A:
    print(ans_d[a])

#%%
# もっときれいな書き方
# https://atcoder.jp/contests/abc159/submissions/15132450
from collections import Counter
n = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

ans = 0
for v in cnt.values():
    ans += v * (v - 1) // 2

for k in A:
    # n*(n-1)//2 - (n-1)*(n-2)//2 = n - 1
    print(ans - (cnt[k] - 1))
