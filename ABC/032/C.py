#%%
# TODO 要復習
n, k = map(int, input().split())
S = [int(input()) for _ in range(n)]

#%%
ans = 0
total = 1
right = 0

for left in range(n):
    while right < n and total * S[right] <= k: # kを超えるまで続ける
        total *= S[right]
        right += 1

    if total == 0:
        ans = n
        break
    ans = max(ans,  right - left)
    if left == right:
        right += 1
    else:
        total //= S[left]

print(ans)