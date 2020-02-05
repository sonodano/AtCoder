#%%
K, A, B = map(int, input().split())

ans = 1
if A + 1 >= B  or A >= K:
    ans += K
else:
    # ビスケットがA がたまるまでの操作回数
    K -= A - 1
    # A枚→1円→B枚で2回操作
    r = K // 2
    m = K % 2
    ans = A +  r * (B - A) + m

print(ans)
