#%%
a = int(input())

def base_n_to10(X, n):
    X = str(X)
    out = 0
    for i in range(1, len(str(X))+1):
        out += int(X[-i]) * (n**(i-1))
    return out#int out

k = 10
ans = -1
while True:
    N = base_n_to10(k, k)
    if N == a:
        ans = k
        break
    elif N > a:
        break

    k += 1

print(ans)