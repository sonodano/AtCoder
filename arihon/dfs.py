#%%
# 部分和問題
# 配列aから適当にチョイスして、合計がkに一致すれば’Yes’
n = 4   # 配列の長さ
a = [1, 2, 4, 7] # 与えられる配列
k = 13  # 合計値

# i まででsumを作って、残りi 以降を調べる
def dfs(i, sum):
    # n個決め終わったら、今までの和 sumがkと等しいかを返す
    if i == n:
        return sum == k

    # a[i]を使わない場合
    if dfs(i + 1, sum):
        return True

    # a[i] を使う場合
    if dfs(i + 1, sum + a[i]):
        return True

    # a[i]を使う使わないにかかわらず k が作れないのでFalseを返す
    return False

if dfs(0, 0):
    print('Yes')
else:
    print('No')

# 再帰はわかりにくいな…

#%%
# bit全探索で解く
for bit in range(1 << n):
    sum = 0
    for i in range(n):
        # bit にi番目のフラグが立っているかどうか
        if bit & (1 << i):
            # フラグが立っているならばsumに加算する
            sum += a[i]

    if sum == k:
        print('Yes')
        import sys
        sys.exit()

print('No')