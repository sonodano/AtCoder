#%%
H = int(input())

n = 0
while True:
    if 2 ** n <= H < 2 ** (n+1):
        break
    n += 1
if n == 0:
    ans = 1
else:
    ans = 1
    for i in range(1, n+1):
        ans += 2**i

print(ans)