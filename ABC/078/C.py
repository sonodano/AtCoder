#%%
n, m = map(int, input().split())
# 初めて成功するまでの確率分布=幾何分布
# 幾何分布の期待値, 1/p
ans = (1900 * m + 100 * (n - m)) / (1/2)**m
print(int(ans))