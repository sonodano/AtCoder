#%%
# https://qiita.com/saba/items/affc94740aff117d2ca9
S = input()
n = len(S)

def dfs(i, f):
    # iがindex番号, fが文字列. 再帰関数なのでiがループの代わり
    # fに探索結果を格納していく
    if i == n-1: # Sの最後まで行ったら合計をとる
        l = list(map(int, f.split('+')))
        return sum(l)

    return dfs(i + 1, f + S[i + 1]) + dfs(i + 1, f + '+' + S[i + 1]) # なのもしないパターンと'+'を追加するパターン

print(dfs(0, S[0]))