#%%
N, A, B, C, D = map(int, input().split())
S = input()


#%%
flag = True
# A -> Cの間に#が二連続するパターン
if '##' in S[A-1:C]:
    flag = False
# B -> Dの間に#が二連続するパターン
if '##' in S[B-1:D]:
    flag = False

# A, Bの位置交換が必要な時
if C > D:
    if '...' not in S[B-2:D+1]:
    # B,Dの間に連続する3つの'.'が必要
        flag = False

if flag:
    print('Yes')
else:
    print('No')
