#%%
n = int(input())
A = [int(input()) for _ in range(n)]

#%%
idx = 0
visited = set()
count = 0
flag = False

for i in range(n):
    next_idx = A[idx]
    next_idx -= 1
    visited.add(idx)

    if idx == 1:
        flag = True
        break
    elif next_idx in visited:
        break
    count += 1
    idx = next_idx

if flag:
    print(count)
else:
    print(-1)
