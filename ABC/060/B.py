#%%
A, B, C = map(int, input().split())

#%%
m = 1
while True:
    if (A * m) % B == 0:
        ans = 'NO'
        break
    elif (A * m) % B == C:
        ans = 'YES'
        break
    m += 1

print(ans)