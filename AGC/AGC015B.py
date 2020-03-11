#%%
S = input()

ans = 0
for i in range(len(S)):
    if S[i] == 'U':
        ans += len(S[i+1:]) + 2 * len(S[:i])
    elif S[i] == 'D':
        ans +=  2 * len(S[i+1:]) + len(S[:i])

print(ans)
