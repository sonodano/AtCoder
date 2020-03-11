#%%
N = int(input())
X = list(map(int, input().split()))

#%%
meanX = sum(X)//len(X)

a1 = 0
for x in X:
    a1 += (x -  meanX)**2
a2 = 0
for x in X:
    a2 += (x- meanX + 1) ** 2

a3 = 0
for x in X:
    a3 += (x - meanX - 1) **2

ans = min(a1, a2, a3)
print(ans)