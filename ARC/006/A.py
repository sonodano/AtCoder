#%%
e = list(input().split())
b = input()
l = list(input().split())

#%%
cnt = 0
for i in e:
    if i in l:
        cnt += 1

if cnt == 6:
    print(1)
elif cnt == 5:
    if b in l:
        print(2)
    else:
        print(3)
elif cnt == 4:
    print(4)
elif cnt == 3:
    print(5)
else:
    print(0)