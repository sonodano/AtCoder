#%%
l, r = map(int, input().split())

if r - l >= 2019:
    ans = 0
else:
    ans = 2019
    flag = False
    for i in range(l, r):
        for j in range(i+1, r+1):
            m = (i * j) % 2019
            ans = min(ans, m)
            if ans == 0:
                flag = True
                break
        if flag:
            break

print(ans)