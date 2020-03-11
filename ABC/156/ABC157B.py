#%%
N, K = map(int, input().split())


def base_10_to_n(X, n):
    if (int(X / n)):
        return base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)

ans = len(str(base_10_to_n(N, K)))
print(ans)