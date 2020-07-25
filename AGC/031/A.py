#%%
# TODO 要復習
from collections import Counter
n = int(input())
S = input()
R = 1000000007

#%%
count = Counter(S)
ans = 1
for c in count.values():
    ans = ans * (c + 1) % R

print(ans - 1)