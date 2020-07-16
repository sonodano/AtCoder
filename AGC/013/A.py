#%%
# TODO 要復習. 実装がよくわからなった
n = int(input())
A = list(map(int, input().split()))

#%%
up = False
down = False
ans = 1
base = A[0]

for i in range(1, n):
    if base < A[i]: # 単調増加のとき
        up = True
        base = A[i]
    elif base > A[i]: # 単調減少の時
        down = True

    # 切り替わるとき
    if (up == True) and (down == True):
        up = False
        down = False
        ans += 1
    base = A[i]

print(ans)
