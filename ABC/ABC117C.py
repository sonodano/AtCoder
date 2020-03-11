#%%
N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()
if N >= M:
    ans = 0
else:
    x_diff = [xn - x for xn, x in zip(X[1:], X[:-1])] #[X[i + 1] - X[i] for i in range(len(X) - 1)]
    # for _ in range(N - 1): # 遅すぎてTLE
    #     x_diff.remove(max(x_diff))
    x_diff.sort(reverse=True)
    ans = sum(x_diff[N-1:])

print(ans)
