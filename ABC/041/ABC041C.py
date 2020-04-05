#%%
n = int(input())
A = list(map(int, input().split()))
k = list(range(1, n+1))
d = dict(zip(k, A))

d_sorted = sorted(d.items(), key=lambda x:x[1], reverse=True)
for kv in d_sorted:
    print(kv[0])