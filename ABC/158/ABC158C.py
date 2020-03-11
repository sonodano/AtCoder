#%%
a, b = map(int, input().split())

eight_min = a / 0.08
eight_max = (a+1) / 0.08
ten_min = b / 0.1
ten_max = (b + 1) / 0.1

ans = False
for p in range(int(eight_min), int(eight_max)):
    if eight_min <= p < eight_max and ten_min <= p < ten_max:
        ans = p
        break


if ans:
    print(ans)
else:
    print(-1)