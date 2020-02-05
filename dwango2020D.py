#%%
N = int(input())
a_list = list(map(int, input().split()))

#%%
import itertools
for x in itertools.permutations(range(N)):
    print(x)
