#%%
from collections import Counter
N = int(input())

memo = [int(input()) for _ in range(N)]


cnt = Counter(memo)

ans = 0
for v in cnt.values():
    if v % 2 == 1:
        ans += 1

print(ans)