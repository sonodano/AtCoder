#%%
n, m = map(int, input().split())

route = {}
for _ in range(m):
    a, b = map(int, input().split())
    route.setdefault(a, []).append(b)

#%%
flag = False
for r1 in route[1]:
    if n in route.get(r1, []):
        flag = True
        break

if flag:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
