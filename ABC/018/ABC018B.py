#%%
S = list(input())
N = int(input())

for _ in range(N):
    l, r = map(int, input().split())
    rev_S = list(reversed(S[l-1:r]))
    S[l-1:r] = rev_S

print(''.join(S))

#%%
# ちょっとスマート　https://atcoder.jp/contests/abc018/submissions/9350701
S = list(input())
N = int(input())
for _ in range(N):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    S[l:r + 1] = list(reversed(S[l:r + 1]))
print(''.join(S))