#%%
n = int(input())

rl = []
bl = []
for _ in range(n):
    x, c = input().split()
    if c == 'R':
        rl.append(int(x))
    elif c == 'B':
        bl.append(int(x))

#%%
rl.sort()
bl.sort()
for r in rl:
    print(r)
for b in bl:
    print(b)