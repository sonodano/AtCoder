#%%
N  = int(input())
A = list(map(int, input().split()))


sA = set(A)
if len(A) == len(sA):
    print('YES')
else:
    print('NO')
