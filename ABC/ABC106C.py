#%%
S = input()
K = int(input())

count = 0
for s in S:
    if s == '1':
        count += 1
    else:
        break

if K <= count:
    ans = 1
else:
    ans = S[count]

print(ans)