#%%
import itertools
N = int(input())
K = int(input())

cards = [input() for _ in range(N)]

numbers = []
for v in itertools.permutations(cards, r=K):
    numbers.append(''.join(v))

print(len(set(numbers)))

#%%
