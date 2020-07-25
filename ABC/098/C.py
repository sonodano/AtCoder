#%%
n = int(input())
S = input()

ans = S.count('E')

w = 0
tmp_w = 0
e = ans

for s in S:
    if s == 'E':
        e -= 1
    else:
        tmp_w += 1 # わざわざtmp_wつくらなくても、ansの計算のあとにWの判別すればよかった

    ans = min(ans, w+e)
    w = tmp_w

print(ans)

#%% 正攻法は累積和で解くらしい？
# https://qiita.com/IGMML/items/5aa36f7fa03746ed6e6c
n = int(input())
S = input()
int_s = [0] * n
cumsum_w = [0] * (n + 1)
cumsum_e = [0] * (n + 1)
answers = [0] * n

for i in range(n):
    if S[i] == 'W':
        int_s[i] = 1
    else:
        int_s[i] = 0
    cumsum_w[i+1] = cumsum_w[i] + int_s[i]

for i in range(n):
    if S[i] == 'E':
        int_s[i] = 1
    else:
        int_s[i] = 0
    cumsum_e[i+1] = cumsum_e[i] + int_s[i]

for i in range(n):
    answers[i] = cumsum_w[i] + (cumsum_e[n] - cumsum_e[i+1]) # i番目までのWの数 + （全部のEの数 - i+1番目以降のEの数）

print(min(answers))