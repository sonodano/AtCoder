#%%
from itertools import permutations
N = int(input())

towns = []
for i in range(N):
    towns.append(list(map(int, input().split())))

perm = list(permutations(towns))

def calc_l2(p_next, p):
    return ((p_next[0] - p[0])**2 + (p_next[1] - p[1])**2) ** 0.5

l2_norm = 0
for p in perm:
    for i in range(len(p) - 1):
        l2_norm += calc_l2(p[i+1], p[i])

print(l2_norm/len(perm))







