#%%
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

flag = True
if n < m:
    flag = False
else:
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(m):
        if A[i] < B[i]:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')
