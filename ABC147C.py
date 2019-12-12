#%%

N = int(input())

A = []
xy = []

for i in range(N):
    A.append(int(input()))
    for j in range(A[i]):
        xy.append(list(map(int, input().split())))

#%%
# y = 0: 嘘つき
# y = 1: 正直
# ビット全探索
#  n 個の選択肢それぞれに Yes or No の二択があるが、その部分集合（選択できるパターン）の全てを網羅的にチェックしたい

ans = 0
for i in range(2**N):
    bit_list = []
    for j in range(N):
        if ((i >> j) & 1):
            bit_list.append(1)
        else:
            bit_list.append(0)