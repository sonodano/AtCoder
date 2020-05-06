#%%
# 深さ優先探索の勉強
# TODO: 要復習
# https://qiita.com/saba/items/affc94740aff117d2ca9#%E4%BE%8B%E9%A1%8C-2-1-1-lake-counting-poj-no2386

N, M = map(int, input().split())

relation = [list(map(int, input().split())) for _ in range(M)]
