#%%
from collections import Counter
N = int(input())
S = Counter(list(input() for _ in range(N)))

#%%
max_v = max(S.values())
words = []
for k, v in S.most_common():
    if v == max_v:
        words.append(k)
    else:
        break

words.sort()
for w in words:
    print(w)