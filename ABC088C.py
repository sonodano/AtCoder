#%%
C = [list(map(int, input().split())) for _ in range(3)]


import sys
min_a1 = min(C[0])
min_a2 = min(C[1])
min_a3 = min(C[2])

for a1 in range(min_a1+1):
    b1_a1 = C[0][0] - a1
    b2_a1 = C[0][1] - a1
    b3_a1 = C[0][2] - a1
    for a2 in range(min_a2+1):
        b1_a2 = C[1][0] - a2
        b2_a2 = C[1][1] - a2
        b3_a2 = C[1][2] - a2
        for a3 in range(min_a3+1):
            b1_a3 = C[2][0] - a3
            b2_a3 = C[2][1] - a3
            b3_a3 = C[2][2] - a3

            if b1_a1 == b1_a2 == b1_a3 and b2_a1 == b2_a2 == b2_a3 and b3_a1 == b3_a2 == b3_a3:
                print('Yes')
                sys.exit()

print('No')

#%%
# 別解
#  c11 = a1 + b1, c22 = a2 + b2, ...って感じなので, 対角成分の和が等しくなるかを確認する
# https://atcoder.jp/contests/abc088/submissions/9309736

f = []
for i in range(3):
    f.append(list(map(int, input().split())))
"""
a1+a2+a3+b1+b2+b3が3通りで合うか
"""
s1 = f[0][0] + f[1][1] + f[2][2]
s2 = f[0][1] + f[1][2] + f[2][0]
s3 = f[0][2] + f[1][0] + f[2][1]

if s1 == s2 == s3:
    print("Yes")
else:
    print("No")

#%%
# 別解2
# numpy を使う
# https://yamakasa.net/atcoder-abc-088-c/

import numpy as np

c = [list(map(int, input().split())) for i in range(3)]

A = np.array([
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1]])

B = np.array([
    [1, 0, 0, 1, 0, 0, c[0][0]],
    [1, 0, 0, 0, 1, 0, c[0][1]],
    [1, 0, 0, 0, 0, 1, c[0][2]],
    [0, 1, 0, 1, 0, 0, c[1][0]],
    [0, 1, 0, 0, 1, 0, c[1][1]],
    [0, 1, 0, 0, 0, 1, c[1][2]],
    [0, 0, 1, 1, 0, 0, c[2][0]],
    [0, 0, 1, 0, 1, 0, c[2][1]],
    [0, 0, 1, 0, 0, 1, c[2][2]]])

# Ax = bが解を持つためには、係数行列Aと拡大係数行列(A|b)のランクが一致（逆行列が存在）
rankA = np.linalg.matrix_rank(A)
rankB = np.linalg.matrix_rank(B)

if rankA == rankB:
    print("Yes")
else:
    print("No")