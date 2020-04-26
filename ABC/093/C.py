#%%
abc = list(map(int, input().split()))

c = max(abc)
abc.remove(c)
a = abc[0]
b = abc[1]

#%%
d_ca = c - a
d_cb = c - b
if d_ca%2 == 0 and d_cb%2 == 0:
    ans = d_ca // 2 + d_cb // 2
elif d_ca%2 == 1 and d_cb%2 == 1:
    ans = d_ca // 2 + d_cb // 2 + 1
else:
    ans = d_ca // 2 + 1 + d_cb // 2 + 1

print(ans)