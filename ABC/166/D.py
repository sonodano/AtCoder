#%%
x = int(input())
#%%
flag = False
for a in range(10001):
    for b in range(-1000, 1000):
        s = a**5 - b**5
        if s == x:
            flag = True
            break
    if flag:
        break

print(a, b)