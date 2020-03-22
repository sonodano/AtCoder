#%%
n = int(input())

# 全探索→長辺x短辺なので半分まで探索すれば良い
cost = 1000000000
for i in range(1, n//2+2): # (1, n//2+1)だとn=1のときループが回らない
    for j in range(1, n//2+2):
        if i * j > n:
            break

        nc = abs(i - j) + n - i * j
        cost = min(nc, cost)

print(cost)