# 愚直に実装
n, m = map(int, input().split())

box = [1] * n
flags = [False] * n
flags[0] = True

#%%
for _ in range(m):
    before_idx, after_idx = map(int, input().split())
    before_idx -= 1
    after_idx -= 1
    box[before_idx] -= 1
    box[after_idx] += 1

    if flags[before_idx] == True: # 移動元に赤玉があるとき
        if box[before_idx] == 0: # 移動元に赤玉しかなかったとき
            flags[before_idx] = False
        flags[after_idx] = True # 移動先に赤玉がある可能性

print(sum(flags))