#%%
n = int(input())
X = list(map(int, input().split()))

sortX = sorted(X)
#%%
lB = sortX[n//2-1]
rB = sortX[n//2]

for x in X:
    if x <= lB:
        print(rB)
    else:
        print(lB)
