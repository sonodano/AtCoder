
r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))

#%%
N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        if r1[i] == b:
            r1[i] = 0
        if r2[i] == b:
            r2[i] = 0
        if r3[i] == b:
            r3[i] = 0

#%%
flag = False
if sum(r1) == 0:
    flag = True
if sum(r2) == 0:
    flag = True
if sum(r3) == 0:
    flag = True
for i in range(3):
    if sum([r1[i], r2[i], r3[i]]) == 0:
        flag = True
if sum([r1[0], r2[1], r3[2]]) == 0:
    flag = True
if sum([r1[2], r2[1], r3[0]]) == 0:
    flag = True

if flag == True:
    print('Yes')
else:
    print('No')