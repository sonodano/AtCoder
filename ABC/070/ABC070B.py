#%%
# 賢くない
a, b, c, d = map(int, input().split())

alice = list(range(a, b+1))
bob = list(range(c, d+1))

ans = 0
for a in alice:
    if a in bob:
        ans += 1
if ans != 0:
    print(ans - 1)
else:
    print(0)

#%%
# 賢い
ans = max(0, min(b, d) - max(a, c))
print(ans)