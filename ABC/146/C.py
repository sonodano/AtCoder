#%%
# TODO わからなかった
a, b, x = map(int, input().split())

#%%
def calc_cost(n):
    return a * n + b * len(str(n))

right = int(1e9)
center = right // 2
left = 0

if calc_cost(right) <= x:
    ans = int(1e9)
else:
    ans = int(1e9)
    # 二分探索
    for i in range(100):
        if calc_cost(center) < x: # 買える
            left = center
            center = (right + left) // 2
        elif calc_cost(center) > x: # 買えない
            right = center
            center = (right + left) // 2

        if ans == center:
            break
        else:
            ans = center

print(ans)