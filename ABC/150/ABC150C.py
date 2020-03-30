#%%
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

import itertools

idx = 1
for l in itertools.permutations(range(1, N+1)):
    if l == P:
        a = idx
    if l == Q:
        b = idx

    idx += 1

print(abs(a-b))
