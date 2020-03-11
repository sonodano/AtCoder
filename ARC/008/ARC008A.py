#%%
N = int(input())


tens = N // 10
ones = N % 10

if ones < 7:
    ans = 100 * tens + 15 * ones
else:
    ans = 100 * (tens + 1)

print(ans)