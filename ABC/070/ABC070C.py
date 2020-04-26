import fractions

n = int(input())
ts = [int(input()) for _ in range(n)]

ans = ts[0]
for i in range(1, n):
    ans = ans * ts[i] // fractions.gcd(ans, ts[i])
print(ans)
