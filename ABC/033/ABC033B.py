#%%
N = int(input())

d = {}
for _ in range(N):
    n, p = input().split()
    p = int(p)
    d[n] = p

#%%
total_v = sum(d.values())
max_k, max_v = max(d.items(), key=lambda x: x[1])

if max_v > total_v/2:
    print(max_k)
else:
    print('atcoder')