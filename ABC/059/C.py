n = int(input())
A = list(map(int, input().split()))

#%%
ans = float('inf')
# 直感的にはAの平均周辺が最小値っぽい
mean = sum(A)//n
means = [mean-1, mean, mean+1]
for m in means:
    tmp = 0
    for a in A:
        tmp += (m - a)**2
    ans = min(ans, tmp)

print(ans)

