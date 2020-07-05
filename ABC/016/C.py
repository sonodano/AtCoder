#%%
#　まったくつながってない孤立している人を表示させるの忘れてた…
n, m = map(int, input().split())

friends = {}
for i in range(1, n+1):
    friends.setdefault(i, set())

for _ in range(m):
    # 友人関係を格納
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

#%%
for k in range(1, n+1):
    # ある人kの友人をあたっていく
    ans = set()
    for v in friends[k]: # kの友人vについて
        for f in friends[v]: # 友人vの友人fを探す
            if (f != k) and (k not in friends[f]): # v-kの関係じゃないかつ、kが友人vの友人fに含まれていないとき(k-fに関係がない)
                ans.add(f) # 1-7-5, 1-6-5のように重複する場合があるのでSetで持っておく

    print(len(ans))
