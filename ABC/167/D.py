#%%
# 考え方はあってそうだが？
# TODO 要復習
# →TLEするのは hoge in listをやっていたから。dict.key, setはo(1)で検索できるけど、listは最悪o(n)
# # https://qiita.com/bee2/items/4ab87d05cc03d53e19f9
# トポロジカルソートで解決できそうだけどわからん！
n, k = map(int, input().split())

field = [(i, j) for i, j in zip(range(n), list(map(int, input().split())))]

#%%
town = 0 # 町は1始まりだが、indexの都合上-1する
order = 0 # 訪問順序
visited = {town: order} # 訪問済みの街を格納

while True:
    trans = field[town][1] - 1 # 現在のtownにあるテレポーターの移動先
    n_town = field[trans][0] # 遷移先の町. これはリストのindexになってるので-1しなくてよい
    if n_town not in visited.keys():
        order += 1
        visited[n_town] = order  # 訪問済みにする
    else: # 訪問済みを踏んだ時 TODO この実装だとループ内の数が数えられない
        st_circ = visited[n_town]
        break
    town = n_town

#%%
# ループ開始前まで
vk = list(visited.keys())
mae = len(vk[:st_circ])
circ = len(vk[st_circ:])

if k < mae:
    ans = vk[k]
else:
    idx = (k - mae) % circ
    ans = vk[idx + mae]

print(ans+1)