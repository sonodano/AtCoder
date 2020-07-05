#%%
n = int(input())
H = list(map(int, input().split()))

#%%
cnt = 0
ans = 0
for i in range(n-1):
    if H[i] >= H[i+1]:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)

print(ans)