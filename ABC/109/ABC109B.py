#%%
import sys
N = int(input())

W = [input() for _ in range(N)]


for i in range(N-1):
    if W.count(W[i]) >= 2:
        print('No')
        sys.exit()
    if W[i][-1] != W[i+1][0]:
        print('No')
        sys.exit()

print('Yes')
