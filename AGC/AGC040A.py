#%%
# 理屈は分かったが書き方がわからなかった...
# 答え: https://www.programming-pack.com/entry/2019/11/04/235625


s = list(input())

# 不等式の向きを記録する
memo = ''

# 不等式の連続した個数を記録する
cnt = 0

# 1つ前に数えた不等式の連続した個数を記録する
before_cnt = 0
s = input()
n = len(s) + 1
a = [0] * n
b = [0] * n
for i in range(n - 1):
    if s[i] == '<':
        a[i + 1] = a[i] + 1
    if s[-i - 1] == '>':
        b[i + 1] = b[i] + 1

print(sum([max(i, j) for i, j in zip(a, b[::-1])]))
# 答え
ans = 0

# 文字列Sの連続したふとうしきの向きを数える
for i in s:
    # はじめはmemoが空白なので、memoに不等式の向きを記録
    if memo == '':
        memo = i

    # 不等式の向きが同じ場合は数を1カウントしてループに戻る
    if memo == i:
        cnt += 1

    # 不等式の向きが異なる場合
    else:
        # ansに和を加算する
        ans += cnt * (cnt + 1) // 2

        # 不等式の向きの変化が処理が必要な場合
        if memo == '>':
            if before_cnt < cnt:
                ans -= before_cnt
            else:
                ans -= cnt

        before_cnt = cnt
        cnt = 1
        memo = i
else:
    ans += cnt * (cnt + 1) // 2
    if before_cnt < cnt:
        if memo == '>':
            ans -= before_cnt
    else:
        if memo == '>':
            ans -= cnt
    before_cnt = cnt
    cnt = 0

print(ans)

'''
これのほうが賢い
s=input()
n=len(s)+1
a=[0]*n
b=[0]*n
for i in range(n-1):
    if s[i]=='<':
        a[i+1]=a[i]+1
    if s[-i-1]=='>':
        b[i+1]=b[i]+1
 
print(sum([max(i,j) for i,j in zip(a,b[::-1])]))
'''