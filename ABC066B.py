#%%
S = input()

for _ in range(len(S)):
    S = S[:-1] # 末尾を削除
    if len(S) % 2 == 0:
        if S[:len(S)//2] == S[len(S)//2:]:
            ans = len(S)
            break

print(ans)