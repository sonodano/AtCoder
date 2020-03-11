#%%
N, M = map(int, input().split())

ans = set([i for i in range(1, M+1)])
for _ in range(N):
    tabemono = list(map(int, input().split()))
    tabemono = set(tabemono[1:])
    ans = ans & tabemono

print(len(ans))
