#%%
S = input()


idx_w = 0
idxes_b = []

for i, s in enumerate(S):
    if s == 'B':
        idxes_b.append(i)
    elif s == 'W':
        idx_w = i

idxes_b = [b for b in idxes_b if idx_w > b] # BBWBB; W以降のものは使えない

ans = 0
for i, b in enumerate(idxes_b[::-1]):
    ans += idx_w - b - i

print(max(0, ans))

#%%
# かしこい
# https://atcoder.jp/contests/agc029/submissions/14863233
s = input()
ans = 0
B = 0
for x in s:
    if x == 'B':
        B += 1
    else:
        ans += B
print(ans)
