#%%
S = input()
T = input()

ans = 'No'
for _ in range(len(S)):
    if S == T:
        ans = 'Yes'
        break
    S = S[-1] + S[:-1]

print(ans)
