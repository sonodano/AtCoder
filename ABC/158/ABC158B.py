#%%
n, a, b = map(int, input().split())

tmp = n // (a + b)
amari = n % (a + b)
ans = a * tmp


if amari >= a:
    ans += a
elif amari < a:
    ans += amari

print(ans)