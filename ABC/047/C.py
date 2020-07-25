#%%
S = input()

current = S[0]
ans = 0
for s in S:
    if s != current:
        ans += 1
        current = s

print(ans)