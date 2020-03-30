#%%
N, K, M = map(int, input().split())
a_list = list(map(int, input().split()))


ans = M * N - sum(a_list)
if ans <= K:
    print(max(0, ans))
else:
    print(-1)