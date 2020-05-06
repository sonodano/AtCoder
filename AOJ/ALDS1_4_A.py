#%%
n = int(input())
s = set(map(int, input().split()))
q = int(input())
t = set(map(int, input().split()))

#%%
cnt = 0
for si in s:
    if si in t:
        cnt += 1

print(cnt)