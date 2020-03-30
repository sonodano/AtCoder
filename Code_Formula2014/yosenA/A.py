#%%
# A ** (1/3)を1000とかがintになってくれない謎
A = int(input())

flag = False
for i in range(1, 101):
    if A == i**3:
        flag = True
        break

if flag:
    print('YES')
else:
    print('NO')