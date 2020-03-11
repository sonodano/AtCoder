#%%
X, Y = map(int, input().split())

ans = 0
while True:
    if Y < X * 2 ** ans:
        break
    ans += 1

print(ans)