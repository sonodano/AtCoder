#%%
# あんまり賢くない
from collections import defaultdict

n = int(input())

d = defaultdict(list)
for i in range(n):
    k, v = input().split()
    v = int(v)
    d[k].append([v, i+1])

#%%
ks = sorted(d.keys())
for k in ks:
    vs = d[k]
    score_d = {}
    for v in vs:
        score_d[v[0]] = v[1]

    score_keys = sorted(score_d.keys(), reverse=True)
    for sk in score_keys:
        print(score_d[sk])

#%%
# 賢い解法
# https://atcoder.jp/contests/abc128/submissions/11699167

n = int(input())
x = []
for i in range(n):
    s, p = input().split()
    x.append((s, 100 - int(p), i+1))
x = sorted(x) # sortの方向を揃える（s, p）とよしなにソートしてくれるっぽい
for xx in x:
    print(xx[2])
