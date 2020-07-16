#%%
n = int(input())
s = input()

#%%
ans = 0
for i in range(n):
    left = set(s[i:])
    right = set(s[:i])
    ans = max(ans, len(left & right))

print(ans)

