#%%
# TODO 要復習, 直感的にはすべてのXORが0になればよい→嘘解法
n = int(input())
A = list(map(int, input().split()))

#%%
setA = set(A)
if len(setA) == 1:
    if sum(A) == 0:
        ans = 'Yes'
    else:
        ans = 'No'

elif len(setA) == 2:
    a1, a2 = sorted(setA)
    if (a1 == 0) and (A.count(a1) * 3 == n):
        ans = 'Yes'
    else:
        ans = 'No'

elif len(setA) == 3:
    a1, a2, a3 = setA
    if (a1 ^ a2 ^ a3 == 0) and (A.count(a1) == A.count(a2) == A.count(a3)):
        ans = 'Yes'
    else:
        ans = 'No'
else:
    ans = 'No'

print(ans)