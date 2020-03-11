#%%
# TODO わからんかった

p = 10000000007
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

def cmb_mod(n, r, p):
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)

    return cmb(n, r, p)
#%%
n, a, b = map(int, input().split())

#%%
# 二項係数の和
# nC0=1はないので引いとく
total = pow(2, n, p)
#%%
# aについての組み合わせ
ap = cmb_mod(n, a, p)
#%%

# bについて
bp = (cmb(n, b)) % r

ans = (total - ap - bp) % r
print(ans)

#%%
