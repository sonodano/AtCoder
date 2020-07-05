#%%
# TODO 要復習 考え方はあってそうだけどコードができな...（尺取り法というらしい）
n, k = map(int, input().split())
A = list(map(int, input().split()))

#%%
ans = 0
total = 0

right = 0
for left in range(n):
    while total < k: # kを超えるまで続ける
        if right == n: # kを超えずに右終端まで来たとき
            break
        else:
            total += A[right]
            right += 1  # 右端を一つ進める

    # 終端まで行ってもkを超えないときは終了
    if total < k:
        break

    ans += n - right + 1 # kがrightまでの範囲でkをこえていれば、あとはいくら足しても条件を満たす
    total -= A[left] # 左端を一つ進める
print(ans)


#%%
# ↓できなかったやつ
# ans = 0
#
# # 初めて[a0,.., am] > kとなるものを求める（初期化処理）
# for j in range(1, n+1):
#     psum = sum(A[:j])
#     if psum >= k:
#         right = j - 1 # 右端
#         ans += n - right
#         break
# print(psum, n - right, 0, right)
# # psum - a0 + am+l したものがkを超えるか判定
# for i in range(1, n):
#     psum += -A[i-1] # ひとつ前のループの先頭の値を削除
#
#     if i == right:
#         right += 1
#     # 先頭を一つ進めても、kを超えてる場合
#     if psum >= k:
#         ans += n - right
#         print(psum, n - right, i, right)
#     # 先頭を進めると、k未満になる場合
#     else:
#         for j in range(right+1, n):
#             psum_tmp = psum
#             psum_tmp += A[j]
#             print(A[j])
#             # print(A[j])
#             if psum_tmp >= k:
#                 right = j
#                 psum = psum_tmp
#                 ans += n - right
#                 print(psum, n - right, i, right)
#                 break
#
# print(ans)