#%%
W, H, x, y = map(int, input().split())

# 最大はちょうど半分に切ったとき = x, yがどこにあっても中心を通ればちょうど半分
s = W * H / 2
# x, yが中心の時は無限に切り方がある
if W / 2 == x and  H / 2 == y:
    w = 1
else:
    w = 0

print(s, w)