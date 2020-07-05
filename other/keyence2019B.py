#%%
S = input()


ans = False
for i in range(len(S)):
    for j in range(i, len(S)):
        moji = S[:i] + S[j:]
        if moji == 'keyence':
            ans = True
            break

if ans:
    print('YES')
else:
    print('NO')

