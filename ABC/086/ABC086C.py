#%%
N = int(input())

t = 0
x = 0
y = 0
flag = True
for _ in range(N):
    tn, xn, yn = map(int, input().split())
    dt = tn - t
    l1 = abs(xn - x) + abs(yn - y)
    if (l1 <= dt) and (tn % 2 == (xn + yn) % 2):
        continue
    else:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')
