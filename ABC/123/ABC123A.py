#%%
antenna = [int(input()) for _ in range(5)]
k = int(input())

#%%
import itertools

flag = True
for v1, v2 in itertools.combinations(antenna, 2):
    if abs(v1 - v2) > k:
        flag = False
        break

if flag:
    print('Yay!')
else:
    print(':(')


