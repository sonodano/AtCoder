#%%
import itertools
n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

#%%
cnt = 0
for bits in itertools.product([0, 1], repeat=n):
    # ライトの配列の初期化
    lights = [0] * m

    # 電球ごとのONになってるスイッチの数をカウント
    # スイッチのindexでループを回す
    for i in range(n):
        if bits[i] == 1: #スイッチがONのとき
            sw = i + 1 # スイッチの番号
            for j in range(len(ks)): # 全部のlight-switchの配線を確認
                if sw in ks[j][1:]: # 配線がつながってるとき
                    lights[j] += 1 # そのlightに1を加算

    # カウント終了後条件判別
    # 2で割ったあまり
    m_lights = [l%2 for l in lights]
    if m_lights == p:
        cnt += 1

print(cnt)




