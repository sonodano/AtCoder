#%%
S = str(input())

count = 0
ans = 0
for s in S:
    if s in 'AGCT':
        count += 1
        ans = max(ans, count)
    else:
        count = 0

print(ans)

