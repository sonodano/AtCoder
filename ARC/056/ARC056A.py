#%%
a, b, k, l = map(int, input().split())

# 制約条件でセットで買ったほうが安いことは決まってる
num_set = k // l
num_ind = k % l

# 個別購入したほうが安いのか、セットで買ったほうが安いのか
if num_ind * a >= b:
    ans = num_set * b + b
else:
    ans = num_set * b + num_ind * a

print(ans)

