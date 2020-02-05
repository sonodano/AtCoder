#%%
# こちらを参考に再帰関数を勉強する
# https://qiita.com/dhirabayashi/items/2f079e62fa2e286f1766
# nを受け取って、1からnまでの和を返す

def total(n):
    if n < 1: # 再帰ループが止まるための条件
        return 0

    # 再帰関数を実装する上での考え方
    # あたかも関数が実装済みであるかのように考える
    # 最終的な合計値は 「n + (n-1)までの合計値」
    # 「(n-1)までの合計値」が「実装済みである」と考える
    return n + total(n - 1)

print(total(5))
print(total(10))
print(total(100))

#%%
# 各要素を二倍にしたリストを出力する
def double_list(lst):
    if lst == []: # まず、例外条件（ここではリストが空の場合）を考える
        return []

    # 次に再帰呼び出しするところを考える。
    # 値を二倍にしたfirstと、各要素を2倍にし終わったrestを結合すればよい
    # 「各要素を二倍にしたrest」の関数は実装済みと考える
    first = lst[0]
    rest = lst[1:]
    return [first * 2] + double_list(rest) # 呼び出されるたびに要素が減っていき上記のifに引っかかる

print(double_list([1, 2, 3]))
print(double_list([4, 5, 6, 7]))

#%%
# アッカーマン関数を計算してみる
# Ack(0, n) = n + 1
# Ack(m, 0) = Ack(m-1, 1)
# Ack(m, n) = Ack(m-1, Ack(m, n-1)), m != 0, n != 0
def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

print(ack(3, 3))
print(ack(0, 5))
#print(ack(5, 0)) # これはでかすぎてpythonだと再帰できない
print(ack(4, 1))
