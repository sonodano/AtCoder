#%%
n = int(input())
H = list(map(int, input().split()))

#%%
def change_min(a, b):
    if a > b:
        return b
    else:
        return a

dp_cost = [float('inf')] * n
dp_cost[0] = 0

for i in range(1, n):
    dp_cost[i] = change_min(dp_cost[i], dp_cost[i-1] + abs(H[i] - H[i-1]))
    if i > 1: # i = 1のときi-2は存在しない
        dp_cost[i] = change_min(dp_cost[i], dp_cost[i-2] + abs(H[i] - H[i-2]))

print(dp_cost[-1])

