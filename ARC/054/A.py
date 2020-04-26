#%%
l, x, y, s, d = map(int, input().split())

#%%
if s == d:
    ans = 0
elif s < d: # sがdよりも手前にあるとき
    # 時計回り
    clockwise = (d-s)/(x + y)
    # 反時計回り
    if x >= y: # 床の回転速度のほうが、反時計回りの歩み寄り早いときはゴールに到達できない
        anti = float('inf')
    else:
        anti = (l - (d - s)) / (y - x)
    ans = min(clockwise, anti)
else: # sがdよりも後ろにあるとき
    # 時計回り
    clockwise = (l - (s - d)) / (x + y)
    # 反時計回り
    if x >= y:
        anti = float('inf')
    else:
        anti = (s - d) / (y - x)
    ans = min(clockwise, anti)

print(ans)
