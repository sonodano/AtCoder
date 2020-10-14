#%%
K = int(input())
#%%
cnt = 1
base = 1
if K % 2 == 0:
    ans = -1
else:
    while True:
        if base % K == 0:
            ans = cnt
            break
        base = base * 10 + 1
        cnt += 1

print(ans)

#%%
print((10**(3)-1)/9)