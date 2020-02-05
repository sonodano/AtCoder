#%%
H, A = map(int, input().split())

ans = 1
while True:
    if H <= A * ans:
        break
    ans += 1

print(ans)