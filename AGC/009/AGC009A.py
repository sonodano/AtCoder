#%%
n = int(input())

a_l = []
b_l = []
for _ in range(n):
    _a, _b = map(int, input().split())
    a_l.append(_a)
    b_l.append(_b)

#%%
cnt = 0
for a, b in zip(a_l[::-1], b_l[::-1]):
    m = (a + cnt) % b
    if m == 0:
        continue
    else:
        cnt += b - m

print(cnt)
