# TODO 要復習
#%%
import fractions
N = int(input())
mons = tuple(map(int, input().split()))

ans = mons[0]
for m in mons:
    ans = fractions.gcd(ans, m)

print(ans)