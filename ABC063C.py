#%%
N = int(input())

S = [int(input()) for _ in range(N)]

ans = sum(S)
if ans % 10 == 0: # 10の倍数の時
    min_s = float('inf')
    for s in S: # sの中から, 10の倍数でない、かつ最小のものを探してくる
        if s % 10 != 0:
            min_s = min(min_s, s)
    if min_s == float('inf'): # sの中に10の倍数でないものがなかったとき
        ans = 0
    else:
        ans -= min_s

print(ans)

# bit 全探索したらTLEした
# ans = 0
# # bit 全探索する
# for bit in range(1 << N):
#     sum = 0
#
#     for i in range(N):
#         # bit にi 番目のフラグが立っているかどうか
#         if bit & (1 << i):
#             # フラグが立っているならsumに加算する
#             sum += S[i]
#
#     if sum % 10 == 0:
#         sum = 0
#     ans = max(ans, sum)
#
# print(ans)

